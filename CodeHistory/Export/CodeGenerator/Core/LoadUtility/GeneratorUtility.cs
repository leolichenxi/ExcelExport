using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using Newtonsoft.Json.Linq;

public interface IGenerateObject
{
    void Read(IConfigElement element);
}

public interface IConfigElement
{
    string GetAttribute(string name);
    string GetText();
    IEnumerable<IConfigElement> GetElements();
    IConfigElement GetElement(string name);
}

public static class GeneratorUtility
{
    private static class GeneratorConfig
    {
        public const string ConfigDir = "";
    }

    private const string JsonFileExt = ".json";

    public static T[] Load<T>(string root, string itemName) where T : IGenerateObject, new()
    {
        using (Stream stream = GetContentStream(root))
        {
            IConfigElement rootElement = LoadRootElement(stream);
            T[] items = GetArray(rootElement, Convert, default(T[]));
            return items != null ? items : new T[0];
        }
    }

    public static T Load<T>(string root) where T : IGenerateObject, new()
    {
        using (Stream stream = GetContentStream(root))
        {
            return Convert<T>(LoadRootElement(stream), default(T));
        }
    }

    public static int Get(IConfigElement element, string key, int _)
    {
        string attribute = element.GetAttribute(key);
        return Convert(attribute, _);
    }

    public static double Get(IConfigElement element, string key, double _)
    {
        string attribute = element.GetAttribute(key);
        return Convert(attribute, _);
    }

    public static bool Get(IConfigElement element, string key, bool _)
    {
        string attribute = element.GetAttribute(key);
        return Convert(attribute, _);
    }

    public static string Get(IConfigElement element, string key, string _)
    {
        string attribute = element.GetAttribute(key);
        return Convert(attribute, _);
    }

    public static T Get<T>(IConfigElement element, string key, T _) where T : IGenerateObject, new()
    {
        var node = element.GetElement(key);
        return Convert(node, _);
    }


    public static int[] Get(IConfigElement element, string key, int[] _)
    {
        return GetArray(element, key, Convert, _);
    }

    public static double[] Get(IConfigElement element, string key, double[] _)
    {
        return GetArray(element, key, Convert, _);
    }

    public static bool[] Get(IConfigElement element, string key, bool[] _)
    {
        return GetArray(element, key, Convert, _);
    }

    public static string[] Get(IConfigElement element, string key, string[] _)
    {
        return GetArray(element, key, Convert, _);
    }

    public static T[] Get<T>(IConfigElement element, string key, T[] _) where T : IGenerateObject, new()
    {
        return GetArray<T>(element, key, Convert, _);
    }

    private static IConfigElement LoadRootElement(Stream stream)
    {
        using (StreamReader streamReader = new StreamReader(stream, Encoding.UTF8))
        {
            JToken token = JToken.Parse(streamReader.ReadToEnd());
            return new JsonConfigElement(token);
        }
    }

    public static Stream GetContentStream(string fileName)
    {
        string path = Path.Combine(GeneratorConfig.ConfigDir, fileName + JsonFileExt);
        Stream stream = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read);
        return stream;
    }


    #region Converts

    private static int Convert(IConfigElement e, int _)
    {
        return Convert(e.GetText(), _);
    }

    private static double Convert(IConfigElement e, double _)
    {
        return Convert(e.GetText(), _);
    }

    private static bool Convert(IConfigElement e, bool _)
    {
        return Convert(e.GetText(), _);
    }

    private static string Convert(IConfigElement e, string _)
    {
        return Convert(e.GetText(), _);
    }

    private static int Convert(string s, int _)
    {
        if (string.IsNullOrEmpty(s))
        {
            return 0;
        }

        return int.Parse(s);
    }

    private static double Convert(string s, double _)
    {
        if (string.IsNullOrEmpty(s))
        {
            return 0;
        }

        return double.Parse(s);
    }

    private static bool Convert(string s, bool _)
    {
        if (string.IsNullOrEmpty(s))
        {
            return false;
        }

        return bool.Parse(s);
    }

    private static string Convert(string s, string _)
    {
        return s;
    }

    private static T Convert<T>(IConfigElement e, T _) where T : IGenerateObject, new()
    {
        if (e == null)
        {
            return default(T);
        }

        T t = new T();
        try
        {
            t.Read(e);
        }
        catch (Exception exception)
        {
            Console.WriteLine(exception.Message);
            throw;
        }

        return t;
    }

    private static T[] GetArray<T>(IConfigElement element, string itemName, Func<IConfigElement, T, T> convert, T[] _)
    {
        var node = element.GetElement(itemName);
        if (node == null)
        {
            return null;
        }

        return GetArray(node, convert, _);
    }

    private static T[] GetArray<T>(IConfigElement element, Func<IConfigElement, T, T> convert, T[] _)
    {
        List<T> list = new List<T>();
        foreach (var node in element.GetElements())
        {
            list.Add(convert(node, default(T)));
        }

        return list.Count > 0 ? list.ToArray() : null;
    }

    #endregion

    #region JsonElement

    private sealed class JsonConfigElement : IConfigElement
    {
        private JToken _element;

        public JsonConfigElement(JToken element)
        {
            _element = element;
        }

        public string GetAttribute(string name)
        {
            JObject obj = _element as JObject;
            var attribute = obj.GetOrDefault(name);
            return attribute != null ? attribute.ToString() : null;
        }

        public string GetText()
        {
            return _element.ToString();
        }

        public IConfigElement GetElement(string name)
        {
            JObject obj = _element as JObject;
            JToken attribute = obj.GetOrDefault(name);
            return attribute != null ? new JsonConfigElement(attribute) : null;
        }

        public IEnumerable<IConfigElement> GetElements()
        {
            JArray array = _element as JArray;
            return array.Select(i => new JsonConfigElement(i));
        }
    }

    #endregion


    #region Utility

    private static T GetOrDefault<K, T>(this IDictionary<K, T> dict, K key, T t = default(T))
    {
        T v;
        if (dict.TryGetValue(key, out v))
        {
            return v;
        }

        return t;
    }

    #endregion
}