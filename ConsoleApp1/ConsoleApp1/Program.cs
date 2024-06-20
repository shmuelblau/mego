using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            song a = new song("aaa", "xxxx", 11);
            song b = new song("aaa", "xxxx", 11);
            song c = new song("aaa", "xxxx", 11);
            song d = new song("aaa", "xxxx", 11);
            song[] arr= new song[10];
            arr[0] = new song("aaaa", "aaaa", 0);
            for (int i = 1; i < 10; i++)
            {
                arr[i] =new song("aaaa","aaaa",i);
                

            }

        }
    }
}
