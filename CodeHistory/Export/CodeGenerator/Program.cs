using System;
using System.IO;
using ProtoBuf;
using Config;
namespace CodeGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            // try
            // {
            //     var data = File.ReadAllBytes("protobuf/TestGlobalTemplate.byte");
            //     var json = File.ReadAllText("json/TestGlobalTemplate.json");
            //     Console.WriteLine(json);
            //
            //     TestGlobalTemplate template = TestGlobalTemplate.Parser.ParseFrom(data);
            //     Console.WriteLine("================byte!!!");
            //     Console.WriteLine(template.TestIntArrays.Count);
            //
            //      template = TestGlobalTemplate.Parser.ParseJson(json);
            //     Console.WriteLine("================json!!!");
            //     Console.WriteLine(template);
            //
            // }
            // catch (Exception e)
            // {
            //     Console.WriteLine(e.Message);
            // }
            //
            //
            //
            //
            // return;
            //


            //File.WriteAllText("Core/Config/BattleParam1.json", b.ToString());
            TryGenerate();
        }

        private static void TryGenerate()
        {
            
            Console.Title = "脚本转换工具";
            try
            {
                CodeBuilder builder = new CodeBuilder();
                builder.Compile();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                Console.ReadLine();
            }
            finally
            {
                Console.WriteLine("success finish generate!!!!");
            }
        }
        public static byte[] Serialize<T>(T t)
        {
            try
            {
                //涉及格式转换，需要用到流，将二进制序列化到流中
                using (MemoryStream ms = new MemoryStream())
                {
                    //使用ProtoBuf工具的序列化方法
                    Serializer.Serialize<T>(ms, t);
                    //定义二级制数组，保存序列化后的结果
                    byte[] result = new byte[ms.Length];
                    //将流的位置设为0，起始点
                    ms.Position = 0;
                    //将流中的内容读取到二进制数组中
                    ms.Read(result, 0, result.Length);
                    return result;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("序列化失败: " + ex.ToString());
                return null;
            }
        }
    }

}
