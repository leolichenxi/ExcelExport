using System.IO;

public static class Utility
{
    public static string ToFirstCharUpper(this string s)
    {
        char first = s[0];
        if (!char.IsUpper(first))
        {
            return char.ToUpper(first) + s.Substring(1);
        }

        return s;
    }

    public static void PreparePath(string path)
    {
        if (File.Exists(path))
        {
            File.Delete(path);
        }

        if (!Directory.Exists(path))
        {
            Directory.CreateDirectory(path);
        }
    }
}