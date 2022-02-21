---@type TestTableArraysTemplate
local TestTableArraysTemplateFieldsIndex ={
  Id = 1,
  Weapons = 2,
  born_position = 3,
  TestTypes = 4,
  LinkId = 5,
  ModeL = 6,
  Icon = 7,
  MachineTypes = 8,
  MapType = 9,
}
local Position3dFieldsIndex ={
  x = 1,
  y = 2,
  z = 3,
}
local TestType_FieldsIndex ={
  types = 1,
  id = 2,
}
local TestTableArraysTemplateCustom ={
  born_position = {0,Position3dFieldsIndex},
  TestTypes = {1,TestType_FieldsIndex},
}
local T = {}
function T.T1()
  return {1,{2,1,3},{1.0,0,3.0},nil,1,"hero_chushi","chushi",nil,"222.0"}
end
function T.T2()
  return {2,{2,1,4},nil,{{nil,2},{{1},2}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T3()
  return {3,{2,1,5},nil,{{{1},2},{{1},4}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T4()
  return {4,{2,1,6},nil,{{nil,0},{nil,0}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T5()
  return {5,{2,1,7},{1.0,2.0,3.0},{{{1},2},{{1},6}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T6()
  return {6,{2,1,8},{1.0,2.0,4.0},{{{1},2},{{1},7}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T7()
  return {7,{2,1,9},{1.0,2.0,5.0},{{{1},2},{{1},8}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T8()
  return {8,{2,1,10},{1.0,2.0,6.0},{{{1},2},{{1},9}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T9()
  return {9,{2,1,11},{1.0,2.0,7.0},{{{1},2},{{1},10}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T10()
  return {10,{2,1,12},{1.0,2.0,8.0},{{{1},2},{{1},11}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
local TestTableArraysTemplate = {
  Values = {}
}
---@return TestTableArrayTemplate
function TestTableArraysTemplate.GetTableByIndex(index)
  if TestTableArraysTemplate.Values[index]==nil then
   TestTableArraysTemplate.Values[index]=New_Config(T['T'..index](),TestTableArraysTemplateFieldsIndex,TestTableArraysTemplateCustom)
  end
  return TestTableArraysTemplate.Values[index]
end
function TestTableArraysTemplate.GetLength()
 return 10
end
function TestTableArraysTemplate.Dispose()
 TestTableArraysTemplate.Values={}
end
return TestTableArraysTemplate