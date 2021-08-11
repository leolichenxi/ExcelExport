
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
Excel to json,lua and protobuf  flatbuffer datas,also export to script language which protoc and flatc support. Write by python

### 说明:

脚本主要为excel转数据和脚本。支持的转出数据格式为：lua json protobuf,flatbuffer格式，依次储存在导出文件夹lua,json,protobuf,falt相关中,protobuf生成脚本原理为excel转proto,在protos文件夹下,使用protoc 生成。可根据生成的.proto 自行导出各语言脚本,生成的lua也会创建一份基于emmylua插件规则的https://github.com/EmmyLua/IntelliJ-EmmyLua  luaAPI用于智能高亮。
flatbuffer 生成.fbs文件和要求的json,json格式数据再转成二进制文件。

根据项目实际需求选择相应的数据。


1. 支持字段 int,float,string.bool类型，配置方式参考示例excel;
2. 支持对象配置方式;
3. 支持数组配置;

>使用场景：unity游戏开发，服务端等;

>待完善 long,double 等；由于python3移除long数据转换，如有需求暂配置字符串，脚本中自定义转化。

### 表格分类

设计分两类表暂命名：单表,列表.

> 单表： 类似配置表1.xlsx,数据为一份,通常为全局表,无复用需求.

> 列表： 存在N条数据规则一样.

### 配置规范

#### 表名

> 中文名|英文名, 英文名驼峰命名TestGlobal
1. 尽量全局表类表放一张表格里或者同一个Excel多个页签；
2. 任何单表或者列表内都不建议配置string类型数组，在有需要文本的地方配置id索引到对应的文本列表；提高服用性和后期多语言翻译。

#### 字段

1. 字段名不允许所有的字段命名不允许出现符号_ ，中文，或者数组开头，比如1Test,Test_Filed,啊Filed,Filed啊。
2. 数组类型字段以,分割，eg: int[] 可配置数据  1,2,5,10;
3. 基础类型支持： int float double string bool ;
4. 对象数组  Position3D[]  {int x;int y;int[] z}[] 对应数据举例 {1,2;2,6;3}{2;5;10,12} 用{}包围,字段间用分号;隔开;


### 潜在规则：

1. 列表会在类名后自动加s,数组类都会自动加s;
2. 声明一个数据对象：例如  Position3D  {int x;int y;int[] z} 对应数据为 1;2;1,2,3 即 x = 1,y = 2, z = 1,2,3;
3. Excel 行第一个前加 #或者留空 此行不会被解析对象或加入数列;
4. 列表连续空白三行之后的不会被加入数据;

> 支持全局类型配置方法新加的在custom.xlsx,这样在全局可以像基础类型那样定义，参考Position3d.暂不支持全局枚举

### 注意事项：

> 使用者需注意配置string文本的问题, 这里不建议在对象或数组里配置string类型,因为分割符可能导致意想不到的结果,比如长度为2 string[],第一句话含有(";"),第二句话含有(",")
就会解析错误; 这种情况建议新建一张string 文本表 这里都填上索引id,也方便多语言翻译和文本复用。


### 关键字分割符
任何配置文本数组的地方不得包含以下分割符，否则解析数据异常
数据解析的特殊符号 |,:;{}[]都是英文输入法状态下的符号。

### 所需配置

Python3以上
protoc 支持proto3,proto2兼容性未测试
python 依赖库： google,protobuf,xlrd,refection


### 性能选择

[Benchmark](http://google.github.io/flatbuffers/md__benchmarks.html)

1. json小项目优选
2. 中大型项目flatbuffer和protobuff 两者flatbuffer除了文件稍微比probof二进制文件稍微大些 其它完胜，但开发调用代码比protobuf冗余些，而且 在csharp中 flatbbufer 是作为值类型存在。意味着这作为参数传递会
造成copy，但flatbuffer内部依赖ByteBuffer获取数组，可忽略。
3. 对于数组类型，flatbuffer 获取数组会造成gc,使用数组时需注意，如果先获取length再进行遍历，不会产生GC,GetArray会产生GC,对原始数据只有Get,所以不会修改原始数据，比较nice,如果正确使用。游戏项目推荐使用FlatBuffer，对内存占用最少。
4. Protobuf优势在于对数据压缩最少,对于一般项目protobuff 已经是很不错的选择。

```
        public T[] ToArray<T>(int pos, int len)
            where T : struct
        {
            AssertOffsetAndLength(pos, len);
            T[] arr = new T[len];
            Buffer.BlockCopy(_buffer.Buffer, pos, arr, 0, ArraySize(arr));
            return arr;
        }
```
##### 参考部分：
 * https://developers.google.com/protocol-buffers/docs/overview#scalar
 * https://github.com/EmmyLua
 * https://github.com/yanghuan/proton  特别鸣谢前同事@yanghuan 
 * https://github.com/EmmyLua/IntelliJ-EmmyLua 
 * https://developers.google.com/protocol-buffers
 * https://google.github.io/flatbuffers/

 #### License
 [Apache 2.0 license] (http://www.apache.org/licenses/LICENSE-2.0)
