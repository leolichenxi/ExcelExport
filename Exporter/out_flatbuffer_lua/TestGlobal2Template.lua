-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: Config

local flatbuffers = require('flatbuffers')

---@class TestGlobal2Template : TestGlobal2Template__mt 
 local TestGlobal2Template = {} -- the module
 ---@class TestGlobal2Template__mt 
 local TestGlobal2Template_mt = {} -- the class metatable
 
function TestGlobal2Template.New()
    local o = {}
    setmetatable(o, {__index = TestGlobal2Template_mt})
    return o
end
function TestGlobal2Template.GetRootAsTestGlobal2Template(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = TestGlobal2Template.New()
    o:Init(buf, n + offset)
    return o
end
function TestGlobal2Template_mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function TestGlobal2Template_mt:TestFloat()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float32, o + self.view.pos)
    end
    return 0.0
end
function TestGlobal2Template.Start(builder) builder:StartObject(1) end
function TestGlobal2Template.AddTestFloat(builder, testFloat) builder:PrependFloat32Slot(0, testFloat, 0.0) end
function TestGlobal2Template.End(builder) return builder:EndObject() end

return TestGlobal2Template -- return the module