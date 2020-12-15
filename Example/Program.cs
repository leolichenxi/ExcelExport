using System;
using Config;
using System.IO;
namespace Example
{
    class Program
    {
        static void Main(string[] args)
        {
        

            TestGlobalTemplate template = TestGlobalTemplate.Parser.ParseFrom(GetByte(typeof(TestGlobalTemplate)));
            Console.WriteLine(template);
            Console.WriteLine(template.TestObj.C);

            TestGlobalTemplate template2 = TestGlobalTemplate.Parser.ParseJson(GetJson(typeof(TestGlobalTemplate)));
            Console.WriteLine(template2);
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
