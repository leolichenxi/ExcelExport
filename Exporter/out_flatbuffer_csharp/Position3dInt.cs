// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct Position3dInt : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static Position3dInt GetRootAsPosition3dInt(ByteBuffer _bb) { return GetRootAsPosition3dInt(_bb, new Position3dInt()); }
  public static Position3dInt GetRootAsPosition3dInt(ByteBuffer _bb, Position3dInt obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public Position3dInt __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int X { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public int Y { get { int o = __p.__offset(6); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public int Z { get { int o = __p.__offset(8); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }

  public static Offset<Position3dInt> CreatePosition3dInt(FlatBufferBuilder builder,
      int x = 0,
      int y = 0,
      int z = 0) {
    builder.StartTable(3);
    Position3dInt.AddZ(builder, z);
    Position3dInt.AddY(builder, y);
    Position3dInt.AddX(builder, x);
    return Position3dInt.EndPosition3dInt(builder);
  }

  public static void StartPosition3dInt(FlatBufferBuilder builder) { builder.StartTable(3); }
  public static void AddX(FlatBufferBuilder builder, int x) { builder.AddInt(0, x, 0); }
  public static void AddY(FlatBufferBuilder builder, int y) { builder.AddInt(1, y, 0); }
  public static void AddZ(FlatBufferBuilder builder, int z) { builder.AddInt(2, z, 0); }
  public static Offset<Position3dInt> EndPosition3dInt(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<Position3dInt>(o);
  }
  public static void FinishPosition3dIntBuffer(FlatBufferBuilder builder, Offset<Position3dInt> offset) { builder.Finish(offset.Value); }
  public static void FinishSizePrefixedPosition3dIntBuffer(FlatBufferBuilder builder, Offset<Position3dInt> offset) { builder.FinishSizePrefixed(offset.Value); }
};
