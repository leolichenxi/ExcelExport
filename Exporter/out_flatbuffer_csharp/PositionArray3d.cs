// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct PositionArray3d : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static PositionArray3d GetRootAsPositionArray3d(ByteBuffer _bb) { return GetRootAsPositionArray3d(_bb, new PositionArray3d()); }
  public static PositionArray3d GetRootAsPositionArray3d(ByteBuffer _bb, PositionArray3d obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public PositionArray3d __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public float Xs(int j) { int o = __p.__offset(4); return o != 0 ? __p.bb.GetFloat(__p.__vector(o) + j * 4) : (float)0; }
  public int XsLength { get { int o = __p.__offset(4); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<float> GetXsBytes() { return __p.__vector_as_span<float>(4, 4); }
#else
  public ArraySegment<byte>? GetXsBytes() { return __p.__vector_as_arraysegment(4); }
#endif
  public float[] GetXsArray() { return __p.__vector_as_array<float>(4); }
  public float Ys(int j) { int o = __p.__offset(6); return o != 0 ? __p.bb.GetFloat(__p.__vector(o) + j * 4) : (float)0; }
  public int YsLength { get { int o = __p.__offset(6); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<float> GetYsBytes() { return __p.__vector_as_span<float>(6, 4); }
#else
  public ArraySegment<byte>? GetYsBytes() { return __p.__vector_as_arraysegment(6); }
#endif
  public float[] GetYsArray() { return __p.__vector_as_array<float>(6); }
  public float Zs(int j) { int o = __p.__offset(8); return o != 0 ? __p.bb.GetFloat(__p.__vector(o) + j * 4) : (float)0; }
  public int ZsLength { get { int o = __p.__offset(8); return o != 0 ? __p.__vector_len(o) : 0; } }
#if ENABLE_SPAN_T
  public Span<float> GetZsBytes() { return __p.__vector_as_span<float>(8, 4); }
#else
  public ArraySegment<byte>? GetZsBytes() { return __p.__vector_as_arraysegment(8); }
#endif
  public float[] GetZsArray() { return __p.__vector_as_array<float>(8); }

  public static Offset<PositionArray3d> CreatePositionArray3d(FlatBufferBuilder builder,
      VectorOffset xsOffset = default(VectorOffset),
      VectorOffset ysOffset = default(VectorOffset),
      VectorOffset zsOffset = default(VectorOffset)) {
    builder.StartTable(3);
    PositionArray3d.AddZs(builder, zsOffset);
    PositionArray3d.AddYs(builder, ysOffset);
    PositionArray3d.AddXs(builder, xsOffset);
    return PositionArray3d.EndPositionArray3d(builder);
  }

  public static void StartPositionArray3d(FlatBufferBuilder builder) { builder.StartTable(3); }
  public static void AddXs(FlatBufferBuilder builder, VectorOffset xsOffset) { builder.AddOffset(0, xsOffset.Value, 0); }
  public static VectorOffset CreateXsVector(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddFloat(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateXsVectorBlock(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartXsVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddYs(FlatBufferBuilder builder, VectorOffset ysOffset) { builder.AddOffset(1, ysOffset.Value, 0); }
  public static VectorOffset CreateYsVector(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddFloat(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateYsVectorBlock(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartYsVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddZs(FlatBufferBuilder builder, VectorOffset zsOffset) { builder.AddOffset(2, zsOffset.Value, 0); }
  public static VectorOffset CreateZsVector(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddFloat(data[i]); return builder.EndVector(); }
  public static VectorOffset CreateZsVectorBlock(FlatBufferBuilder builder, float[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartZsVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static Offset<PositionArray3d> EndPositionArray3d(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<PositionArray3d>(o);
  }
  public static void FinishPositionArray3dBuffer(FlatBufferBuilder builder, Offset<PositionArray3d> offset) { builder.Finish(offset.Value); }
  public static void FinishSizePrefixedPositionArray3dBuffer(FlatBufferBuilder builder, Offset<PositionArray3d> offset) { builder.FinishSizePrefixed(offset.Value); }
};

