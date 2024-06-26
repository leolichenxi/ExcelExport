// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: protos/PositionArray3d.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
/// <summary>Holder for reflection information generated from protos/PositionArray3d.proto</summary>
public static partial class PositionArray3DReflection {

  #region Descriptor
  /// <summary>File descriptor for protos/PositionArray3d.proto</summary>
  public static pbr::FileDescriptor Descriptor {
    get { return descriptor; }
  }
  private static pbr::FileDescriptor descriptor;

  static PositionArray3DReflection() {
    byte[] descriptorData = global::System.Convert.FromBase64String(
        string.Concat(
          "Chxwcm90b3MvUG9zaXRpb25BcnJheTNkLnByb3RvIjUKD1Bvc2l0aW9uQXJy",
          "YXkzZBIKCgJ4cxgBIAMoAhIKCgJ5cxgCIAMoAhIKCgJ6cxgDIAMoAmIGcHJv",
          "dG8z"));
    descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
        new pbr::FileDescriptor[] { },
        new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
          new pbr::GeneratedClrTypeInfo(typeof(global::PositionArray3d), global::PositionArray3d.Parser, new[]{ "Xs", "Ys", "Zs" }, null, null, null, null)
        }));
  }
  #endregion

}
#region Messages
[global::System.Diagnostics.DebuggerDisplayAttribute("{ToString(),nq}")]
public sealed partial class PositionArray3d : pb::IMessage<PositionArray3d>
#if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    , pb::IBufferMessage
#endif
{
  private static readonly pb::MessageParser<PositionArray3d> _parser = new pb::MessageParser<PositionArray3d>(() => new PositionArray3d());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public static pb::MessageParser<PositionArray3d> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::PositionArray3DReflection.Descriptor.MessageTypes[0]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public PositionArray3d() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public PositionArray3d(PositionArray3d other) : this() {
    xs_ = other.xs_.Clone();
    ys_ = other.ys_.Clone();
    zs_ = other.zs_.Clone();
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public PositionArray3d Clone() {
    return new PositionArray3d(this);
  }

  /// <summary>Field number for the "xs" field.</summary>
  public const int XsFieldNumber = 1;
  private static readonly pb::FieldCodec<float> _repeated_xs_codec
      = pb::FieldCodec.ForFloat(10);
  private readonly pbc::RepeatedField<float> xs_ = new pbc::RepeatedField<float>();
  /// <summary>
  /// x
  /// </summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public pbc::RepeatedField<float> Xs {
    get { return xs_; }
  }

  /// <summary>Field number for the "ys" field.</summary>
  public const int YsFieldNumber = 2;
  private static readonly pb::FieldCodec<float> _repeated_ys_codec
      = pb::FieldCodec.ForFloat(18);
  private readonly pbc::RepeatedField<float> ys_ = new pbc::RepeatedField<float>();
  /// <summary>
  /// y
  /// </summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public pbc::RepeatedField<float> Ys {
    get { return ys_; }
  }

  /// <summary>Field number for the "zs" field.</summary>
  public const int ZsFieldNumber = 3;
  private static readonly pb::FieldCodec<float> _repeated_zs_codec
      = pb::FieldCodec.ForFloat(26);
  private readonly pbc::RepeatedField<float> zs_ = new pbc::RepeatedField<float>();
  /// <summary>
  /// z
  /// </summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public pbc::RepeatedField<float> Zs {
    get { return zs_; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override bool Equals(object other) {
    return Equals(other as PositionArray3d);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public bool Equals(PositionArray3d other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if(!xs_.Equals(other.xs_)) return false;
    if(!ys_.Equals(other.ys_)) return false;
    if(!zs_.Equals(other.zs_)) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override int GetHashCode() {
    int hash = 1;
    hash ^= xs_.GetHashCode();
    hash ^= ys_.GetHashCode();
    hash ^= zs_.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void WriteTo(pb::CodedOutputStream output) {
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    output.WriteRawMessage(this);
  #else
    xs_.WriteTo(output, _repeated_xs_codec);
    ys_.WriteTo(output, _repeated_ys_codec);
    zs_.WriteTo(output, _repeated_zs_codec);
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  #endif
  }

  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
    xs_.WriteTo(ref output, _repeated_xs_codec);
    ys_.WriteTo(ref output, _repeated_ys_codec);
    zs_.WriteTo(ref output, _repeated_zs_codec);
    if (_unknownFields != null) {
      _unknownFields.WriteTo(ref output);
    }
  }
  #endif

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public int CalculateSize() {
    int size = 0;
    size += xs_.CalculateSize(_repeated_xs_codec);
    size += ys_.CalculateSize(_repeated_ys_codec);
    size += zs_.CalculateSize(_repeated_zs_codec);
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void MergeFrom(PositionArray3d other) {
    if (other == null) {
      return;
    }
    xs_.Add(other.xs_);
    ys_.Add(other.ys_);
    zs_.Add(other.zs_);
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void MergeFrom(pb::CodedInputStream input) {
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    input.ReadRawMessage(this);
  #else
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 10:
        case 13: {
          xs_.AddEntriesFrom(input, _repeated_xs_codec);
          break;
        }
        case 18:
        case 21: {
          ys_.AddEntriesFrom(input, _repeated_ys_codec);
          break;
        }
        case 26:
        case 29: {
          zs_.AddEntriesFrom(input, _repeated_zs_codec);
          break;
        }
      }
    }
  #endif
  }

  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
          break;
        case 10:
        case 13: {
          xs_.AddEntriesFrom(ref input, _repeated_xs_codec);
          break;
        }
        case 18:
        case 21: {
          ys_.AddEntriesFrom(ref input, _repeated_ys_codec);
          break;
        }
        case 26:
        case 29: {
          zs_.AddEntriesFrom(ref input, _repeated_zs_codec);
          break;
        }
      }
    }
  }
  #endif

}

#endregion


#endregion Designer generated code
