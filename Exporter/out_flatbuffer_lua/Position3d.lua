-- automatically generated by the FlatBuffers compiler, do not modify

-- namespace: 

local flatbuffers = require('flatbuffers')

---@class Position3d : Position3d__mt 
 local Position3d = {} -- the module
 ---@class Position3d__mt 
 local Position3d_mt = {} -- the class metatable
 
function Position3d.New()
    local o = {}
    setmetatable(o, {__index = Position3d_mt})
    return o
end
function Position3d.GetRootAsPosition3d(buf, offset)
    if type(buf) == "string" then
        buf = flatbuffers.binaryArray.New(buf)
    end
    local n = flatbuffers.N.UOffsetT:Unpack(buf, offset)
    local o = Position3d.New()
    o:Init(buf, n + offset)
    return o
end
function Position3d_mt:Init(buf, pos)
    self.view = flatbuffers.view.New(buf, pos)
end
function Position3d_mt:X()
    local o = self.view:Offset(4)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float32, o + self.view.pos)
    end
    return 0.0
end
function Position3d_mt:Y()
    local o = self.view:Offset(6)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float32, o + self.view.pos)
    end
    return 0.0
end
function Position3d_mt:Z()
    local o = self.view:Offset(8)
    if o ~= 0 then
        return self.view:Get(flatbuffers.N.Float32, o + self.view.pos)
    end
    return 0.0
end
function Position3d.Start(builder) builder:StartObject(3) end
function Position3d.AddX(builder, x) builder:PrependFloat32Slot(0, x, 0.0) end
function Position3d.AddY(builder, y) builder:PrependFloat32Slot(1, y, 0.0) end
function Position3d.AddZ(builder, z) builder:PrependFloat32Slot(2, z, 0.0) end
function Position3d.End(builder) return builder:EndObject() end

return Position3d -- return the module