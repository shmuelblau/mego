using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Text;

namespace Queue1
{
    class Program
    {
        static int aaa(int x,int y)
        {
            int sum = 0;
            int s = 0;
            while (x > 0)
            {
                sum = sum + (x%2<<s)*y;
                x=x>>1;
                s ++;

            }
            return sum;
        }
        static void aaa2(int x,int y)
        {
            Stack<int> stack = new Stack<int>();
            while (x > 0)
            {
                stack.Push(x%y);
                x=x/y; 
            }
            while (!stack.IsEmpty())
            {
                Console.Write(stack.Pop());
            }
        }
        static Node<int> CreateList(int[] x)
        {
            if (x.Length > 0)
            {
                Node<int> a = new Node<int>(x[0]);
                Node<int> b = a;
                for (int i = 1; i < x.Length; i++)
                {
                    b.SetNext(new Node<int>(x[i]));
                    b = b.GetNext();
                }
                return a;
            }
            return null;
        }

        static bool iscorect(string x)
        {
            Stack<char> stack = new Stack<char>();
            for (int i = 0; i < x.Length; i++)
            {
                char c = x[i];
                if (c == '(' || c == '[' || c == '{') ;
                    stack.Push(c);


                if (c == ')')
                {
                    if (stack.Pop() != '(') ;
                        return false;
                }
                if (c == ']')
                {
                    if (stack.Pop() != '[') ;
                        return false;
                }
                if (c == '}')
                {
                    if (stack.Pop() != '{') ;
                       return false;
                }





            }
            return true;    

        }
        static void Main(string[] args)
        {
            aaa2(21, 4);
            
        }
    }
}





