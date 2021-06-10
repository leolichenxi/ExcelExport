-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: Config

local flatbuffers = require('flatbuffers')

local TestObjArray_ = {} -- the module
local TestObjArray__mt = {} -- the class metatable

function TestObjArray_.New()
    local o = {}
    setmetatable(o, {__index = TestObjArray__mt})
    return o
end
function TestObjArray_.GetRootAsTestObjArray_(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = TestObjArray_.New()
    o:Init(buf, n + offset)
    return o
end
function TestObjArray__mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function TestObjArray__mt:A()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestObjArray__mt:B()
    local o = self.view:Offset(6)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestObjArray__mt:C()
    local o = self.view:Offset(8)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestObjArray_.Start(builder) builder:StartObject(3) end
function TestObjArray_.AddA(builder, a) builder:PrependInt32Slot(0, a, 0) end
function TestObjArray_.AddB(builder, b) builder:PrependInt32Slot(1, b, 0) end
function TestObjArray_.AddC(builder, c) builder:PrependInt32Slot(2, c, 0) end
function TestObjArray_.End(builder) return builder:EndObject() end

return TestObjArray_ -- return the module