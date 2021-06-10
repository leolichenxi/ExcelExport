using System;
using System.IO;
using FlatBuffers;
using Config;

namespace ExampleFlat
{
    class Program
    {
        static void Main(string[] args)
        {
  
            var data = File.ReadAllBytes("Config/TestGlobalTemplate.bin");
            var bb = new ByteBuffer(data);
            var t = TestGlobalTemplate.GetRootAsTestGlobalTemplate(bb);
            Console.WriteLine(t.TestFloat);
            Console.WriteLine(t.TestObj.Value.B);
            Console.WriteLine(t.TestObj1.Value.Bs(3));
            Console.WriteLine(t.TestDefineFromGlobal.Value.Z);
            Console.WriteLine(t.TestDefineFromGlobal2s(0).Value.X);
            Console.WriteLine(t.ToString());

            
            var datas = File.ReadAllBytes("Config/TestTableArraysTemplate.bin");
            var bbs = new ByteBuffer(datas);
            var ts = TestTableArraysTemplateList.GetRootAsTestTableArraysTemplateList(bbs);
            Console.WriteLine(ts.TestTableArrays(0).Value.Id);
            Console.WriteLine(ts.TestTableArrays(0).Value.Icon);
            Console.WriteLine(ts.TestTableArrays(0).Value.MachineType);
            Console.WriteLine(t.TestStringArraysLength);
        }
    }
}
