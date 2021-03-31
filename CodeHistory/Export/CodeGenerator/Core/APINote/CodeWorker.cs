// using System;
// using System.CodeDom;
// using System.CodeDom.Compiler;
// using System.IO;
// using System.Reflection;
//
// namespace CodeGenerator.Core
// {
//     public class CompileInfo
//     {
//         public string className;
//         public string nameSpace;
//     }
//
//     public class CodeWorker
//     {
//         private readonly CodeDomProvider _provider = CodeDomProvider.CreateProvider("CSharp");
//         private readonly CodeGeneratorOptions _options = new CodeGeneratorOptions() {
//             BracingStyle = "C",  // 使用C 风格
//             ElseOnClosing = true,
//             IndentString = "    ",
//             BlankLinesBetweenMembers = true,
//         };
//
//         public void Compile()
//         {
//             // CompilerParameters cp = new CompilerParameters();
//             // cp.GenerateExecutable = true;
//             // cp.OutputAssembly = "Test";
//             // cp.GenerateInMemory = true;
//             // cp.TreatWarningsAsErrors = false;
//             //
//             // CodeTypeDeclaration typeDeclaration = new CodeTypeDeclaration()
//             // {
//             //     Name = "Test",
//             //     TypeAttributes = TypeAttributes.Class | TypeAttributes.Public | TypeAttributes.Sealed | TypeAttributes.Serializable
//             // };
//             //
//             // CodeMemberMethod method = new CodeMemberMethod()
//             // {
//             //     Name = "Debug",
//             //     Attributes = MemberAttributes.Public | MemberAttributes.Final
//             // };
//             // method.Comments.Add(new CodeCommentStatement("<summary>", true));
//             // method.Comments.Add(new CodeCommentStatement("@CSharpLua.Ignore", true));
//             // method.Comments.Add(new CodeCommentStatement("</summary>", true));
//             // typeDeclaration.Members.Add(method);
//             Save(new CodeUnitCreator());
//         }
//         
//         private void Save(CodeUnitCreator creator)
//         {
// #if DEBUG
//             var unit = creator.BuildCodeCompileUnit();
//             _provider.GenerateCodeFromCompileUnit(unit, Console.Out, _options);   
// #endif
//             
//             // return;
//             // using (MemoryStream stream = new MemoryStream())
//             // {
//             //     StreamWriter sourceWriter = new StreamWriter(stream);
//             //     var unit = creator.BuildCodeCompileUnit();
//             //     _provider.GenerateCodeFromCompileUnit(unit, sourceWriter, _options);
//             //     sourceWriter.Flush();
//             //     stream.Seek(0, SeekOrigin.Begin);
//             //     
//             //     string path = Path.Combine("Test.cs");
//             //     StreamReader reader = new StreamReader(stream);
//             //     using (StreamWriter fileWriter = new StreamWriter(path)) {
//             //         while (true) {
//             //             string line = reader.ReadLine();
//             //             if (line != null) {
//             //                 int post = line.LastIndexOf('.');
//             //                 if (post != -1) {
//             //                     line = line.Substring(0, post);
//             //                 }
//             //                 fileWriter.WriteLine(line);
//             //             } else {
//             //                 break;
//             //             }
//             //         }
//             //     }
//             // }
//         }
//
//         public override string ToString()
//         {
//             return _provider.FileExtension;
//         }
//     }
// }