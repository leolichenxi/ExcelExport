---@type TestListTablesTemplate
local TestListTablesTemplateFieldsIndex ={
  key = 1,
}
local T = {}
function T.T1()
  return {"我去"}
end
local TestListTablesTemplate = {
  Values = {}
}
---@return TestListTableTemplate
function TestListTablesTemplate.GetTableByIndex(index)
  if TestListTablesTemplate.Values[index]==nil then
   TestListTablesTemplate.Values[index]=New_Config(T['T'..index](),TestListTablesTemplateFieldsIndex,TestListTablesTemplateCustom)
  end
  return TestListTablesTemplate.Values[index]
end
function TestListTablesTemplate.GetLength()
 return 1
end
function TestListTablesTemplate.Dispose()
 TestListTablesTemplate.Values={}
end
return TestListTablesTemplate