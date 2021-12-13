import tools.utility as utility
import tools.script_exporter as script_exporter
import json


class Filed:
    def __init__(self, filed_name, filed_type, filed_des, is_list=False):
        self.filed_name = filed_name
        self.filed_type = filed_type
        self.filed_des = filed_des.replace('\n', '')
        self.is_list = is_list
        pass

    def get_name(self):
        return self.filed_name

    def get_is_list(self):
        return self.is_list

    def get_filed_name(self):
        if self.is_list:
            return self.filed_name + 's'
        return self.filed_name

    def get_flat_buffer_filed_name(self):
        flat_filed_name = self.get_filed_name()
        flat_filed_name = utility.convert_to_lower_snake_cake(flat_filed_name)
        return flat_filed_name

    def get_filed_type(self):
        return self.filed_type

    def get_defined_type(self):
        if self.is_list:
            return self.get_define_base_type() + '[]'
        return self.get_define_base_type()

    def get_define_base_type(self):
        if script_exporter.BaseProtoTypes.__contains__(self.filed_type):
            return script_exporter.BaseProtoTypes[self.filed_type]
        return self.filed_type

    def get_filed_des(self):
        return self.filed_des

    def get_define_proto(self, index):
        r = ''
        if self.is_list:
            r = ' repeated'
        return '%s %s %s = %s ; // %s' % (r, self.get_filed_type(), self.get_filed_name(), index, self.get_filed_des())

    def get_define_flat_scheme(self):
        """
        example v:[float:3];
        name:string;
        :return:
        """
        define_type = self.get_filed_type()
        if self.is_list:
            define_type = "[" + define_type + "]"
        return ' %s:%s ; // %s' % (self.get_flat_buffer_filed_name(), define_type, self.get_filed_des())

    def get_lua_api(self):
        r = ''
        if self.is_list:
            r = '[]'
        return '%s %s %s%s @%s ' % ("---@field ", self.get_filed_name(), self.get_filed_type(), r, self.get_filed_des())

    def get_lua_script(self):
        pass

    def scheme_info(self):
        return json.dumps((self.get_filed_name(), self.get_filed_type()), ensure_ascii=False, indent=2)
