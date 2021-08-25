using Config;

namespace ExampleFlat.Core
{
    public class TestGlobalTemplateManager:ConfigSingle<TestGlobalTemplateManager,TestGlobalTemplate>
    {
        protected override void OnInit(TestGlobalTemplate t)
        {
            
        }
    }
    
    public class TestTableArraysTemplateManager : ConfigSingleExtend<TestTableArraysTemplateManager,TestTableArraysTemplateList,TestTableArraysTemplate,int>
    {
        protected override int GetKey(TestTableArraysTemplate t)
        {
            return t.Id;
        }

        protected override int GetLength()
        {
            return Template.TestTableArraysLength;
        }

        protected override Config.TestTableArraysTemplate GetTemplate(int index)
        {
            return  Template.TestTableArrays(index).GetValueOrDefault();
        }
    }
}