-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: Config

local flatbuffers = require('flatbuffers')

---@class TestType_ : TestType___mt 
 local TestType_ = {} -- the module
 ---@class TestType___mt 
 local TestType__mt = {} -- the class metatable
 
function TestType_.New()
    local o = {}
    setmetatable(o, {__index = TestType__mt})
    return o
end
function TestType_.GetRootAsTestType_(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = TestType_.New()
    o:Init(buf, n + offset)
    return o
end
function TestType__mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function TestType__mt:Types(j)
    local o = self.view:Offset(4)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:Get(flatbuffers.N.Int32, a + ((j-1) * 4))
    end
    return 0
end
function TestType__mt:TypesLength()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestType__mt:Id()
    local o = self.view:Offset(6)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestType_.Start(builder) builder:StartObject(2) end
function TestType_.AddTypes(builder, types) builder:PrependUOffsetTRelativeSlot(0, types, 0) end
function TestType_.StartTypesVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestType_.AddId(builder, id) builder:PrependInt32Slot(1, id, 0) end
function TestType_.End(builder) return builder:EndObject() end

return TestType_ -- return the module