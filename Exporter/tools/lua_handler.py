import collections
import json
import tools.utility as utility
import tools.string_script as string_script
import tools.script_exporter as script_exporter


def to_list_data(obj, msg):
    # fields = msg.get_msg_fields()
    # data = []
    # index = -1
    # for k, v in obj.items():
    #     index = index + 1
    #     filed = fields[index]
    #     is_add = False
    #     if isinstance(v,list):
    #        data.append(get)
    #
    #     elif isinstance(v,dict):
    #         if len(v) == 0:
    #             data.append(None)
    #         else:
    #             data.append(to_list_data(v,msg))
    #         is_add = True
    #     if not is_add:
    #         data.append(v)
    return get_obj_data(obj)


def get_list_data(value):
    if len(value) == 0:
        return None
    data = []
    for v in value:
        if isinstance(v, list):
            raise ValueError("Error get_list_data")
        elif isinstance(v, dict):
            data.append(get_obj_data(v))
        else:
            data.append(get_base_data(v))
    return data


def get_obj_data(value):
    if value is None or len(value) == 0:
        return None
    data = []
    for k, v in value.items():
        if isinstance(v, list):
            data.append(get_list_data(v))
        elif isinstance(v, dict):
            data.append(get_obj_data(v))
        else:
            data.append(get_base_data(v))
    return data


def get_base_data(value):
    return value


def get_lua_data(obj, indent=1, lines=True):
    if utility.is_base_type(obj):
        yield json.dumps(obj, ensure_ascii=False)
    else:
        yield '{'
        is_list = isinstance(obj, list)
        is_first = True
        for i in obj:
            if is_first:
                is_first = False
            else:
                yield ','
            if lines:  ##is_root
                yield utility.newline(indent)
            if not is_list:
                k = i
                i = obj[k]
                yield k
                yield ' = '
            if i is None:
                yield 'nil'
            else:
                for part in get_lua_data(i, indent + 1, lines):
                    yield part
        if lines:  ##is_root
            yield utility.newline(indent - 1)
        yield '}'


def get_msg_lua_fields_indexes_name(msg):
    return msg.get_proto_name() + "FieldsIndex"


def get_msg_lua_custom_name(msg):
    return msg.get_proto_name() + "Custom"


def get_message_lua_fields(msg):
    types = msg.get_msg_fields()
    filed_script = string_script.StringScript("local %s ={" % get_msg_lua_fields_indexes_name(msg))
    all_customs = msg.get_all_msg()
    customs = collections.OrderedDict()
    for i in range(len(types)):
        filed_info = types[i]
        filed_script.add_space_line("%s = %s," % (filed_info.get_filed_name(), i + 1))
        if all_customs.__contains__(filed_info.get_filed_type()):
            if filed_info.get_is_list():
                customs[filed_info.get_filed_name()] = (1, all_customs[filed_info.get_filed_type()])
            else:
                customs[filed_info.get_filed_name()] = (0, all_customs[filed_info.get_filed_type()])

    filed_script.add_line("}")
    for key, used_msg in msg.get_all_msg().items():
        filed_script.add_line(get_message_lua_fields(used_msg))

    if len(customs) > 0:
        filed_script.add_line("local %s ={" % get_msg_lua_custom_name(msg))
        for key, v in customs.items():
            filed_script.add_space_line("%s = {%s,%s}," % (key, v[0], get_msg_lua_fields_indexes_name(v[1])))
        filed_script.add_line("}")
    return filed_script.get_value()


def get_list_lua_script(info):
    file_name = info.get_proto_name()
    msg = info.get_message()
    obj = info.get_value()
    is_list = not info.is_single()
    if not is_list:
        raise ValueError("%s is not a list table!!!",file_name)
    single_data = obj[list(obj.keys())[0]]
    filed_script = string_script.StringScript(get_message_lua_fields(msg))

    script = string_script.StringScript('---@type %s' % file_name)
    script.add_line(filed_script.get_value())
    script.add_line("local T = {}")
    index = 0
    for row_data in single_data:
        index = index + 1
        function = "function T.T%s()" % index
        function_script = string_script.StringScript(function)
        list_data = to_list_data(row_data, msg)
        table_data = "".join(script_exporter.get_lua_data(list_data, False))
        function_script.add_space_line("return %s" % table_data)
        function_script.add_line("end")
        script.add_line(function_script.get_value())

    function_read_only = string_script.StringScript("local function table_read_only(t)")
    function_read_only.add_line("  local temp= {}")
    function_read_only.add_line("  local mt = {")
    function_read_only.add_line("    __index = t,")
    function_read_only.add_line("    __newindex = function(t, k, v)")
    function_read_only.add_line("        error('error write to a read-only table with key = ' .. tostring(k)"
                                "..', " "value ='..tostring(v))")
    function_read_only.add_line("    end")
    function_read_only.add_line("  }")
    function_read_only.add_line("  setmetatable(temp, mt)")
    function_read_only.add_line("  return temp")
    function_read_only.add_line("end")
    script.add_line(function_read_only.get_value())

    function_new = string_script.StringScript("local function New(data,tableIndexes)")
    function_new.add_space_line("local t = {}")
    function_new.add_space_line("for k,v in pairs(tableIndexes) do")
    function_new.add_space_line("   local c = %s[k]" % get_msg_lua_custom_name(msg))
    function_new.add_space_line("   local d = data[v]")
    function_new.add_space_line("   if c == nil then")
    function_new.add_space_line("      t[k]= d")
    function_new.add_space_line("   else")
    function_new.add_space_line("     if c[1] == 1 then")
    function_new.add_space_line("        local t_c = {}")
    function_new.add_space_line("        for index = 1,#d do")
    function_new.add_space_line("            table.insert(t_c, New(d[index],c[2]))")
    function_new.add_space_line("        end")
    function_new.add_space_line("        t[k] = t_c")
    function_new.add_space_line("     else")
    function_new.add_space_line("        t[k] = New(d,c[2])")
    function_new.add_space_line("     end")
    function_new.add_space_line("   end")
    function_new.add_space_line("end")
    function_new.add_space_line("return table_read_only(t)")
    function_new.add_line_end()
    script.add_line(function_new.get_value())

    script.add_line('local %s = {\n  Values = {}\n}' % file_name)

    script.add_line("---@return %s%s" % (msg.name, msg.suffix))
    get_function = string_script.StringScript("function %s.GetTableByIndex(index)" % file_name)
    get_function.add_space_line("if %s.Values[index]==nil then" % file_name)
    get_function.add_space_line(" %s.Values[index]=New(%s['%s'..index](),%s)" % (file_name, "T","T", get_msg_lua_fields_indexes_name(msg)))
    get_function.add_space_line("end")
    get_function.add_space_line("return %s.Values[index]" % file_name)
    get_function.add_line_end()
    script.add_line(get_function.get_value())

    get_len_function = "function %s.GetLength()\n return %s" % (file_name, len(single_data))
    script.add_line(get_len_function)
    script.add_line("end")

    get_clear_function = "function %s.Dispose()\n %s.Values={}" % (file_name, file_name)
    script.add_line(get_clear_function)
    script.add_line("end")

    script.add_line('return %s' % file_name)
    return script.get_value()
