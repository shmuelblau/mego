using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Queue1
{
    class Program
    {
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
	   static void Main(string[] args)
	   {
		  int[] v = new int[] { 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4 };
		  int[] h = new int[] { 7, 7, 1, 6, 8 };
		  int[] d = new int[] { 9, 3, 4, 5 };
		  int[] j = new int[] { };
		  Node<int> l = CreateList(v);
		  Console.WriteLine(l);
		  Console.WriteLine(CreateList(h));
		  Console.WriteLine(CreateList(d));
		  Console.WriteLine(CreateList(j));
	   }
    }
}



