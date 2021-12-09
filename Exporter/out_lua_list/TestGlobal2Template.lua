local TestGlobal2Template = {}
local TestGlobal2Template__mt = {
  TestFloat = 6.5
}
local TestGlobal2Template__mt__mt = {__index= TestGlobal2Template__mt,__newindex = function (t, k, v) error('error write to a read-only table with key = ' .. tostring(k)..', value ='..tostring(v)) end }
setmetatable(TestGlobal2Template,TestGlobal2Template__mt__mt)
return TestGlobal2Template