# ExcelExport
Excel to json,lua and protobuf datas,also export to script language which protoc support. Write by python.

### 说明:

脚本主要为excel转数据和脚本。支持的转出数据格式为：lua json protobuf格式，依次储存在导出文件夹lua,json,protobuf中,生成脚本原理为excel转proto,在protos文件夹下,使用protoc 生成。可根据生成的protos 自行导出各语言脚本。参考：https://developers.google.com/protocol-buffers


1. 支持字段 int,float,double,string.bool类型，配置方式参考示例excel。
2. 支持对象配置方式 
3. 支持数组配置
4. 使用场景，unity游戏开发等。

### 导出：

参考 exprot.py 
  
 
### 使用方法：
csharp 核心方法 pasrse等。参考案列TODO 上传

### 注意事项：
1.配置类型如果为字符串数组，字符串不能有分隔符,
2.配置类型如果为对象数组 不支持字段有数组 数据,(同样因为分隔符为,后续优化)
3.配置类型如果为对象且不是数组，支持字段和数组为数组。

### 所需配置

Python3 
protoc 支持proto3 proto2兼容性未知
python 依赖库： google,protobuf,xlrd,refection
