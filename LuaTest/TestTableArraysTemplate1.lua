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
  born_position = {0,Position3dFieldsIndex},
  TestTypes = {1,TestType_FieldsIndex},
}
local T = {}
function T.T1()
  return {1,{2,1,3},nil,nil,1,"hero_chushi","chushi",nil,"222.0"}
end
function T.T2()
  return {2,{2,1,4},nil,{{nil,2},{{1},3}},1,"hero_chushi","chushi",{"防御"},"平原"}
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
local function New(data,tableIndexes)
  local t = {}
  for k,v in pairs(tableIndexes) do
    local c = TestTableArraysTemplateCustom[k]
    local d = data[v]
    if c == nil then
      t[k]= d
    else
      if c[1] == 1 then
        local t_c = {}
        for index = 1,#d do
          table.insert(t_c, New(d[index],c[2]))
        end
        t[k] = t_c
      else
        t[k] = New(d,c[2])
      end
    end
  end
  return table_read_only(t)
end
local TestTableArraysTemplate = {
  Values = {}
}
---@return TestTableArrayTemplate
function TestTableArraysTemplate.GetTableByIndex(index)
  if TestTableArraysTemplate.Values[index]==nil then
    TestTableArraysTemplate.Values[index]=New(T['T'..index](),TestTableArraysTemplateFieldsIndex)
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