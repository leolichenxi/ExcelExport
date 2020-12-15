# ExcelExport
Excel to json,lua and protobuf datas,also export to script language which protoc support. Write by python.

### 说明:

脚本主要为excel转数据和脚本。支持的转出数据格式为：lua json protobuf格式，依次储存在导出文件夹lua,json,protobuf中,生成脚本原理为excel转proto,在protos文件夹下,使用protoc 生成。可根据生成的.proto 自行导出各语言脚本。参考：https://developers.google.com/protocol-buffers


1. 支持字段 int,float,double,string.bool类型，配置方式参考示例excel。
2. 支持对象配置方式 
3. 支持数组配置
4. 使用场景，unity游戏开发等。

### 导出：

参考 exprot.py 
  
 
### 使用方法：
google导出的代码读取数据相关的API。参考案列上传

### 注意事项：


### 所需配置

Python3 
protoc 支持proto3 proto2兼容性未知
python 依赖库： google,protobuf,xlrd,refection
