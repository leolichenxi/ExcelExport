// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace Config
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct Test_Global2Template : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static Test_Global2Template GetRootAsTest_Global2Template(ByteBuffer _bb) { return GetRootAsTest_Global2Template(_bb, new Test_Global2Template()); }
  public static Test_Global2Template GetRootAsTest_Global2Template(ByteBuffer _bb, Test_Global2Template obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public Test_Global2Template __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public float TestFloat { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetFloat(o + __p.bb_pos) : (float)0.0f; } }

  public static Offset<Config.Test_Global2Template> CreateTest_Global2Template(FlatBufferBuilder builder,
      float test_float = 0.0f) {
    builder.StartTable(1);
    Test_Global2Template.AddTestFloat(builder, test_float);
    return Test_Global2Template.EndTest_Global2Template(builder);
  }

  public static void StartTest_Global2Template(FlatBufferBuilder builder) { builder.StartTable(1); }
  public static void AddTestFloat(FlatBufferBuilder builder, float testFloat) { builder.AddFloat(0, testFloat, 0.0f); }
  public static Offset<Config.Test_Global2Template> EndTest_Global2Template(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<Config.Test_Global2Template>(o);
  }
  public static void FinishTest_Global2TemplateBuffer(FlatBufferBuilder builder, Offset<Config.Test_Global2Template> offset) { builder.Finish(offset.Value); }
  public static void FinishSizePrefixedTest_Global2TemplateBuffer(FlatBufferBuilder builder, Offset<Config.Test_Global2Template> offset) { builder.FinishSizePrefixed(offset.Value); }
};


}