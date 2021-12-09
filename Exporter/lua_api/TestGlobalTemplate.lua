---@class TestGlobalTemplate 
---@field  TestInt int32 @测试int类型 
---@field  TestStringArrays string[] @测试string[]类型 
---@field  TestString1 double @测试string数字类型 
---@field  TestString string @测试string类型 
---@field  TestFloat float @测试float类型 
---@field  TestDouble double @测试double类型 
---@field  TestBool bool @测试bool类型 
---@field  TestIntArrays int32[] @测试int数组 
---@field  TestFloatArrays float[] @测试float数组 
---@field  TestDoubleArrays double[] @测试double数组 
---@field  TestBoolArrays bool[] @测试bool数组 
---@field  TestObj TestObj_ @测试普通自定义对象 
---@field  TestObj1 TestObj1_ @测试普通自定义内部含有数组对象, 
---@field  TestObjArrays TestObjArray_[] @测试普通自定义对象数组 
---@field  TestObjArray1s TestObjArray1_[] @测试普通自定义内部含有数组对象数组 
---@field  TestDefineFromGlobal Position3d @测试全局对象声明 
---@field  TestDefineFromGlobal2s Position3d[] @测试全局对象声明数组 
---@field  TestCustomObj PositionArray3d @测试全局配置数组字段 
---@field  TestCustomObjArrays PositionArray3d[] @测试全局配置含有数组字段的数组 
---@field  Test1Int int32 @测试int类型 可以 但不建议字段命名含有数字 
---@field  TestInt1 int32 @测试int类型 可以 但不建议字段命名含有数字 