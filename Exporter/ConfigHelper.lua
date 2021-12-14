---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by lichenxi02.
--- DateTime: 2021/12/14 16:54
---

function table_read_only(t)
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

function New_Config(data,tableIndexes,customs)
  local t = {}
  for k,v in pairs(tableIndexes) do
     local c = customs[k]
     local d = data[v]
     if c == nil then
        t[k]= d
     else
       if c[1] == 1 then
          local t_c = {}
          for index = 1,#d do
              table.insert(t_c, New_Config(d[index],c[2],customs))
          end
          t[k] = t_c
       else
          t[k] = New_Config(d,c[2],customs)
       end
     end
  end
  return table_read_only(t)
end