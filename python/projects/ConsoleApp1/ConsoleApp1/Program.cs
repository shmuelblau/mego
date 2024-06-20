using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        public static int What( int num)
        {
            if (num == 1) 
                return 1;

            int sum = num;
            for (int i = 1; i < num; i++)
            {
                Console.WriteLine(i+"lol");
                sum= sum + What(i);
            }
            Console.WriteLine(sum);
            return sum;
        }
            


        static void Main(string[] args)
        {
            What(4);





            

            

            

        }
    }
}
