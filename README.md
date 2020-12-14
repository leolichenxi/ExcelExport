# ExcelExport
Excel to json,lua and protobuf datas,also export to script language which protoc support. Write by python.

### 说明:

脚本主要为excel转数据和脚本。支持的转出数据格式为：lua json protobuf格式，依次储存在导出文件夹lua,json,protobuf中,生成脚本原理为excel转proto,在protos文件夹下,使用protoc 生成。可根据生成的protos 自行导出各语言脚本。参考：https://developers.google.com/protocol-buffers


1. 支持字段 int,float,double,string.bool类型，配置方式参考示例excel。
2. 支持对象配置方式 

### 导出：
  
 
### 使用方法：
