-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: 

local flatbuffers = require('flatbuffers')

local CommonType = {} -- the module
local CommonType_mt = {} -- the class metatable

function CommonType.New()
    local o = {}
    setmetatable(o, {__index = CommonType_mt})
    return o
end
function CommonType.GetRootAsCommonType(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = CommonType.New()
    o:Init(buf, n + offset)
    return o
end
function CommonType_mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function CommonType_mt:Type()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function CommonType_mt:Id()
    local o = self.view:Offset(6)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function CommonType.Start(builder) builder:StartObject(2) end
function CommonType.AddType(builder, type) builder:PrependInt32Slot(0, type, 0) end
function CommonType.AddId(builder, id) builder:PrependInt32Slot(1, id, 0) end
function CommonType.End(builder) return builder:EndObject() end

return CommonType -- return the module