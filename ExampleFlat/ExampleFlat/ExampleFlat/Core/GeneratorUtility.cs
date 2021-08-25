using System.IO;
using FlatBuffers;

namespace ExampleFlat.Core
{
    public static class GeneratorUtility
    {
        public static T Get<T>(string filePath) where T:IFlatbufferObject,new()
        {
            var t = new T();
            var bytes = File.ReadAllBytes(filePath);
            ByteBuffer byteBuffer = new ByteBuffer(bytes);
            t.__init(byteBuffer.GetInt(byteBuffer.Position) + byteBuffer.Position, byteBuffer);
            return t;
        }
    }
}