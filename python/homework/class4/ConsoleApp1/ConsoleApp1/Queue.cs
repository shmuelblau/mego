using Queue1;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Queue<T>
    {
        private Node<T> first;
        private Node<T> last;
        public Queue<int> combine(Queue<int> q1, Queue<int> q2)
        {
            Queue<int> q3 = new Queue<int>();
            while (!q1.IsEmpty() && !q2.IsEmpty())
            {
                if (q1.first.GetValue() > q2.first.GetValue())
                {
                    q3.Insert(q2.Remove());
                    q3.Insert(q1.Remove());
                }
                else
                {
                    q3.Insert(q1.Remove());
                    q3.Insert(q2.Remove());
                }
            }
            return q3;

        }
        public Queue()
        {
            this.first = null;
            this.last = null;
        }
        public void Insert(T x)
        {
            Node<T> temp = new Node<T>(x);
            if (first == null)
                first = temp;
            else
                last.SetNext(temp);
            last = temp;
        }
        public T Remove()
        {
            T x = first.GetValue();
            first = first.GetNext();
            if (first == null)
                last = null;
            return x;
        }
        public T Head()
        {
            return first.GetValue();
        }
        public bool IsEmpty()
        {
            return first == null;
        }
        public override string ToString()
        {
            if (this.IsEmpty()) return "[]";
            Queue<T> temp = new Queue<T>();
            while (!this.IsEmpty())
                temp.Insert(this.Remove());
            string s = "[";
            while (!temp.IsEmpty())
            {
                s = s + temp.Head() + ',';
                this.Insert(temp.Remove());
            }
            s = s.Substring(0, s.Length - 1) + "]";
            return s;
        }
    }

}
