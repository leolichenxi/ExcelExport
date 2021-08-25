using System;
using System.Collections.Generic;
using FlatBuffers;

namespace ExampleFlat.Core
{
    
    public abstract class ConfigSingle <T,T1> :XObject where T : ConfigSingle<T,T1>,new() where T1:IFlatbufferObject,new()
    {
        public T1 Template { get; private set; }
        private static T _instance;
        public static T Instance {
            get
            {
                if (_instance == null)
                {
                    _instance = new T {InstanceName = typeof(T).Name};
                    var t1 = GeneratorUtility.Get<T1>(_instance.FilePath);
                    _instance.Init(t1);
                }
                return _instance;
            }
        }

        private void Init(T1 t)
        {
            Template = t;
            OnInit(t);
        }

        protected abstract void OnInit(T1 t);

        protected override void OnDispose()
        {
            _instance = null;
        }

        protected virtual string FilePath => "data_bin/" + typeof(T1).Name + ".bin";

        public static void Release()
        {
            if (_instance!=null)
            {
                _instance.Dispose();
            }
            _instance = null;
        }
    }

    public abstract class ConfigSingleExtend<T, T1,T2, K> : ConfigSingle<T,T1> where T : ConfigSingle<T, T1>, new()
        where T1 : IFlatbufferObject, new() 
        where T2 : IFlatbufferObject 
        where K : struct
    {
        
        protected override string FilePath => "data_bin/" + typeof(T2).Name + ".bin";
        private Dictionary<K, T2> _items;
        protected abstract K GetKey(T2 t);
        protected abstract int GetLength();
        protected abstract T2 GetTemplate(int index);
        
        protected override void OnInit(T1 t)
        {
            int length = GetLength();
            _items = new Dictionary<K, T2>(length);
            for (int i = 0; i < length; i++)
            {
                var template = GetTemplate(i);
                if (template != null)
                {
                    _items.Add(GetKey(template),template);
                }
            }
        }

        public bool TryGetTemplate(K id,out T2 v)
        {
            return _items.TryGetValue(id, out v);
        }
        
        public bool IsExists(K id) 
        {
            return _items.ContainsKey(id);
        }

        protected override void OnDispose()
        {
             base.OnDispose();
             if (_items != null)
             {
                 _items.Clear();
                 _items = null;
             }
        }
    }

    public abstract class ConfigDoubleExtend<T, T1, T2, K, K2> : ConfigSingle<T, T1>
        where T : ConfigSingle<T, T1>, new()
        where T1 : IFlatbufferObject, new()
        where T2 : IFlatbufferObject
        where K : struct
        where K2 : struct
    {
        private Dictionary<K, Dictionary<K2, T2>> _items;
        protected override void OnInit(T1 t)
        {
            int length = GetLength();
            _items = new Dictionary<K, Dictionary<K2, T2>>(length);
            for (int i = 0; i < length; i++)
            {
                var template = GetTemplate(i);
                K key1 = GetKey(template);
                K2 key2 = GetKey2(template);
                if (_items.ContainsKey(key1))
                {
                    if (_items[key1].ContainsKey(key2))
                        throw new Exception($"{key1},{key2} is already in {InstanceName}");
                    else
                        _items[key1].Add(key2, template);
                }
                else
                {
                    Dictionary<K2, T2> item = new Dictionary<K2, T2>();
                    item.Add(key2, template);
                    _items.Add(key1, item);
                }
            }
        }
        public bool TryGetTemplate(K key1, K2 key2,out T2 t)
        {
            if (_items.TryGetValue(key1,out Dictionary<K2,T2> dic))
            {
                if (dic.TryGetValue(key2,out  t))
                {
                    return true;
                }
            }
            t = default(T2);
            return false;
        }
        protected abstract K GetKey(T2 t);
        protected abstract K2 GetKey2(T2 t);
        protected abstract int GetLength();
        protected abstract T2 GetTemplate(int index);
    }
}