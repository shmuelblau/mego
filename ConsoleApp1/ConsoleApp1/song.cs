using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class song
    {
        string name;
        string preformer;
        int length;
        song next;
        public song(string name, string preformer, int length)
        {
            this.name = name;
            this.preformer = preformer;
            this.length = length;

        }
        public  string stasus(string name)
        {
            return  preformer + "/" + name + ";"+length.ToString();

        }
        public void SetNext(song next) { this.next = next; }
        public string GetName() {  return name; }
        public string GetPreformer() {  return preformer; }
        public int GetLength() { return length; }

        public void SetName(string name) { this.name = name; }

        public void SetPreformer(string preformer) { this.preformer = preformer; }
        public void SetLength(int length) {  this.length = length; }









    }
}
