// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: protos/TestTableArraysTemplate.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Config {

  /// <summary>Holder for reflection information generated from protos/TestTableArraysTemplate.proto</summary>
  public static partial class TestTableArraysTemplateReflection {

    #region Descriptor
    /// <summary>File descriptor for protos/TestTableArraysTemplate.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static TestTableArraysTemplateReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiRwcm90b3MvVGVzdFRhYmxlQXJyYXlzVGVtcGxhdGUucHJvdG8SBkNvbmZp",
            "ZyJ5ChdUZXN0VGFibGVBcnJheXNUZW1wbGF0ZRIKCgJJZBgBIAEoBRIPCgdX",
            "ZWFwb25zGAIgAygFEg0KBU1vZGVsGAMgASgJEgwKBEljb24YBCABKAkSEwoL",
            "TWFjaGluZVR5cGUYBSABKAkSDwoHTWFwVHlwZRgGIAEoCSJXChtUZXN0VGFi",
            "bGVBcnJheXNUZW1wbGF0ZUxpc3QSOAoPVGVzdFRhYmxlQXJyYXlzGAEgAygL",
            "Mh8uQ29uZmlnLlRlc3RUYWJsZUFycmF5c1RlbXBsYXRlYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Config.TestTableArraysTemplate), global::Config.TestTableArraysTemplate.Parser, new[]{ "Id", "Weapons", "Model", "Icon", "MachineType", "MapType" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Config.TestTableArraysTemplateList), global::Config.TestTableArraysTemplateList.Parser, new[]{ "TestTableArrays" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class TestTableArraysTemplate : pb::IMessage<TestTableArraysTemplate>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<TestTableArraysTemplate> _parser = new pb::MessageParser<TestTableArraysTemplate>(() => new TestTableArraysTemplate());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<TestTableArraysTemplate> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Config.TestTableArraysTemplateReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TestTableArraysTemplate() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TestTableArraysTemplate(TestTableArraysTemplate other) : this() {
      id_ = other.id_;
      weapons_ = other.weapons_.Clone();
      model_ = other.model_;
      icon_ = other.icon_;
      machineType_ = other.machineType_;
      mapType_ = other.mapType_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TestTableArraysTemplate Clone() {
      return new TestTableArraysTemplate(this);
    }

    /// <summary>Field number for the "Id" field.</summary>
    public const int IdFieldNumber = 1;
    private int id_;
    /// <summary>
    /// 英雄ID
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "Weapons" field.</summary>
    public const int WeaponsFieldNumber = 2;
    private static readonly pb::FieldCodec<int> _repeated_weapons_codec
        = pb::FieldCodec.ForInt32(18);
    private readonly pbc::RepeatedField<int> weapons_ = new pbc::RepeatedField<int>();
    /// <summary>
    /// 武器(武器Id)
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<int> Weapons {
      get { return weapons_; }
    }

    /// <summary>Field number for the "Model" field.</summary>
    public const int ModelFieldNumber = 3;
    private string model_ = "";
    /// <summary>
    /// 切片
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Model {
      get { return model_; }
      set {
        model_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "Icon" field.</summary>
    public const int IconFieldNumber = 4;
    private string icon_ = "";
    /// <summary>
    /// Icon
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Icon {
      get { return icon_; }
      set {
        icon_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "MachineType" field.</summary>
    public const int MachineTypeFieldNumber = 5;
    private string machineType_ = "";
    /// <summary>
    /// 机体类型
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string MachineType {
      get { return machineType_; }
      set {
        machineType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "MapType" field.</summary>
    public const int MapTypeFieldNumber = 6;
    private string mapType_ = "";
    /// <summary>
    /// 地形适应
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string MapType {
      get { return mapType_; }
      set {
        mapType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as TestTableArraysTemplate);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(TestTableArraysTemplate other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if(!weapons_.Equals(other.weapons_)) return false;
      if (Model != other.Model) return false;
      if (Icon != other.Icon) return false;
      if (MachineType != other.MachineType) return false;
      if (MapType != other.MapType) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      hash ^= weapons_.GetHashCode();
      if (Model.Length != 0) hash ^= Model.GetHashCode();
      if (Icon.Length != 0) hash ^= Icon.GetHashCode();
      if (MachineType.Length != 0) hash ^= MachineType.GetHashCode();
      if (MapType.Length != 0) hash ^= MapType.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Id != 0) {
        output.WriteRawTag(8);
        output.WriteInt32(Id);
      }
      weapons_.WriteTo(output, _repeated_weapons_codec);
      if (Model.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Model);
      }
      if (Icon.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Icon);
      }
      if (MachineType.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(MachineType);
      }
      if (MapType.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(MapType);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Id != 0) {
        output.WriteRawTag(8);
        output.WriteInt32(Id);
      }
      weapons_.WriteTo(ref output, _repeated_weapons_codec);
      if (Model.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Model);
      }
      if (Icon.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Icon);
      }
      if (MachineType.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(MachineType);
      }
      if (MapType.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(MapType);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Id != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(Id);
      }
      size += weapons_.CalculateSize(_repeated_weapons_codec);
      if (Model.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Model);
      }
      if (Icon.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Icon);
      }
      if (MachineType.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(MachineType);
      }
      if (MapType.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(MapType);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(TestTableArraysTemplate other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      weapons_.Add(other.weapons_);
      if (other.Model.Length != 0) {
        Model = other.Model;
      }
      if (other.Icon.Length != 0) {
        Icon = other.Icon;
      }
      if (other.MachineType.Length != 0) {
        MachineType = other.MachineType;
      }
      if (other.MapType.Length != 0) {
        MapType = other.MapType;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
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
          case 8: {
            Id = input.ReadInt32();
            break;
          }
          case 18:
          case 16: {
            weapons_.AddEntriesFrom(input, _repeated_weapons_codec);
            break;
          }
          case 26: {
            Model = input.ReadString();
            break;
          }
          case 34: {
            Icon = input.ReadString();
            break;
          }
          case 42: {
            MachineType = input.ReadString();
            break;
          }
          case 50: {
            MapType = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 8: {
            Id = input.ReadInt32();
            break;
          }
          case 18:
          case 16: {
            weapons_.AddEntriesFrom(ref input, _repeated_weapons_codec);
            break;
          }
          case 26: {
            Model = input.ReadString();
            break;
          }
          case 34: {
            Icon = input.ReadString();
            break;
          }
          case 42: {
            MachineType = input.ReadString();
            break;
          }
          case 50: {
            MapType = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class TestTableArraysTemplateList : pb::IMessage<TestTableArraysTemplateList>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<TestTableArraysTemplateList> _parser = new pb::MessageParser<TestTableArraysTemplateList>(() => new TestTableArraysTemplateList());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<TestTableArraysTemplateList> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Config.TestTableArraysTemplateReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TestTableArraysTemplateList() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TestTableArraysTemplateList(TestTableArraysTemplateList other) : this() {
      testTableArrays_ = other.testTableArrays_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TestTableArraysTemplateList Clone() {
      return new TestTableArraysTemplateList(this);
    }

    /// <summary>Field number for the "TestTableArrays" field.</summary>
    public const int TestTableArraysFieldNumber = 1;
    private static readonly pb::FieldCodec<global::Config.TestTableArraysTemplate> _repeated_testTableArrays_codec
        = pb::FieldCodec.ForMessage(10, global::Config.TestTableArraysTemplate.Parser);
    private readonly pbc::RepeatedField<global::Config.TestTableArraysTemplate> testTableArrays_ = new pbc::RepeatedField<global::Config.TestTableArraysTemplate>();
    /// <summary>
    /// List
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::Config.TestTableArraysTemplate> TestTableArrays {
      get { return testTableArrays_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as TestTableArraysTemplateList);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(TestTableArraysTemplateList other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!testTableArrays_.Equals(other.testTableArrays_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= testTableArrays_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      testTableArrays_.WriteTo(output, _repeated_testTableArrays_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      testTableArrays_.WriteTo(ref output, _repeated_testTableArrays_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      size += testTableArrays_.CalculateSize(_repeated_testTableArrays_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(TestTableArraysTemplateList other) {
      if (other == null) {
        return;
      }
      testTableArrays_.Add(other.testTableArrays_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
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
          case 10: {
            testTableArrays_.AddEntriesFrom(input, _repeated_testTableArrays_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            testTableArrays_.AddEntriesFrom(ref input, _repeated_testTableArrays_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
