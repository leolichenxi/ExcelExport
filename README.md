
'''
Copyright 2020 li Chenxi(lichenxi3010@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# ExcelExport
Excel to json,lua and protobuf datas,also export to script language which protoc support. Write by python.

### 说明:

脚本主要为excel转数据和脚本。支持的转出数据格式为：lua json protobuf格式，依次储存在导出文件夹lua,json,protobuf中,生成脚本原理为excel转proto,在protos文件夹下,使用protoc 生成。可根据生成的.proto 自行导出各语言脚本。参考：https://developers.google.com/protocol-buffers


1. 支持字段 int,float,double,string.bool类型，配置方式参考示例excel。
2. 支持对象配置方式 
3. 支持数组配置
4. 使用场景，unity游戏开发等。

### 表格分类

设计分两类表暂命名：单表,列表.

> 单表： 类似配置表1.xlsx,数据为一份,通常为全局表,无复用需求.

> 列表： 存在N条数据规则一样.
  
 
### 使用方法：

1. 基础类型支持： int float double string bool ;
2. 数组配置间隔符号为,   int[] 可配置数据  1,2,5,10;
3. 声明一个数据对象：例如  Position3D  {int x:int y:int[] z} 对应数据为 1:2:1,2,3 即 x = 1,y = 2, z = 1,2,3;
4. 对象数组  Position3D[]  {int x:int y:int[] z}[] 对应数据举例 1,2:2,6:3;2:5:10,12 中间用分号;隔开;
5. Excel 行第一个前加 #或者留空 此行不会被解析对象或加入数列;
6. 列表连续空白三行之后的不会被加入数据;

> 支持全局类型配置方法新加的在custom.xlsx,这样在全局可以像基础类型那样定义，参考Position3d.

##### 1.标记Sheet页  
google导出的代码读取数据相关的API。参考案列上传

### 注意事项：

> 使用者需注意string问题, 这里不建议在对象或数组里配置string类型,因为分割符可能导致意想不到的结果,比如 string[]  第一:句话,第二,句话
就会解析错误; 这种情况建议新建一张string 文本表 这里都填上索引id,也方便多语言翻译和文本复用


### 所需配置

Python3以上
protoc 支持proto3,proto2兼容性未测试
python 依赖库： google,protobuf,xlrd,refection


##### 参考部分：
 * https://developers.google.com/protocol-buffers/docs/overview#scalar
