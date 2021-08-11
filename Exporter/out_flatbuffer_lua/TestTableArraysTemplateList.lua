-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: Config

local flatbuffers = require('flatbuffers')

local TestTableArraysTemplateList = {} -- the module
local TestTableArraysTemplateList_mt = {} -- the class metatable

function TestTableArraysTemplateList.New()
    local o = {}
    setmetatable(o, {__index = TestTableArraysTemplateList_mt})
    return o
end
function TestTableArraysTemplateList.GetRootAsTestTableArraysTemplateList(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = TestTableArraysTemplateList.New()
    o:Init(buf, n + offset)
    return o
end
function TestTableArraysTemplateList_mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function TestTableArraysTemplateList_mt:TestTableArrays(j)
    local o = self.view:Offset(4)
    if o ~= 0 then
        local x = self.view:Vector(o)
        x = x + ((j-1) * 4)
        x = self.view:Indirect(x)
        local obj = require('Config.TestTableArraysTemplate').New()
        obj:Init(self.view.bytes, x)
        return obj
    end
end
function TestTableArraysTemplateList_mt:TestTableArraysLength()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestTableArraysTemplateList.Start(builder) builder:StartObject(1) end
function TestTableArraysTemplateList.AddTestTableArrays(builder, testTableArrays) builder:PrependUOffsetTRelativeSlot(0, testTableArrays, 0) end
function TestTableArraysTemplateList.StartTestTableArraysVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestTableArraysTemplateList.End(builder) return builder:EndObject() end

return TestTableArraysTemplateList -- return the module