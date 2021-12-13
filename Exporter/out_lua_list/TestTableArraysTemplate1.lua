---@type TestTableArraysTemplate
local TestTableArraysTemplateFieldsIndex ={
  Id = 1,
  Weapons = 2,
  born_position = 3,
  TestTypes = 4,
  LinkId = 5,
  Model = 6,
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
  born_position = Position3dFieldsIndex,
  TestTypes = TestType_FieldsIndex,
}
local T = {}
function T.T1()
  return {1,{2,1,3},nil,{},1,"hero_chushi","chushi",{},"222.0"}
end
function T.T2()
  return {2,{2,1,4},nil,{{types = {},id = 2},{types = {1},id = 3}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T3()
  return {3,{2,1,5},nil,{{types = {1},id = 2},{types = {1},id = 4}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T4()
  return {4,{2,1,6},nil,{{types = {},id = 0},{types = {},id = 0}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T5()
  return {5,{2,1,7},{x = 1.0,y = 2.0,z = 3.0},{{types = {1},id = 2},{types = {1},id = 6}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T6()
  return {6,{2,1,8},{x = 1.0,y = 2.0,z = 4.0},{{types = {1},id = 2},{types = {1},id = 7}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T7()
  return {7,{2,1,9},{x = 1.0,y = 2.0,z = 5.0},{{types = {1},id = 2},{types = {1},id = 8}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T8()
  return {8,{2,1,10},{x = 1.0,y = 2.0,z = 6.0},{{types = {1},id = 2},{types = {1},id = 9}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T9()
  return {9,{2,1,11},{x = 1.0,y = 2.0,z = 7.0},{{types = {1},id = 2},{types = {1},id = 10}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
function T.T10()
  return {10,{2,1,12},{x = 1.0,y = 2.0,z = 8.0},{{types = {1},id = 2},{types = {1},id = 11}},1,"hero_chushi","chushi",{"防御"},"平原"}
end
local function table_read_only(t)
  local temp= {}
  local mt = {
    __index = t,
    __newindex = function(t, k, v)
        error('error write to a read-only table with key = ' .. tostring(k)..', value ='..tostring(v))
    end
  }
  setmetatable(temp, mt)
  return temp
end
local function New(data)
  local t = {}
  for k,v in pairs(TestTableArraysTemplateFieldsIndex) do
    t[k]= data[v]
  end
  return table_read_only(t)
end
local TestTableArraysTemplate = {
  Values = {}
}
---@return TestTableArrayTemplate
function TestTableArraysTemplate.GetTableByIndex(index)
  if TestTableArraysTemplate.Values[index]==nil then
   TestTableArraysTemplate.Values[index]=New(T['T'..index]())
  end
  return TestTableArraysTemplate.Values[index]
end
function TestTableArraysTemplate.GetLength()
 return 10
end
return TestTableArraysTemplate