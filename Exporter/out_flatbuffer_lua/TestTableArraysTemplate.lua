-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: Config

local flatbuffers = require('flatbuffers')

local TestTableArraysTemplate = {} -- the module
local TestTableArraysTemplate_mt = {} -- the class metatable

function TestTableArraysTemplate.New()
    local o = {}
    setmetatable(o, {__index = TestTableArraysTemplate_mt})
    return o
end
function TestTableArraysTemplate.GetRootAsTestTableArraysTemplate(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = TestTableArraysTemplate.New()
    o:Init(buf, n + offset)
    return o
end
function TestTableArraysTemplate_mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function TestTableArraysTemplate_mt:Id()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Int32, o + self.view.pos)
    end
    return 0
end
function TestTableArraysTemplate_mt:Weapons(j)
    local o = self.view:Offset(6)
    if o ~= 0 then
        local a = self.view:Vector(o)
        return self.view:Get(flatbuffers.N.Int32, a + ((j-1) * 4))
    end
    return 0
end
function TestTableArraysTemplate_mt:WeaponsLength()
    local o = self.view:Offset(6)
    if o ~= 0 then
        return self.view:VectorLen(o)
    end
    return 0
end
function TestTableArraysTemplate_mt:Model()
    local o = self.view:Offset(8)
    if o ~= 0 then
        return self.view:String(o + self.view.pos)
    end
end
function TestTableArraysTemplate_mt:Icon()
    local o = self.view:Offset(10)
    if o ~= 0 then
        return self.view:String(o + self.view.pos)
    end
end
function TestTableArraysTemplate_mt:MachineType()
    local o = self.view:Offset(12)
    if o ~= 0 then
        return self.view:String(o + self.view.pos)
    end
end
function TestTableArraysTemplate_mt:MapType()
    local o = self.view:Offset(14)
    if o ~= 0 then
        return self.view:String(o + self.view.pos)
    end
end
function TestTableArraysTemplate.Start(builder) builder:StartObject(6) end
function TestTableArraysTemplate.AddId(builder, id) builder:PrependInt32Slot(0, id, 0) end
function TestTableArraysTemplate.AddWeapons(builder, weapons) builder:PrependUOffsetTRelativeSlot(1, weapons, 0) end
function TestTableArraysTemplate.StartWeaponsVector(builder, numElems) return builder:StartVector(4, numElems, 4) end
function TestTableArraysTemplate.AddModel(builder, model) builder:PrependUOffsetTRelativeSlot(2, model, 0) end
function TestTableArraysTemplate.AddIcon(builder, icon) builder:PrependUOffsetTRelativeSlot(3, icon, 0) end
function TestTableArraysTemplate.AddMachineType(builder, machineType) builder:PrependUOffsetTRelativeSlot(4, machineType, 0) end
function TestTableArraysTemplate.AddMapType(builder, mapType) builder:PrependUOffsetTRelativeSlot(5, mapType, 0) end
function TestTableArraysTemplate.End(builder) return builder:EndObject() end

return TestTableArraysTemplate -- return the module