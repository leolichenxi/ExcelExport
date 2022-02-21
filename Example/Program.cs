using System;
using Config;
using System.IO;
namespace Example
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] s = File.ReadAllLines("1.txt");
            for (int i = 0; i < s.Length; i++)
            {
                Console.WriteLine("{" + s[i].Replace("|", "}{") + "}");
                s[i] = "{" + s[i].Replace("|", "}{") + "}";
            }
            File.WriteAllLines("rs.txt", s);

            return;
            TestJson();
            TestProtobuf();

        }

        private static void TestJson()
        {

            TestGlobalTemplate template = TestGlobalTemplate.Parser.ParseJson(GetJson(typeof(TestGlobalTemplate)));
            Console.WriteLine(template);

            //TestTableArraysTemplateList template2 = TestTableArraysTemplateList.Parser.ParseJson(GetJson(typeof(TestTableArraysTemplate)));
            //Console.WriteLine(template2.TestTableArrays);
        }
        private static void TestProtobuf()
        {
            TestGlobalTemplate template = TestGlobalTemplate.Parser.ParseFrom(GetBytes(typeof(TestGlobalTemplate)));
            Console.WriteLine(template);

            //TestTableArraysTemplateList template2 = TestTableArraysTemplateList.Parser.ParseFrom(GetBytes(typeof(TestTableArraysTemplate)));
            //Console.WriteLine(template2.TestTableArrays);
        }

        private static string GetJson(Type t)
        {
            return File.ReadAllText("out_json/" + t.Name + ".json");
        }

        private static byte[] GetBytes(Type t)
        {
            return File.ReadAllBytes("out_protobuf/" + t.Name + ".bytes");
        }
    }
}
