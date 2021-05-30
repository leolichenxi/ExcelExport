// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace Config
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct TestGlobalTemplate : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static TestGlobalTemplate GetRootAsTestGlobalTemplate(ByteBuffer _bb) { return GetRootAsTestGlobalTemplate(_bb, new TestGlobalTemplate()); }
  public static TestGlobalTemplate GetRootAsTestGlobalTemplate(ByteBuffer _bb, TestGlobalTemplate obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public TestGlobalTemplate __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int TestInt { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public string TestStringArrays(int j) { int o = __p.__offset(6); return o != 0 ? __p.__string(__p.__vector(o) + j * 4) : null; }
  public int TestStringArraysLength { get { int o = __p.__offset(6); return o != 0 ? __p.__vector_len(o) : 0; } }
  public double TestString1 { get { int o = __p.__offset(8); return o != 0 ? __p.bb.GetDouble(o + __p.bb_pos) : (double)0.0; } }
  public string TestString { get { int o = __p.__offset(10); return o != 0 ? __p.__string(o + __p.bb_pos) : null; } }
#if ENABLE_SPAN_T
  public Span<byte> GetTestStringBytes() { return __p.__vector_as_span<byte>(10, 1); }
#else
  public ArraySegment<byte>? GetTestStringBytes() { return __p.__vector_as_arraysegment(10); }
#endif
  public byte[] GetTestStringArray() { return __p.__vector_as_array<byte>(10); }
  public float TestFloat { get { int o = __p.__offset(12); return o != 0 ? __p.bb.GetFloat(o + __p.bb_pos) : (float)0.0f; } }
  public double TestDouble { get { int o = __p.__offset(14); return o != 0 ? __p.bb.GetDouble(o + __p.bb_pos) : (double)0.0; } }
  public bool TestBool { get { int o = __p.__offset(16); return o != 0 ? 0!=__p.bb.Get(o + __p.bb_pos) : (bool)false; } }
  public int TestIntArrays(int j) { int o = __p.__offset(18); return o != 0 ? __p.bb.GetInt(__p.__vector(o) + j * 4) : (int)0; }
  public int TestIntArraysLength { get { int o = __p.__offset(18); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<int> GetTestIntArraysBytes() { return __p.__vector_as_span<int>(18, 4); }
#else
  public ArraySegment<byte>? GetTestIntArraysBytes() { return __p.__vector_as_arraysegment(18); }
#endif
  public int[] GetTestIntArraysArray() { return __p.__vector_as_array<int>(18); }
  public float TestFloatArrays(int j) { int o = __p.__offset(20); return o != 0 ? __p.bb.GetFloat(__p.__vector(o) + j * 4) : (float)0; }
  public int TestFloatArraysLength { get { int o = __p.__offset(20); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<float> GetTestFloatArraysBytes() { return __p.__vector_as_span<float>(20, 4); }
#else
  public ArraySegment<byte>? GetTestFloatArraysBytes() { return __p.__vector_as_arraysegment(20); }
#endif
  public float[] GetTestFloatArraysArray() { return __p.__vector_as_array<float>(20); }
  public double TestDoubleArrays(int j) { int o = __p.__offset(22); return o != 0 ? __p.bb.GetDouble(__p.__vector(o) + j * 8) : (double)0; }
  public int TestDoubleArraysLength { get { int o = __p.__offset(22); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<double> GetTestDoubleArraysBytes() { return __p.__vector_as_span<double>(22, 8); }
#else
  public ArraySegment<byte>? GetTestDoubleArraysBytes() { return __p.__vector_as_arraysegment(22); }
#endif
  public double[] GetTestDoubleArraysArray() { return __p.__vector_as_array<double>(22); }
  public bool TestBoolArrays(int j) { int o = __p.__offset(24); return o != 0 ? 0!=__p.bb.Get(__p.__vector(o) + j * 1) : false; }
  public int TestBoolArraysLength { get { int o = __p.__offset(24); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<bool> GetTestBoolArraysBytes() { return __p.__vector_as_span<bool>(24, 1); }
#else
  public ArraySegment<byte>? GetTestBoolArraysBytes() { return __p.__vector_as_arraysegment(24); }
#endif
  public bool[] GetTestBoolArraysArray() { return __p.__vector_as_array<bool>(24); }
  public Config.TestObj_? TestObj { get { int o = __p.__offset(26); return o != 0 ? (Config.TestObj_?)(new Config.TestObj_()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }
  public Config.TestObj1_? TestObj1 { get { int o = __p.__offset(28); return o != 0 ? (Config.TestObj1_?)(new Config.TestObj1_()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }
  public Config.TestObjArray_? TestObjArrays(int j) { int o = __p.__offset(30); return o != 0 ? (Config.TestObjArray_?)(new Config.TestObjArray_()).__assign(__p.__indirect(__p.__vector(o) + j * 4), __p.bb) : null; }
  public int TestObjArraysLength { get { int o = __p.__offset(30); return o != 0 ? __p.__vector_len(o) : 0; } }
  public Config.TestObjArray1_? TestObjArray1s(int j) { int o = __p.__offset(32); return o != 0 ? (Config.TestObjArray1_?)(new Config.TestObjArray1_()).__assign(__p.__indirect(__p.__vector(o) + j * 4), __p.bb) : null; }
  public int TestObjArray1sLength { get { int o = __p.__offset(32); return o != 0 ? __p.__vector_len(o) : 0; } }
  public Position3d? TestDefineFromGlobal { get { int o = __p.__offset(34); return o != 0 ? (Position3d?)(new Position3d()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }
  public Position3d? TestDefineFromGlobal2s(int j) { int o = __p.__offset(36); return o != 0 ? (Position3d?)(new Position3d()).__assign(__p.__indirect(__p.__vector(o) + j * 4), __p.bb) : null; }
  public int TestDefineFromGlobal2sLength { get { int o = __p.__offset(36); return o != 0 ? __p.__vector_len(o) : 0; } }
  public PositionArray3d? TestCustomObj { get { int o = __p.__offset(38); return o != 0 ? (PositionArray3d?)(new PositionArray3d()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }
  public PositionArray3d? TestCustomObjArrays(int j) { int o = __p.__offset(40); return o != 0 ? (PositionArray3d?)(new PositionArray3d()).__assign(__p.__indirect(__p.__vector(o) + j * 4), __p.bb) : null; }
  public int TestCustomObjArraysLength { get { int o = __p.__offset(40); return o != 0 ? __p.__vector_len(o) : 0; } }

  public static Offset<Config.TestGlobalTemplate> CreateTestGlobalTemplate(FlatBufferBuilder builder,
      int test_int = 0,
      VectorOffset test_string_arraysOffset = default(VectorOffset),
      double test_string1 = 0.0,
      StringOffset test_stringOffset = default(StringOffset),
      float test_float = 0.0f,
      double test_double = 0.0,
      bool test_bool = false,
      VectorOffset test_int_arraysOffset = default(VectorOffset),
      VectorOffset test_float_arraysOffset = default(VectorOffset),
      VectorOffset test_double_arraysOffset = default(VectorOffset),
      VectorOffset test_bool_arraysOffset = default(VectorOffset),
      Offset<Config.TestObj_> test_objOffset = default(Offset<Config.TestObj_>),
      Offset<Config.TestObj1_> test_obj1Offset = default(Offset<Config.TestObj1_>),
      VectorOffset test_obj_arraysOffset = default(VectorOffset),
      VectorOffset test_obj_array1sOffset = default(VectorOffset),
      Offset<Position3d> test_define_from_globalOffset = default(Offset<Position3d>),
      VectorOffset test_define_from_global2sOffset = default(VectorOffset),
      Offset<PositionArray3d> test_custom_objOffset = default(Offset<PositionArray3d>),
      VectorOffset test_custom_obj_arraysOffset = default(VectorOffset)) {
    builder.StartTable(19);
    TestGlobalTemplate.AddTestDouble(builder, test_double);
    TestGlobalTemplate.AddTestString1(builder, test_string1);
    TestGlobalTemplate.AddTestCustomObjArrays(builder, test_custom_obj_arraysOffset);
    TestGlobalTemplate.AddTestCustomObj(builder, test_custom_objOffset);
    TestGlobalTemplate.AddTestDefineFromGlobal2s(builder, test_define_from_global2sOffset);
    TestGlobalTemplate.AddTestDefineFromGlobal(builder, test_define_from_globalOffset);
    TestGlobalTemplate.AddTestObjArray1s(builder, test_obj_array1sOffset);
    TestGlobalTemplate.AddTestObjArrays(builder, test_obj_arraysOffset);
    TestGlobalTemplate.AddTestObj1(builder, test_obj1Offset);
    TestGlobalTemplate.AddTestObj(builder, test_objOffset);
    TestGlobalTemplate.AddTestBoolArrays(builder, test_bool_arraysOffset);
    TestGlobalTemplate.AddTestDoubleArrays(builder, test_double_arraysOffset);
    TestGlobalTemplate.AddTestFloatArrays(builder, test_float_arraysOffset);
    TestGlobalTemplate.AddTestIntArrays(builder, test_int_arraysOffset);
    TestGlobalTemplate.AddTestFloat(builder, test_float);
    TestGlobalTemplate.AddTestString(builder, test_stringOffset);
    TestGlobalTemplate.AddTestStringArrays(builder, test_string_arraysOffset);
    TestGlobalTemplate.AddTestInt(builder, test_int);
    TestGlobalTemplate.AddTestBool(builder, test_bool);
    return TestGlobalTemplate.EndTestGlobalTemplate(builder);
  }

  public static void StartTestGlobalTemplate(FlatBufferBuilder builder) { builder.StartTable(19); }
  public static void AddTestInt(FlatBufferBuilder builder, int testInt) { builder.AddInt(0, testInt, 0); }
  public static void AddTestStringArrays(FlatBufferBuilder builder, VectorOffset testStringArraysOffset) { builder.AddOffset(1, testStringArraysOffset.Value, 0); }
  public static VectorOffset CreateTestStringArraysVector(FlatBufferBuilder builder, StringOffset[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateTestStringArraysVectorBlock(FlatBufferBuilder builder, StringOffset[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestStringArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTestString1(FlatBufferBuilder builder, double testString1) { builder.AddDouble(2, testString1, 0.0); }
  public static void AddTestString(FlatBufferBuilder builder, StringOffset testStringOffset) { builder.AddOffset(3, testStringOffset.Value, 0); }
  public static void AddTestFloat(FlatBufferBuilder builder, float testFloat) { builder.AddFloat(4, testFloat, 0.0f); }
  public static void AddTestDouble(FlatBufferBuilder builder, double testDouble) { builder.AddDouble(5, testDouble, 0.0); }
  public static void AddTestBool(FlatBufferBuilder builder, bool testBool) { builder.AddBool(6, testBool, false); }
  public static void AddTestIntArrays(FlatBufferBuilder builder, VectorOffset testIntArraysOffset) { builder.AddOffset(7, testIntArraysOffset.Value, 0); }
  public static VectorOffset CreateTestIntArraysVector(FlatBufferBuilder builder, int[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddInt(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateTestIntArraysVectorBlock(FlatBufferBuilder builder, int[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestIntArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTestFloatArrays(FlatBufferBuilder builder, VectorOffset testFloatArraysOffset) { builder.AddOffset(8, testFloatArraysOffset.Value, 0); }
  public static VectorOffset CreateTestFloatArraysVector(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddFloat(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateTestFloatArraysVectorBlock(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestFloatArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTestDoubleArrays(FlatBufferBuilder builder, VectorOffset testDoubleArraysOffset) { builder.AddOffset(9, testDoubleArraysOffset.Value, 0); }
  public static VectorOffset CreateTestDoubleArraysVector(FlatBufferBuilder builder, double[] data) { builder.StartVector(8, data.Length, 8); for (int i = data.Length - 1; i >= 0; i--) builder.AddDouble(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateTestDoubleArraysVectorBlock(FlatBufferBuilder builder, double[] data) { builder.StartVector(8, data.Length, 8); builder.Add(data); return builder.EndVector(); }
  public static void StartTestDoubleArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(8, numElems, 8); }
  public static void AddTestBoolArrays(FlatBufferBuilder builder, VectorOffset testBoolArraysOffset) { builder.AddOffset(10, testBoolArraysOffset.Value, 0); }
  public static VectorOffset CreateTestBoolArraysVector(FlatBufferBuilder builder, bool[] data) { builder.StartVector(1, data.Length, 1); for (int i = data.Length - 1; i >= 0; i--) builder.AddBool(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateTestBoolArraysVectorBlock(FlatBufferBuilder builder, bool[] data) { builder.StartVector(1, data.Length, 1); builder.Add(data); return builder.EndVector(); }
  public static void StartTestBoolArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(1, numElems, 1); }
  public static void AddTestObj(FlatBufferBuilder builder, Offset<Config.TestObj_> testObjOffset) { builder.AddOffset(11, testObjOffset.Value, 0); }
  public static void AddTestObj1(FlatBufferBuilder builder, Offset<Config.TestObj1_> testObj1Offset) { builder.AddOffset(12, testObj1Offset.Value, 0); }
  public static void AddTestObjArrays(FlatBufferBuilder builder, VectorOffset testObjArraysOffset) { builder.AddOffset(13, testObjArraysOffset.Value, 0); }
  public static VectorOffset CreateTestObjArraysVector(FlatBufferBuilder builder, Offset<Config.TestObjArray_>[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateTestObjArraysVectorBlock(FlatBufferBuilder builder, Offset<Config.TestObjArray_>[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestObjArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTestObjArray1s(FlatBufferBuilder builder, VectorOffset testObjArray1sOffset) { builder.AddOffset(14, testObjArray1sOffset.Value, 0); }
  public static VectorOffset CreateTestObjArray1sVector(FlatBufferBuilder builder, Offset<Config.TestObjArray1_>[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateTestObjArray1sVectorBlock(FlatBufferBuilder builder, Offset<Config.TestObjArray1_>[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestObjArray1sVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTestDefineFromGlobal(FlatBufferBuilder builder, Offset<Position3d> testDefineFromGlobalOffset) { builder.AddOffset(15, testDefineFromGlobalOffset.Value, 0); }
  public static void AddTestDefineFromGlobal2s(FlatBufferBuilder builder, VectorOffset testDefineFromGlobal2sOffset) { builder.AddOffset(16, testDefineFromGlobal2sOffset.Value, 0); }
  public static VectorOffset CreateTestDefineFromGlobal2sVector(FlatBufferBuilder builder, Offset<Position3d>[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateTestDefineFromGlobal2sVectorBlock(FlatBufferBuilder builder, Offset<Position3d>[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestDefineFromGlobal2sVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTestCustomObj(FlatBufferBuilder builder, Offset<PositionArray3d> testCustomObjOffset) { builder.AddOffset(17, testCustomObjOffset.Value, 0); }
  public static void AddTestCustomObjArrays(FlatBufferBuilder builder, VectorOffset testCustomObjArraysOffset) { builder.AddOffset(18, testCustomObjArraysOffset.Value, 0); }
  public static VectorOffset CreateTestCustomObjArraysVector(FlatBufferBuilder builder, Offset<PositionArray3d>[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateTestCustomObjArraysVectorBlock(FlatBufferBuilder builder, Offset<PositionArray3d>[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartTestCustomObjArraysVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static Offset<Config.TestGlobalTemplate> EndTestGlobalTemplate(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<Config.TestGlobalTemplate>(o);
  }
  public static void FinishTestGlobalTemplateBuffer(FlatBufferBuilder builder, Offset<Config.TestGlobalTemplate> offset) { builder.Finish(offset.Value); }
  public static void FinishSizePrefixedTestGlobalTemplateBuffer(FlatBufferBuilder builder, Offset<Config.TestGlobalTemplate> offset) { builder.FinishSizePrefixed(offset.Value); }
};


}
