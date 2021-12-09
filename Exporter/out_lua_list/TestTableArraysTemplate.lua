---@type TestTableArraysTemplate
local Filed_Dic ={
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
local T = {}
function T.T1()
  return {1,2,1,3,{x = 1.0,y = 2.0,z = 3.0},1,"hero_chushi","chushi",""}
end
function T.T2()
  return {2,2,1,4,{x = 1.0,y = 2.0,z = 3.0},{2},{1,3},1,"hero_chushi","chushi","防御","平原"}
end
function T.T3()
  return {3,2,1,5,{x = 1.0,y = 2.0,z = 3.0},{1,2},{1,4},1,"hero_chushi","chushi","防御","平原"}
end
function T.T4()
  return {4,2,1,6,{x = 1.0,y = 2.0,z = 3.0},{0},{0},1,"hero_chushi","chushi","防御","平原"}
end
function T.T5()
  return {5,2,1,7,{x = 1.0,y = 2.0,z = 3.0},{1,2},{1,6},1,"hero_chushi","chushi","防御","平原"}
end
function T.T6()
  return {6,2,1,8,{x = 1.0,y = 2.0,z = 4.0},{1,2},{1,7},1,"hero_chushi","chushi","防御","平原"}
end
function T.T7()
  return {7,2,1,9,{x = 1.0,y = 2.0,z = 5.0},{1,2},{1,8},1,"hero_chushi","chushi","防御","平原"}
end
function T.T8()
  return {8,2,1,10,{x = 1.0,y = 2.0,z = 6.0},{1,2},{1,9},1,"hero_chushi","chushi","防御","平原"}
end
function T.T9()
  return {9,2,1,11,{x = 1.0,y = 2.0,z = 7.0},{1,2},{1,10},1,"hero_chushi","chushi","防御","平原"}
end
function T.T10()
  return {10,2,1,12,{x = 1.0,y = 2.0,z = 8.0},{1,2},{1,11},1,"hero_chushi","chushi","防御","平原"}
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
  for k,v in pairs(Filed_Dic) do
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