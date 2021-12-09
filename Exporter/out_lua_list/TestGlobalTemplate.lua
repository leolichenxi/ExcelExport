local TestGlobalTemplate = {}
local TestGlobalTemplate__mt = {
  TestInt = 7,
  TestStringArrays = {
    "哈",
    "哈哈",
    "哈哈1"
  },
  TestString1 = 1.1111111111111112e+131,
  TestString = "哈\\哈\n哈",
  TestFloat = 6.5,
  TestDouble = 7.852,
  TestBool = true,
  TestIntArrays = {
  },
  TestFloatArrays = {
    1.2,
    1.8,
    2.0
  },
  TestDoubleArrays = {
    1.21,
    1.81,
    2.01
  },
  TestBoolArrays = {
    true,
    false,
    true,
    false
  },
  TestObj = {
    a = 1,
    b = 2.02,
    c = true
  },
  TestObj1 = {
    a = 1,
    bs = {
      2.0,
      2.0,
      3.0,
      4.0
    },
    v = true
  },
  TestObjArrays = {
    {
      a = 1,
      b = 2,
      c = 0
    },
    {
      a = 1,
      b = 10,
      c = 1
    }
  },
  TestObjArray1s = {
    {
      a = 1,
      bs = {
        2.0,
        2.0,
        3.0,
        4.0
      }
    },
    {
      a = -1,
      bs = {
        2.0,
        2.0
      }
    }
  },
  TestDefineFromGlobal = {
    x = 1.0,
    y = 2.0,
    z = 3.0
  },
  TestDefineFromGlobal2s = {
    {
      x = 1.0,
      y = 2.0,
      z = 3.0
    },
    {
      x = 2.0,
      y = 2.0,
      z = 10.0
    }
  },
  TestCustomObj = {
    xs = {
      1.0,
      2.0
    },
    ys = {
      2.0,
      6.0
    },
    zs = {
      3.0
    }
  },
  TestCustomObjArrays = {
    {
      xs = {
        1.0,
        2.0
      },
      ys = {
        2.0,
        6.0
      },
      zs = {
        3.0
      }
    },
    {
      xs = {
        2.0
      },
      ys = {
        5.0
      },
      zs = {
        10.0,
        12.0
      }
    }
  },
  Test1Int = 7,
  TestInt1 = 7
}
local TestGlobalTemplate__mt__mt = {__index= TestGlobalTemplate__mt,__newindex = function (t, k, v) error('error write to a read-only table with key = ' .. tostring(k)..', value ='..tostring(v)) end }
setmetatable(TestGlobalTemplate,TestGlobalTemplate__mt__mt)
return TestGlobalTemplate