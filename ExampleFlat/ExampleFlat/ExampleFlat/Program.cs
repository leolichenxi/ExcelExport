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
  
            var data = File.ReadAllBytes("TestGlobalTemplatelower.bin");
            var bb = new ByteBuffer(data);
            var t = TestGlobalTemplate.GetRootAsTestGlobalTemplate(bb);
            Console.WriteLine(t.TestFloat);
            Console.WriteLine(t.ToString());

        }
    }
}
