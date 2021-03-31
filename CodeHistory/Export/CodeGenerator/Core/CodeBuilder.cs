using System;
using System.CodeDom.Compiler;
using System.IO;
using Newtonsoft.Json.Linq;


public class CodeBuilder
{
    private const string ExportConfigFilePath = "export_config.json";
    private const string ExportCodeDomFilePath = "code_dom.json";

    private readonly CodeDomProvider _provider = CodeDomProvider.CreateProvider("CSharp");

    private readonly CodeGeneratorOptions _options = new CodeGeneratorOptions()
    {
        BracingStyle = "C", // 使用C 风格
        ElseOnClosing = true,
        IndentString = "    ",
        BlankLinesBetweenMembers = true,
    };

    private const string KeyNameSpace = "namespace";
    private const string KeyOutFolder = "outFolder";
    private const string KeySuffix = "suffix";
    private const string KeyFormat = "format";
    private JToken _token;

    public static string OutNameSpace { get; private set; }
    public static string OutFolder { get; private set; }
    public static string OutSuffix { get; private set; }
    public static string OutFormat { get; private set; }

    public CodeBuilder()
    {
        Build();
    }

    private void Build()
    {
        string schema = System.IO.File.ReadAllText(ExportCodeDomFilePath);
        _token = JArray.Parse(schema);

        string config = File.ReadAllText(ExportConfigFilePath);
        JToken token = JToken.Parse(config);
        OutNameSpace = token[KeyNameSpace].ToString();
        OutFolder = token[KeyOutFolder].ToString();
        OutSuffix = token[KeySuffix].ToString();
        OutFormat = token[KeyFormat].ToString();

#if RELEASE
        File.Delete(ExportCodeDomFilePath);
        File.Delete(ExportConfigFilePath);
#endif

        Console.WriteLine("ExportConfigFile info!!!");
        Console.WriteLine(config);
    }

    public void Compile()
    {
        Utility.PreparePath(OutFolder);
        foreach (var compileToken in _token)
        {
            CodeUnitBuilder codeUnitBuilder = new CodeUnitBuilder(compileToken);
            Save(codeUnitBuilder);
        }
    }

    private void Save(CodeUnitBuilder creator)
    {
        const int lineCount = 3;
        using MemoryStream stream = new MemoryStream();
        StreamWriter sourceWriter = new StreamWriter(stream);
        var unit = creator.CompileUnit;
        _provider.GenerateCodeFromCompileUnit(unit, sourceWriter, _options);
        sourceWriter.Flush();
        stream.Seek(0, SeekOrigin.Begin);
        int count = 0;
        string outDir = Path.Combine(OutFolder, OutSuffix);
        string path = Path.Combine(OutFolder, OutSuffix, creator.OutFileName);

        if (!Directory.Exists(outDir))
        {
            Directory.CreateDirectory(outDir);
        }

        StreamReader reader = new StreamReader(stream);
        using (StreamWriter fileWriter = new StreamWriter(path))
        {
            while (true)
            {
                string line = reader.ReadLine();
                if (line != null)
                {
                    if (count == lineCount)
                    {
                        int post = line.LastIndexOf('.');
                        if (post != -1)
                        {
                            line = line.Substring(0, post);
                            Console.WriteLine(line);
                        }
                    }
                    else
                    {
                        line = line.Replace(CodeUnitBuilder.PropertySignReplace, CodeUnitBuilder.PropertySign);
                    }

                    fileWriter.WriteLine(line);
                }
                else
                {
                    break;
                }

                count++;
            }
        }
    }
}