-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: Config

local flatbuffers = require('flatbuffers')

---@class TestGlobalTemplate : TestGlobalTemplate__mt 
 local TestGlobalTemplate = {} -- the module
 ---@class TestGlobalTemplate__mt 
 local TestGlobalTemplate_mt = {} -- the class metatable
 
function TestGlobalTemplate.New()
    local o = {}
    setmetatable(o, {__index = TestGlobalTemplate_mt})
    return o
end
function TestGlobalTemplate.GetRootAsTestGlobalTemplate(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = TestGlobalTemplate.New()
    o:Init(buf, n + offset)
    return o
end
function TestGlobalTemplate_mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function TestGlobalTemplate_mt:TestInt()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestGlobalTemplate_mt:TestStringArrays(j)
    local o = self.view:Offset(6)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:String(a + ((j-1) * 4))
    end
    return ''
end
function TestGlobalTemplate_mt:TestStringArraysLength()
    local o = self.view:Offset(6)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestString1()
    local o = self.view:Offset(8)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float64, o + self.view.pos)
    end
    return 0.0
end
function TestGlobalTemplate_mt:TestString()
    local o = self.view:Offset(10)
    if o ~= 0 then
        return self.view:String(o + self.view.pos)
    end
end
function TestGlobalTemplate_mt:TestFloat()
    local o = self.view:Offset(12)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float32, o + self.view.pos)
    end
    return 0.0
end
function TestGlobalTemplate_mt:TestDouble()
    local o = self.view:Offset(14)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float64, o + self.view.pos)
    end
    return 0.0
end
function TestGlobalTemplate_mt:TestBool()
    local o = self.view:Offset(16)
    if o ~= 0 then
        return (self.view:Get(flatbuffers.N.Bool, o + self.view.pos) ~= 0)
    end
    return false
end
function TestGlobalTemplate_mt:TestIntArrays(j)
    local o = self.view:Offset(18)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:Get(flatbuffers.N.Int32, a + ((j-1) * 4))
    end
    return 0
end
function TestGlobalTemplate_mt:TestIntArraysLength()
    local o = self.view:Offset(18)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestFloatArrays(j)
    local o = self.view:Offset(20)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:Get(flatbuffers.N.Float32, a + ((j-1) * 4))
    end
    return 0
end
function TestGlobalTemplate_mt:TestFloatArraysLength()
    local o = self.view:Offset(20)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestDoubleArrays(j)
    local o = self.view:Offset(22)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:Get(flatbuffers.N.Float64, a + ((j-1) * 8))
    end
    return 0
end
function TestGlobalTemplate_mt:TestDoubleArraysLength()
    local o = self.view:Offset(22)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestBoolArrays(j)
    local o = self.view:Offset(24)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:Get(flatbuffers.N.Bool, a + ((j-1) * 1))
    end
    return 0
end
function TestGlobalTemplate_mt:TestBoolArraysLength()
    local o = self.view:Offset(24)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestObj()
    local o = self.view:Offset(26)
    if o ~= 0 then
        local x = self.view:Indirect(o + self.view.pos)
        local obj = require('Config.TestObj_').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestObj1()
    local o = self.view:Offset(28)
    if o ~= 0 then
        local x = self.view:Indirect(o + self.view.pos)
        local obj = require('Config.TestObj1_').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestObjArrays(j)
    local o = self.view:Offset(30)
    if o ~= 0 then
        local x = self.view:Vector(o)
        x = x + ((j-1) * 4)
        x = self.view:Indirect(x)
        local obj = require('Config.TestObjArray_').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestObjArraysLength()
    local o = self.view:Offset(30)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestObjArray1s(j)
    local o = self.view:Offset(32)
    if o ~= 0 then
        local x = self.view:Vector(o)
        x = x + ((j-1) * 4)
        x = self.view:Indirect(x)
        local obj = require('Config.TestObjArray1_').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestObjArray1sLength()
    local o = self.view:Offset(32)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestDefineFromGlobal()
    local o = self.view:Offset(34)
    if o ~= 0 then
        local x = self.view:Indirect(o + self.view.pos)
        local obj = require('Position3d').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestDefineFromGlobal2s(j)
    local o = self.view:Offset(36)
    if o ~= 0 then
        local x = self.view:Vector(o)
        x = x + ((j-1) * 4)
        x = self.view:Indirect(x)
        local obj = require('Position3d').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestDefineFromGlobal2sLength()
    local o = self.view:Offset(36)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:TestCustomObj()
    local o = self.view:Offset(38)
    if o ~= 0 then
        local x = self.view:Indirect(o + self.view.pos)
        local obj = require('PositionArray3d').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestCustomObjArrays(j)
    local o = self.view:Offset(40)
    if o ~= 0 then
        local x = self.view:Vector(o)
        x = x + ((j-1) * 4)
        x = self.view:Indirect(x)
        local obj = require('PositionArray3d').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestGlobalTemplate_mt:TestCustomObjArraysLength()
    local o = self.view:Offset(40)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestGlobalTemplate_mt:Test1Int()
    local o = self.view:Offset(42)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestGlobalTemplate_mt:TestInt1()
    local o = self.view:Offset(44)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestGlobalTemplate.Start(builder) builder:StartObject(21) end
function TestGlobalTemplate.AddTestInt(builder, testInt) builder:PrependInt32Slot(0, testInt, 0) end
function TestGlobalTemplate.AddTestStringArrays(builder, testStringArrays) builder:PrependUOffsetTRelativeSlot(1, testStringArrays, 0) end
function TestGlobalTemplate.StartTestStringArraysVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTestString1(builder, testString1) builder:PrependFloat64Slot(2, testString1, 0.0) end
function TestGlobalTemplate.AddTestString(builder, testString) builder:PrependUOffsetTRelativeSlot(3, testString, 0) end
function TestGlobalTemplate.AddTestFloat(builder, testFloat) builder:PrependFloat32Slot(4, testFloat, 0.0) end
function TestGlobalTemplate.AddTestDouble(builder, testDouble) builder:PrependFloat64Slot(5, testDouble, 0.0) end
function TestGlobalTemplate.AddTestBool(builder, testBool) builder:PrependBoolSlot(6, testBool, 0) end
function TestGlobalTemplate.AddTestIntArrays(builder, testIntArrays) builder:PrependUOffsetTRelativeSlot(7, testIntArrays, 0) end
function TestGlobalTemplate.StartTestIntArraysVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTestFloatArrays(builder, testFloatArrays) builder:PrependUOffsetTRelativeSlot(8, testFloatArrays, 0) end
function TestGlobalTemplate.StartTestFloatArraysVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTestDoubleArrays(builder, testDoubleArrays) builder:PrependUOffsetTRelativeSlot(9, testDoubleArrays, 0) end
function TestGlobalTemplate.StartTestDoubleArraysVector(builder, numElems) return builder:StartVector(8, numElems, 8) end
function TestGlobalTemplate.AddTestBoolArrays(builder, testBoolArrays) builder:PrependUOffsetTRelativeSlot(10, testBoolArrays, 0) end
function TestGlobalTemplate.StartTestBoolArraysVector(builder, numElems) return builder:StartVector(1, numElems, 1) end
function TestGlobalTemplate.AddTestObj(builder, testObj) builder:PrependUOffsetTRelativeSlot(11, testObj, 0) end
function TestGlobalTemplate.AddTestObj1(builder, testObj1) builder:PrependUOffsetTRelativeSlot(12, testObj1, 0) end
function TestGlobalTemplate.AddTestObjArrays(builder, testObjArrays) builder:PrependUOffsetTRelativeSlot(13, testObjArrays, 0) end
function TestGlobalTemplate.StartTestObjArraysVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTestObjArray1s(builder, testObjArray1s) builder:PrependUOffsetTRelativeSlot(14, testObjArray1s, 0) end
function TestGlobalTemplate.StartTestObjArray1sVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTestDefineFromGlobal(builder, testDefineFromGlobal) builder:PrependUOffsetTRelativeSlot(15, testDefineFromGlobal, 0) end
function TestGlobalTemplate.AddTestDefineFromGlobal2s(builder, testDefineFromGlobal2s) builder:PrependUOffsetTRelativeSlot(16, testDefineFromGlobal2s, 0) end
function TestGlobalTemplate.StartTestDefineFromGlobal2sVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTestCustomObj(builder, testCustomObj) builder:PrependUOffsetTRelativeSlot(17, testCustomObj, 0) end
function TestGlobalTemplate.AddTestCustomObjArrays(builder, testCustomObjArrays) builder:PrependUOffsetTRelativeSlot(18, testCustomObjArrays, 0) end
function TestGlobalTemplate.StartTestCustomObjArraysVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestGlobalTemplate.AddTest1Int(builder, test1Int) builder:PrependInt32Slot(19, test1Int, 0) end
function TestGlobalTemplate.AddTestInt1(builder, testInt1) builder:PrependInt32Slot(20, testInt1, 0) end
function TestGlobalTemplate.End(builder) return builder:EndObject() end

return TestGlobalTemplate -- return the module