// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: protos/Position3d.proto

#include "protos/Position3d.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
class Position3dDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<Position3d> _instance;
} _Position3d_default_instance_;
static void InitDefaultsscc_info_Position3d_protos_2fPosition3d_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::_Position3d_default_instance_;
    new (ptr) ::Position3d();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_Position3d_protos_2fPosition3d_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_Position3d_protos_2fPosition3d_2eproto}, {}};

static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_protos_2fPosition3d_2eproto[1];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_protos_2fPosition3d_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_protos_2fPosition3d_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_protos_2fPosition3d_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::Position3d, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::Position3d, x_),
  PROTOBUF_FIELD_OFFSET(::Position3d, y_),
  PROTOBUF_FIELD_OFFSET(::Position3d, z_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::Position3d)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::_Position3d_default_instance_),
};

const char descriptor_table_protodef_protos_2fPosition3d_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\027protos/Position3d.proto\"-\n\nPosition3d\022"
  "\t\n\001x\030\001 \001(\002\022\t\n\001y\030\002 \001(\002\022\t\n\001z\030\003 \001(\002b\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_protos_2fPosition3d_2eproto_deps[1] = {
};
static ::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase*const descriptor_table_protos_2fPosition3d_2eproto_sccs[1] = {
  &scc_info_Position3d_protos_2fPosition3d_2eproto.base,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_protos_2fPosition3d_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_protos_2fPosition3d_2eproto = {
  false, false, descriptor_table_protodef_protos_2fPosition3d_2eproto, "protos/Position3d.proto", 80,
  &descriptor_table_protos_2fPosition3d_2eproto_once, descriptor_table_protos_2fPosition3d_2eproto_sccs, descriptor_table_protos_2fPosition3d_2eproto_deps, 1, 0,
  schemas, file_default_instances, TableStruct_protos_2fPosition3d_2eproto::offsets,
  file_level_metadata_protos_2fPosition3d_2eproto, 1, file_level_enum_descriptors_protos_2fPosition3d_2eproto, file_level_service_descriptors_protos_2fPosition3d_2eproto,
};

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_protos_2fPosition3d_2eproto = (static_cast<void>(::PROTOBUF_NAMESPACE_ID::internal::AddDescriptors(&descriptor_table_protos_2fPosition3d_2eproto)), true);

// ===================================================================

class Position3d::_Internal {
 public:
};

Position3d::Position3d(::PROTOBUF_NAMESPACE_ID::Arena* arena)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena) {
  SharedCtor();
  RegisterArenaDtor(arena);
  // @@protoc_insertion_point(arena_constructor:Position3d)
}
Position3d::Position3d(const Position3d& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  ::memcpy(&x_, &from.x_,
    static_cast<size_t>(reinterpret_cast<char*>(&z_) -
    reinterpret_cast<char*>(&x_)) + sizeof(z_));
  // @@protoc_insertion_point(copy_constructor:Position3d)
}

void Position3d::SharedCtor() {
  ::memset(reinterpret_cast<char*>(this) + static_cast<size_t>(
      reinterpret_cast<char*>(&x_) - reinterpret_cast<char*>(this)),
      0, static_cast<size_t>(reinterpret_cast<char*>(&z_) -
      reinterpret_cast<char*>(&x_)) + sizeof(z_));
}

Position3d::~Position3d() {
  // @@protoc_insertion_point(destructor:Position3d)
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

void Position3d::SharedDtor() {
  GOOGLE_DCHECK(GetArena() == nullptr);
}

void Position3d::ArenaDtor(void* object) {
  Position3d* _this = reinterpret_cast< Position3d* >(object);
  (void)_this;
}
void Position3d::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void Position3d::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const Position3d& Position3d::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_Position3d_protos_2fPosition3d_2eproto.base);
  return *internal_default_instance();
}


void Position3d::Clear() {
// @@protoc_insertion_point(message_clear_start:Position3d)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  ::memset(&x_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&z_) -
      reinterpret_cast<char*>(&x_)) + sizeof(z_));
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* Position3d::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // float x = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 13)) {
          x_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else goto handle_unusual;
        continue;
      // float y = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 21)) {
          y_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else goto handle_unusual;
        continue;
      // float z = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 29)) {
          z_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag,
            _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
            ptr, ctx);
        CHK_(ptr != nullptr);
        continue;
      }
    }  // switch
  }  // while
success:
  return ptr;
failure:
  ptr = nullptr;
  goto success;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* Position3d::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:Position3d)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // float x = 1;
  if (!(this->x() <= 0 && this->x() >= 0)) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(1, this->_internal_x(), target);
  }

  // float y = 2;
  if (!(this->y() <= 0 && this->y() >= 0)) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(2, this->_internal_y(), target);
  }

  // float z = 3;
  if (!(this->z() <= 0 && this->z() >= 0)) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(3, this->_internal_z(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:Position3d)
  return target;
}

size_t Position3d::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:Position3d)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // float x = 1;
  if (!(this->x() <= 0 && this->x() >= 0)) {
    total_size += 1 + 4;
  }

  // float y = 2;
  if (!(this->y() <= 0 && this->y() >= 0)) {
    total_size += 1 + 4;
  }

  // float z = 3;
  if (!(this->z() <= 0 && this->z() >= 0)) {
    total_size += 1 + 4;
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void Position3d::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:Position3d)
  GOOGLE_DCHECK_NE(&from, this);
  const Position3d* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<Position3d>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:Position3d)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:Position3d)
    MergeFrom(*source);
  }
}

void Position3d::MergeFrom(const Position3d& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:Position3d)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (!(from.x() <= 0 && from.x() >= 0)) {
    _internal_set_x(from._internal_x());
  }
  if (!(from.y() <= 0 && from.y() >= 0)) {
    _internal_set_y(from._internal_y());
  }
  if (!(from.z() <= 0 && from.z() >= 0)) {
    _internal_set_z(from._internal_z());
  }
}

void Position3d::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:Position3d)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void Position3d::CopyFrom(const Position3d& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:Position3d)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Position3d::IsInitialized() const {
  return true;
}

void Position3d::InternalSwap(Position3d* other) {
  using std::swap;
  _internal_metadata_.Swap<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(&other->_internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::internal::memswap<
      PROTOBUF_FIELD_OFFSET(Position3d, z_)
      + sizeof(Position3d::z_)
      - PROTOBUF_FIELD_OFFSET(Position3d, x_)>(
          reinterpret_cast<char*>(&x_),
          reinterpret_cast<char*>(&other->x_));
}

::PROTOBUF_NAMESPACE_ID::Metadata Position3d::GetMetadata() const {
  return GetMetadataStatic();
}


// @@protoc_insertion_point(namespace_scope)
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::Position3d* Arena::CreateMaybeMessage< ::Position3d >(Arena* arena) {
  return Arena::CreateMessageInternal< ::Position3d >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
