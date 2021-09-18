using System;
using System.IO;
using FlatBuffers;
using Config;
using ExampleFlat.Core;

namespace ExampleFlat
{
    class Program
    {
        static void Main(string[] args)
        {
  
            var data = File.ReadAllBytes("data_bin/TestGlobalTemplate.bin");
            var bb = new ByteBuffer(data);
            var t = TestGlobalTemplate.GetRootAsTestGlobalTemplate(bb);
            Console.WriteLine(t.TestFloat);
            Console.WriteLine(t.TestString);
            Console.WriteLine(t.TestObj.Value.B);
            Console.WriteLine(t.TestObj1.Value.Bs(3));
            Console.WriteLine(t.TestDefineFromGlobal.Value.Z);
            Console.WriteLine(t.TestDefineFromGlobal2s(0).Value.X);
            Console.WriteLine(t.ToString());
            
            
            // var datas = File.ReadAllBytes("data_json/TestTableArraysTemplate.json");
            var datas = File.ReadAllBytes("data_bin/TestTableArraysTemplate.bin");
            
            var bbs = new ByteBuffer(datas);
            
            var ts = TestTableArraysTemplateList.GetRootAsTestTableArraysTemplateList(bbs);
            Console.WriteLine(ts.TestTableArrays(0).Value.Id);
            Console.WriteLine(ts.TestTableArrays(0).Value.Icon);
            Console.WriteLine(ts.TestTableArrays(0).Value.MachineType);
            Console.WriteLine(ts.TestTableArrays(0).Value.BornPosition.Value.X);
            Console.WriteLine(t.TestStringArraysLength);
            
            Console.WriteLine(ts.TestTableArraysLength);
            Console.WriteLine(ts.TestTableArrays(0).Value.TestTypesLength);
            Console.WriteLine( );
            

          
           
        }

        private static void Test(TestTableArraysTemplateList tst)
        {
            
        }
    }
}
