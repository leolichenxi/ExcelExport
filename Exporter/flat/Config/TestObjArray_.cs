// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace Config
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct TestObjArray_ : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static TestObjArray_ GetRootAsTestObjArray_(ByteBuffer _bb) { return GetRootAsTestObjArray_(_bb, new TestObjArray_()); }
  public static TestObjArray_ GetRootAsTestObjArray_(ByteBuffer _bb, TestObjArray_ obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public TestObjArray_ __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int A { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public int B { get { int o = __p.__offset(6); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public int C { get { int o = __p.__offset(8); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }

  public static Offset<Config.TestObjArray_> CreateTestObjArray_(FlatBufferBuilder builder,
      int a = 0,
      int b = 0,
      int c = 0) {
    builder.StartTable(3);
    TestObjArray_.AddC(builder, c);
    TestObjArray_.AddB(builder, b);
    TestObjArray_.AddA(builder, a);
    return TestObjArray_.EndTestObjArray_(builder);
  }

  public static void StartTestObjArray_(FlatBufferBuilder builder) { builder.StartTable(3); }
  public static void AddA(FlatBufferBuilder builder, int a) { builder.AddInt(0, a, 0); }
  public static void AddB(FlatBufferBuilder builder, int b) { builder.AddInt(1, b, 0); }
  public static void AddC(FlatBufferBuilder builder, int c) { builder.AddInt(2, c, 0); }
  public static Offset<Config.TestObjArray_> EndTestObjArray_(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<Config.TestObjArray_>(o);
  }
};


}
