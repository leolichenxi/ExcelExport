using System;
using System.Text;

namespace ExampleFlat.Core
{
    public abstract class XObject : IDisposable
    {
        private bool mDisposed = false;
        public string InstanceName { get; set; }

        ~XObject()
        {
            if (!mDisposed)
                Dispose(false);
        }

        public void Dispose()
        {
            if (!mDisposed)
                Dispose(true);
        }

        private void Dispose(bool disposing)
        {
            if (disposing)
            {
                mDisposed = true;
                OnDispose();
                GC.SuppressFinalize(this);
            }
            else
            {
                StringBuilder sb = new StringBuilder();
                sb.AppendFormat("Memory leak!!!(Type: {0}), (Instance: {1})", this.GetType().ToString(), InstanceName);
                Console.WriteLine(sb.ToString());
            }
        }
        protected abstract void OnDispose();
    }
}