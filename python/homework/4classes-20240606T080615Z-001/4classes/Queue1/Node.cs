using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Queue1
{
    class Node<T>
    {
        private T value;
        private Node<T> next;
        public Node(T value)        //  constractor 
        {
            this.value = value;
            this.next = null;
        }
        public Node(T value, Node<T> next)        //  constractor 
        {
            this.value = value;
            this.next = next;
        }
        public T GetValue()
        {
            return this.value;
        }
        public Node<T> GetNext()
        {
            return this.next;
        }
        public bool HasNext()
        {
            return (this.next != null);
        }
        public void SetValue(T value)
        {
            this.value = value;
        }
        public void SetNext(Node<T> next)
        {
            this.next = next;
        }
        public string Tostring1()
        {
            return this.value + "-->" + this.next;
        }
        public override string ToString()
        {
            string s = "";
            Node<T> temp = this;
            while (temp != null)
            {
                s = s + temp.GetValue() + "  ";
                temp = temp.GetNext();
            }
            return s;
        }
    }
}

