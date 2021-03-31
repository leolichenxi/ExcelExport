// using System;
// using System.CodeDom;
// using System.Collections.Generic;
//
// namespace CodeGenerator.Core
// {
//     public class CodeUnitCreator
//     {
//         
//         public CodeCompileUnit BuildCodeCompileUnit()
//         {
//             CodeTypeDeclaration typeDeclaration = new CodeTypeDeclaration()
//             {
//                 Name = "TestClass",
//             };
//             
//             CodeNamespace nameSpace = new CodeNamespace("TestNameSpace");
//             CodeNamespace nameSpace2 = new CodeNamespace("TestNameSpace2");
//             
//             // 声明变量 
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(string), "TestString"));  
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(int), "TestInt"));
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(double), "TestDouble"));
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(bool), "TestBool"));
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(bool), "TestBool"));
//             typeDeclaration.Members.Add(BuildMemberField());
//             typeDeclaration.Members.Add(BuildProperty());
//
//             typeDeclaration.Members.Add(BuildDelegate());
//             
//             CodeMemberMethod memberMethod = new CodeMemberMethod()
//             {
//                 Name = "TestFunction",
//                 Attributes = MemberAttributes.Public | MemberAttributes.Final,   
//             };
//             typeDeclaration.Members.Add(memberMethod);
//             CodeCompileUnit compileUnit = new CodeCompileUnit();
//
//             var structType = BuildStructType();
//             nameSpace.Types.Add(typeDeclaration);
//             nameSpace.Types.Add(structType);
//
//             var constructType = BuildConstructorType();
//             
//             nameSpace2.Types.AddRange(BuildInherit().ToArray());
//             // nameSpace2.Types.Add(constructType);
//             typeDeclaration.Members.Add(constructType);
//             nameSpace2.Types.Add(BuildTestAddFunction());
//             nameSpace2.Types.Add(BuildTextEnum());
//
//             nameSpace.Imports.Add(new CodeNamespaceImport("System.IO")); // 引入命名空间
//             compileUnit.ReferencedAssemblies.Add("System");                // 引用程序集
//             compileUnit.Namespaces.Add(nameSpace);
//             compileUnit.Namespaces.Add(nameSpace2);
//
//             return compileUnit;
//         }
//         
//         // 测试声明变量  
//         private CodeMemberField BuildMemberField()
//         {
//             CodeMemberField field = new CodeMemberField
//             {
//                 Name = "BuildMemberField", 
//                 Type = new CodeTypeReference(typeof(int))
//             };
//             return field;
//         }
//
//         private CodeTypeDeclaration BuildStructType()
//         {
//             CodeTypeDeclaration typeDeclaration = new CodeTypeDeclaration()
//             {
//                 Name = "TestStruct",
//             };
//             typeDeclaration.IsStruct = true;
//             typeDeclaration.Attributes = MemberAttributes.Public;
//             // typeDeclaration.Attributes = MemberAttributes.Private;
//             return typeDeclaration;
//         }
//
//         private CodeTypeDelegate BuildDelegate()
//         {
//             CodeTypeDelegate typeDelegate = new CodeTypeDelegate("TestDelegate");
//             typeDelegate.ReturnType = new CodeTypeReference(typeof(void));
//             return typeDelegate;
//         }
//
//         // 测试基类 接口 
//         private List<CodeTypeDeclaration>  BuildInherit()
//         {
//             List<CodeTypeDeclaration> declarations = new List<CodeTypeDeclaration>();
//             CodeTypeDeclaration typeDeclarationChild = new CodeTypeDeclaration("TestChild");
//             CodeTypeDeclaration typeDeclarationParent = new CodeTypeDeclaration("TestParent");
//             CodeTypeDeclaration typeDeclarationInterface = new CodeTypeDeclaration("TestParentInterface");
//             typeDeclarationInterface.IsInterface = true;
//             typeDeclarationChild.BaseTypes.Add(new CodeTypeReference("TestParent"));
//             typeDeclarationChild.BaseTypes.Add(new CodeTypeReference("TestParentInterface"));
//             CodeCommentStatement commentStatement = new CodeCommentStatement("这是一个注释",true);
//                 typeDeclarationInterface.Comments.Add(commentStatement);
//             declarations.Add(typeDeclarationInterface);
//             declarations.Add(typeDeclarationParent);
//             declarations.Add(typeDeclarationChild);
//
//             return declarations;
//         }
//
//         private CodeMemberProperty BuildProperty()
//         {
//             CodeMemberField memberField = new CodeMemberField(typeof(int), "_testProperty");
//             CodeMemberProperty memberProperty = new CodeMemberProperty();
//             memberProperty.Name = "TestProperty";
//             memberProperty.Type = new CodeTypeReference(typeof(int));
//             memberProperty.HasGet = true;
//             memberProperty.HasSet = false;
//             memberProperty.Attributes = MemberAttributes.Public | MemberAttributes.Final;
//            
//             CodeMethodReturnStatement returnStatement = new CodeMethodReturnStatement(
//                 new CodeFieldReferenceExpression(new CodeThisReferenceExpression(),
//                 memberField.Name));
//             memberProperty.GetStatements.Add(returnStatement);
//             
//             return memberProperty;
//         }
//
//         private CodeTypeDeclaration BuildConstructorType()
//         {
//             CodeTypeDeclaration declaration = new CodeTypeDeclaration();
//             declaration.Name = "TestConstructor";
//             declaration.IsClass = true;
//               
//             CodeConstructor constructor = new CodeConstructor();
//             constructor.Attributes = MemberAttributes.Final | MemberAttributes.Public;
//             declaration.Members.Add(constructor);
//             
//             CodeMemberField memberField = new CodeMemberField(typeof(int),"_testA");
//             memberField.Attributes = MemberAttributes.Private | MemberAttributes.Final;
//
//             declaration.Members.Add(memberField);
//             
//             CodeParameterDeclarationExpression parameterDeclarationExpression = new CodeParameterDeclarationExpression(memberField.Type,"testA");
//             constructor.Parameters.Add(parameterDeclarationExpression);
//             
//             CodeAssignStatement codeAssignStatement = new CodeAssignStatement(
//                 new CodeFieldReferenceExpression(new CodeThisReferenceExpression(), memberField.Name),
//                      new CodeVariableReferenceExpression(parameterDeclarationExpression.Name));
//             constructor.Statements.Add(codeAssignStatement);
//             return declaration;
//         }
//         
//         
//         private CodeTypeDeclaration BuildTestAddFunction()
//         {
//             CodeTypeDeclaration typeDeclaration = new CodeTypeDeclaration()
//             {
//                 Name = "TestStructSum",
//             };
//             
//             
//             CodeMemberMethod memberMethod = new CodeMemberMethod()
//             {
//                 Name = "TestAdd",
//                 Attributes = MemberAttributes.Public | MemberAttributes.Final,   
//             };
//             typeDeclaration.Members.Add(memberMethod);
//             
//             CodeVariableReferenceExpression left = new CodeVariableReferenceExpression("a");
//             CodeVariableReferenceExpression right = new CodeVariableReferenceExpression("b");
//             
//             CodeBinaryOperatorExpression operatorExpression = new CodeBinaryOperatorExpression();
//             operatorExpression.Operator = CodeBinaryOperatorType.Add;
//             operatorExpression.Left = left;
//             operatorExpression.Right = right;
//
//             CodeMethodReturnStatement returnStatement = new CodeMethodReturnStatement(operatorExpression);
//             memberMethod.Statements.Add(returnStatement);
//             
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(int),"a"));
//             typeDeclaration.Members.Add(new CodeMemberField(typeof(int),"b"));
//             
//             
//             return typeDeclaration;
//         }
//
//         private CodeTypeDeclaration BuildTextEnum()
//         {
//             CodeTypeDeclaration typeDeclaration = new CodeTypeDeclaration("TestEnum");
//             typeDeclaration.IsEnum = true;
//             typeDeclaration.Attributes = MemberAttributes.Public;
//             
//             CodeMemberField field = new CodeMemberField();
//             field.Name = "TestEnum1";
//             field.InitExpression = new CodePrimitiveExpression(15);
//
//             typeDeclaration.Members.Add(field);
//             
//             return typeDeclaration;
//         }
//         
//         private CodeVariableDeclarationStatement BuildVariableField()
//         {
//             CodeVariableDeclarationStatement declarationStatement = new CodeVariableDeclarationStatement(typeof(int),"BuildVariableField",new CodePrimitiveExpression(1000));
//             return declarationStatement;
//         }
//         
//     }
// }