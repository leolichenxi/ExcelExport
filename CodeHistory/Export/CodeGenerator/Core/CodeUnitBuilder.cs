using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Reflection;
using Newtonsoft.Json.Linq;


// [Serializable]
// public class BuildObject
// {
//     public string outFilePath;
//     public string nameSpace;
//     public string className;
//     public string comment;
//     public string type;
//     public BuildMember[] members;
//     public BuildChildObject[] Objects;
// }
//
// public class BuildChildObject
// {
//     public string className;
//     public string comment;
//     public string type;
//     public BuildMember[] members;
// }
//
// [Serializable]
// public class BuildMember
// {
//     public string type;
//     public string filedName;
//     public string comment;
// }

public class MemberContext
{
    public JToken ItemType { get; private set; }
    public string Comment { get; private set; }

    private MemberContext()
    {
    }

    public static MemberContext Get(JArray value)
    {
        MemberContext context = new MemberContext
        {
            ItemType = value[0],
            Comment = value.Count > 1 ? value[1].ToString() : null
        };
        return context;
    }
}

public class CodeUnitBuilder
{
    public static readonly Dictionary<string, string> BaseTypes = new Dictionary<string, string>()
    {
        ["int"] = "System.Int32",
        ["double"] = "System.Double",
        ["string"] = "System.String",
        ["bool"] = "System.Boolean",
    };

    //
    // public static readonly HashSet<string> BaseObjects = new HashSet<string>()
    // {
    //     "class","enum","struct"
    // };
    public const string PropertySign = " { get; private set; }";
    public const string PropertySignReplace = PropertySign + ";";
    public const string MethodInitName = "OnInit";
    public const string MethodInitComment = "Init Function";
    public const string MethodReadName = "Read";
    public const string MethodLoadName = "Load";
    public const string GeneratorUtility = "GeneratorUtility";
    public const string IConfigElement = "IConfigElement";
    public const string IGenerateObject = "IGenerateObject";

    public const string Element = "element";
    public const string KRoot = "root";
    public const string KItem = "item";

    public const string KSchema = "schema";
    // public const string KOutFilePath = "export_file";

    public CodeCompileUnit CompileUnit { get; }
    private Dictionary<string, CodeTypeDeclaration> _typeDeclarations = new Dictionary<string, CodeTypeDeclaration>();
    public string OutFileName { get; private set; }
    public string ClassName { get; private set; }
    public string ItemName { get; private set; }
    public bool IsItem { get; private set; }

    private readonly JToken _jToken;

    public CodeUnitBuilder(JToken token)
    {
        _jToken = token;
        CompileUnit = Build();
    }

    private CodeCompileUnit Build()
    {
        CodeCompileUnit unit = new CodeCompileUnit();
        CodeNamespace codeNamespace = new CodeNamespace(CodeBuilder.OutNameSpace);
        unit.Namespaces.Add(codeNamespace);
        ClassName = _jToken[KRoot].ToString();
        ItemName = _jToken[KItem].ToString();
        IsItem = ClassName.Contains(ItemName + 's');
        OutFileName = ClassName + ".cs";
        JObject schema = _jToken[KSchema] as JObject;
        CodeTypeDeclaration codeTypeDeclaration = Build(ClassName, schema, null, null);
        codeNamespace.Types.Add(codeTypeDeclaration);
        return unit;
    }


    /// <summary>
    /// 返回对象声明
    /// </summary>
    /// <param name="className">编出脚本的类名</param>
    /// <param name="members">类的成员变量</param>
    /// <param name="des">注释</param>
    /// <param name="parent">从属类</param>
    /// <returns></returns>
    private CodeTypeDeclaration Build(string className, JObject members, string des, CodeTypeDeclaration parent)
    {
        CodeTypeDeclaration codeTypeDeclaration = new CodeTypeDeclaration(className)
        {
            TypeAttributes = TypeAttributes.Public,
            IsClass = true
        };
        bool isRoot = parent == null;
        if (!isRoot)
        {
            parent.Members.Add(codeTypeDeclaration);
            codeTypeDeclaration.TypeAttributes |= TypeAttributes.Sealed;
        }

        codeTypeDeclaration.BaseTypes.Add(new CodeTypeReference(IGenerateObject));
        if (!string.IsNullOrEmpty(des))
        {
            codeTypeDeclaration.Comments.Add(new CodeCommentStatement(des));
        }

        CodeStatementCollection statements = new CodeStatementCollection();
        foreach (var member in members)
        {
            MemberContext context = MemberContext.Get(member.Value as JArray);
            string typeName = Build(member.Key, context, codeTypeDeclaration);
            CodeStatement statement = BuildProperty(member.Key, typeName, context.Comment, codeTypeDeclaration);
            statements.Add(statement);
        }

        BuildClassMethods(codeTypeDeclaration, statements, isRoot);
        return codeTypeDeclaration;
    }

    private CodeStatement BuildProperty(string memberFiledName, string typeName, string contextComment, CodeTypeDeclaration parent)
    {
        CodeMemberField member = new CodeMemberField
        {
            Type = new CodeTypeReference(typeName),
            Name = memberFiledName
        };
        member.Comments.AddRange(BuildDocComments(contextComment));
        member.Attributes = MemberAttributes.Final | MemberAttributes.Public;
        member.Name += PropertySign;
        parent.Members.Add(member);
        CodeAssignStatement assign = new CodeAssignStatement(
            new CodeVariableReferenceExpression("this." + memberFiledName),
            new CodeVariableReferenceExpression(string.Format("{0}.Get(element, \"{1}\",{2})", GeneratorUtility, memberFiledName, "this." + memberFiledName)));
        return assign;
    }

    private string Build(string filedName, MemberContext context, CodeTypeDeclaration parent)
    {
        switch (context.ItemType.Type)
        {
            case JTokenType.String:
                return GetBaseType(context.ItemType.ToString());
            case JTokenType.Array:
                return BuildArray(filedName, context.ItemType as JArray, parent);
            case JTokenType.Object:
                filedName = filedName.ToFirstCharUpper() + "_";
                var key = context.ItemType.ToString();
                // 说明重复
                if (_typeDeclarations.TryGetValue(key, out CodeTypeDeclaration codeTypeDeclaration))
                {
                    codeTypeDeclaration = BuildObject(filedName, codeTypeDeclaration, parent);
                }
                else
                {
                    codeTypeDeclaration = Build(filedName, context.ItemType as JObject, context.Comment, parent);
                    _typeDeclarations.Add(key, codeTypeDeclaration);
                }

                return codeTypeDeclaration.Name;
            default:
                throw new NotSupportedException();
        }
    }

    private CodeTypeDeclaration BuildObject(string name, CodeTypeDeclaration baseType, CodeTypeDeclaration parent)
    {
        baseType.TypeAttributes &= ~TypeAttributes.Sealed;
        CodeTypeDeclaration typeDeclaration = new CodeTypeDeclaration(name)
        {
            IsClass = true,
            TypeAttributes = TypeAttributes.Public | TypeAttributes.Sealed,
        };
        typeDeclaration.BaseTypes.Add(baseType.Name);
        parent.Members.Add(typeDeclaration);
        return typeDeclaration;
    }

    private string GetBaseType(string key)
    {
        return BaseTypes[key];
    }

    private string BuildArray(string filedName, JArray type, CodeTypeDeclaration parent)
    {
        var member = MemberContext.Get(type);
        string baseName = filedName.Remove(filedName.Length - 1);
        return Build(baseName, member, parent) + "[]";
    }

    // private void BuildMembers(CodeTypeDeclaration typeDeclaration, BuildMember[] buildMembers)
    // {
    //     for (int i = 0; i < buildMembers.Length; i++)
    //     {
    //         BuildMember buildMember = buildMembers[i];
    //         CodeMemberField member = new CodeMemberField();
    //         if (!BaseTypes.TryGetValue(buildMember.type, out string type))
    //         {
    //             type = buildMember.type;
    //         }
    //
    //         member.Type = new CodeTypeReference(type);
    //         member.Name = buildMember.filedName;
    //         member.Comments.AddRange(BuildDocComments(buildMember.comment));
    //         member.Attributes = MemberAttributes.Final | MemberAttributes.Public;
    //         member.Name += PropertySign;
    //         typeDeclaration.Members.Add(member);
    //     }
    // }


    private void BuildClassMethods(CodeTypeDeclaration codeTypeDeclaration, CodeStatementCollection statementCollection, bool isRoot)
    {
        CodeMemberMethod readMethod = new CodeMemberMethod()
        {
            Name = MethodReadName,
            Attributes = MemberAttributes.Public | MemberAttributes.Final,
        };
        CodeParameterDeclarationExpression element = new CodeParameterDeclarationExpression(IConfigElement, Element);
        readMethod.Parameters.Add(element);
        readMethod.Statements.AddRange(statementCollection);
        codeTypeDeclaration.Members.Add(readMethod);

        //Create Static Load Method;   
        if (isRoot)
        {
            // Create Init Function;
            CodeMemberMethod memberInitMethod = new CodeMemberMethod {Name = MethodInitName, Attributes = MemberAttributes.Public};
            memberInitMethod.Comments.AddRange(BuildDocComments(MethodInitComment));
            readMethod.Statements.Add(new CodeMethodInvokeExpression(new CodeThisReferenceExpression(), MethodInitName));
            codeTypeDeclaration.Members.Add(memberInitMethod);
            codeTypeDeclaration.Members.Add(CreateLoadMethod());
            codeTypeDeclaration.Members.Add(CreateGenericsLoadMethod());
        }
    }

    private CodeMemberMethod CreateLoadMethod()
    {
        CodeMemberMethod loadMethod = new CodeMemberMethod()
        {
            Name = MethodLoadName,
            Attributes = MemberAttributes.Public | MemberAttributes.Static
        };
        loadMethod.ReturnType = new CodeTypeReference(ClassName + (IsItem ? "[]" : ""));
        CodeMethodReturnStatement returnStatement = new CodeMethodReturnStatement(
            new CodeVariableReferenceExpression($"{MethodLoadName}<{ClassName}>()")
        );
        loadMethod.Statements.Add(returnStatement);
        return loadMethod;
    }

    private CodeMemberMethod CreateGenericsLoadMethod()
    {
        CodeMemberMethod loadMethod = new CodeMemberMethod()
        {
            Name = MethodLoadName,
            Attributes = MemberAttributes.Public | MemberAttributes.Static,
        };
        loadMethod.ReturnType = new CodeTypeReference("T" + (IsItem ? "[]" : ""));

        CodeTypeParameter typeParameter = new CodeTypeParameter("T");
        typeParameter.HasConstructorConstraint = true;
        typeParameter.Constraints.Add(new CodeTypeReference(ClassName));
        loadMethod.TypeParameters.Add(typeParameter);
        string express;
        if (IsItem)
        {
            express = $"{GeneratorUtility}.{MethodLoadName}<T>(\"{ClassName}\",\"{ItemName}\")";
        }
        else
        {
            express = $"{GeneratorUtility}.{MethodLoadName}<T>(\"{ClassName}\")";
        }

        CodeMethodReturnStatement returnStatement = new CodeMethodReturnStatement(new CodeVariableReferenceExpression(express));
        loadMethod.Statements.Add(returnStatement);
        return loadMethod;
    }

    private CodeCommentStatementCollection BuildDocComments(params string[] comment)
    {
        CodeCommentStatementCollection comments = new CodeCommentStatementCollection();
        if (!IsNullOrEmpty(comment))
        {
            comments.Add(new CodeCommentStatement("<summary>", true));
            for (int i = 0; i < comment.Length; i++)
            {
                comments.Add(new CodeCommentStatement(comment[i], true));
            }

            comments.Add(new CodeCommentStatement("<summary>", true));
        }

        return comments;
    }

    private bool IsNullOrEmpty(params string[] comment)
    {
        if (comment == null)
        {
            return true;
        }

        for (int i = 0; i < comment.Length; i++)
        {
            if (!string.IsNullOrEmpty(comment[i]))
            {
                return false;
            }
        }

        return true;
    }
}