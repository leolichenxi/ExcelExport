// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: protos/PositionArray3d.proto

#include "protos/PositionArray3d.pb.h"

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
class PositionArray3dDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<PositionArray3d> _instance;
} _PositionArray3d_default_instance_;
static void InitDefaultsscc_info_PositionArray3d_protos_2fPositionArray3d_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::_PositionArray3d_default_instance_;
    new (ptr) ::PositionArray3d();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_PositionArray3d_protos_2fPositionArray3d_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_PositionArray3d_protos_2fPositionArray3d_2eproto}, {}};

static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_protos_2fPositionArray3d_2eproto[1];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_protos_2fPositionArray3d_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_protos_2fPositionArray3d_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_protos_2fPositionArray3d_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::PositionArray3d, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::PositionArray3d, xs_),
  PROTOBUF_FIELD_OFFSET(::PositionArray3d, ys_),
  PROTOBUF_FIELD_OFFSET(::PositionArray3d, zs_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::PositionArray3d)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::_PositionArray3d_default_instance_),
};

const char descriptor_table_protodef_protos_2fPositionArray3d_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\034protos/PositionArray3d.proto\"5\n\017Positi"
  "onArray3d\022\n\n\002xs\030\001 \003(\002\022\n\n\002ys\030\002 \003(\002\022\n\n\002zs\030"
  "\003 \003(\002b\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_protos_2fPositionArray3d_2eproto_deps[1] = {
};
static ::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase*const descriptor_table_protos_2fPositionArray3d_2eproto_sccs[1] = {
  &scc_info_PositionArray3d_protos_2fPositionArray3d_2eproto.base,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_protos_2fPositionArray3d_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_protos_2fPositionArray3d_2eproto = {
  false, false, descriptor_table_protodef_protos_2fPositionArray3d_2eproto, "protos/PositionArray3d.proto", 93,
  &descriptor_table_protos_2fPositionArray3d_2eproto_once, descriptor_table_protos_2fPositionArray3d_2eproto_sccs, descriptor_table_protos_2fPositionArray3d_2eproto_deps, 1, 0,
  schemas, file_default_instances, TableStruct_protos_2fPositionArray3d_2eproto::offsets,
  file_level_metadata_protos_2fPositionArray3d_2eproto, 1, file_level_enum_descriptors_protos_2fPositionArray3d_2eproto, file_level_service_descriptors_protos_2fPositionArray3d_2eproto,
};

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_protos_2fPositionArray3d_2eproto = (static_cast<void>(::PROTOBUF_NAMESPACE_ID::internal::AddDescriptors(&descriptor_table_protos_2fPositionArray3d_2eproto)), true);

// ===================================================================

class PositionArray3d::_Internal {
 public:
};

PositionArray3d::PositionArray3d(::PROTOBUF_NAMESPACE_ID::Arena* arena)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena),
  xs_(arena),
  ys_(arena),
  zs_(arena) {
  SharedCtor();
  RegisterArenaDtor(arena);
  // @@protoc_insertion_point(arena_constructor:PositionArray3d)
}
PositionArray3d::PositionArray3d(const PositionArray3d& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      xs_(from.xs_),
      ys_(from.ys_),
      zs_(from.zs_) {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  // @@protoc_insertion_point(copy_constructor:PositionArray3d)
}

void PositionArray3d::SharedCtor() {
}

PositionArray3d::~PositionArray3d() {
  // @@protoc_insertion_point(destructor:PositionArray3d)
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

void PositionArray3d::SharedDtor() {
  GOOGLE_DCHECK(GetArena() == nullptr);
}

void PositionArray3d::ArenaDtor(void* object) {
  PositionArray3d* _this = reinterpret_cast< PositionArray3d* >(object);
  (void)_this;
}
void PositionArray3d::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void PositionArray3d::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const PositionArray3d& PositionArray3d::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_PositionArray3d_protos_2fPositionArray3d_2eproto.base);
  return *internal_default_instance();
}


void PositionArray3d::Clear() {
// @@protoc_insertion_point(message_clear_start:PositionArray3d)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  xs_.Clear();
  ys_.Clear();
  zs_.Clear();
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* PositionArray3d::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // repeated float xs = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 10)) {
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::PackedFloatParser(_internal_mutable_xs(), ptr, ctx);
          CHK_(ptr);
        } else if (static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 13) {
          _internal_add_xs(::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr));
          ptr += sizeof(float);
        } else goto handle_unusual;
        continue;
      // repeated float ys = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 18)) {
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::PackedFloatParser(_internal_mutable_ys(), ptr, ctx);
          CHK_(ptr);
        } else if (static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 21) {
          _internal_add_ys(::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr));
          ptr += sizeof(float);
        } else goto handle_unusual;
        continue;
      // repeated float zs = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 26)) {
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::PackedFloatParser(_internal_mutable_zs(), ptr, ctx);
          CHK_(ptr);
        } else if (static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 29) {
          _internal_add_zs(::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr));
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

::PROTOBUF_NAMESPACE_ID::uint8* PositionArray3d::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:PositionArray3d)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // repeated float xs = 1;
  if (this->_internal_xs_size() > 0) {
    target = stream->WriteFixedPacked(1, _internal_xs(), target);
  }

  // repeated float ys = 2;
  if (this->_internal_ys_size() > 0) {
    target = stream->WriteFixedPacked(2, _internal_ys(), target);
  }

  // repeated float zs = 3;
  if (this->_internal_zs_size() > 0) {
    target = stream->WriteFixedPacked(3, _internal_zs(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:PositionArray3d)
  return target;
}

size_t PositionArray3d::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:PositionArray3d)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // repeated float xs = 1;
  {
    unsigned int count = static_cast<unsigned int>(this->_internal_xs_size());
    size_t data_size = 4UL * count;
    if (data_size > 0) {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int32Size(
            static_cast<::PROTOBUF_NAMESPACE_ID::int32>(data_size));
    }
    int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(data_size);
    _xs_cached_byte_size_.store(cached_size,
                                    std::memory_order_relaxed);
    total_size += data_size;
  }

  // repeated float ys = 2;
  {
    unsigned int count = static_cast<unsigned int>(this->_internal_ys_size());
    size_t data_size = 4UL * count;
    if (data_size > 0) {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int32Size(
            static_cast<::PROTOBUF_NAMESPACE_ID::int32>(data_size));
    }
    int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(data_size);
    _ys_cached_byte_size_.store(cached_size,
                                    std::memory_order_relaxed);
    total_size += data_size;
  }

  // repeated float zs = 3;
  {
    unsigned int count = static_cast<unsigned int>(this->_internal_zs_size());
    size_t data_size = 4UL * count;
    if (data_size > 0) {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int32Size(
            static_cast<::PROTOBUF_NAMESPACE_ID::int32>(data_size));
    }
    int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(data_size);
    _zs_cached_byte_size_.store(cached_size,
                                    std::memory_order_relaxed);
    total_size += data_size;
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void PositionArray3d::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:PositionArray3d)
  GOOGLE_DCHECK_NE(&from, this);
  const PositionArray3d* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<PositionArray3d>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:PositionArray3d)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:PositionArray3d)
    MergeFrom(*source);
  }
}

void PositionArray3d::MergeFrom(const PositionArray3d& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:PositionArray3d)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  xs_.MergeFrom(from.xs_);
  ys_.MergeFrom(from.ys_);
  zs_.MergeFrom(from.zs_);
}

void PositionArray3d::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:PositionArray3d)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void PositionArray3d::CopyFrom(const PositionArray3d& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:PositionArray3d)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool PositionArray3d::IsInitialized() const {
  return true;
}

void PositionArray3d::InternalSwap(PositionArray3d* other) {
  using std::swap;
  _internal_metadata_.Swap<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(&other->_internal_metadata_);
  xs_.InternalSwap(&other->xs_);
  ys_.InternalSwap(&other->ys_);
  zs_.InternalSwap(&other->zs_);
}

::PROTOBUF_NAMESPACE_ID::Metadata PositionArray3d::GetMetadata() const {
  return GetMetadataStatic();
}


// @@protoc_insertion_point(namespace_scope)
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::PositionArray3d* Arena::CreateMaybeMessage< ::PositionArray3d >(Arena* arena) {
  return Arena::CreateMessageInternal< ::PositionArray3d >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
