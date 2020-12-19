using System;
using Config;
using System.IO;
namespace Example
{
    class Program
    {
        static void Main(string[] args)
        {

            TestGlobalTemplate template = TestGlobalTemplate.Parser.ParseJson(GetJson(typeof(TestGlobalTemplate)));
            Console.WriteLine(template);

            TestTableArraysTemplateList template2 = TestTableArraysTemplateList.Parser.ParseJson(GetJson(typeof(TestTableArraysTemplate)));
            Console.WriteLine(template2.TestTableArrays);

           
        }

        private static string GetJson(Type t)
        {
            return File.ReadAllText("json/" + t.Name + ".json");
        }

        private static byte[] GetByte(Type t)
        {
            return File.ReadAllBytes("protobuf/"+t.Name + ".byte");
        }
    }
}
