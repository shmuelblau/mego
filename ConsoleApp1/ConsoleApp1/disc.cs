using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class disc
    {
        string discName;
        song[] songs;
        public disc(string discName, song[] songs)
        {
            this.discName = discName;
            this.songs = songs;
        }

        public bool Exist(string nSong, string pSong )
        {
            for (int i = 0; i < songs.Length; i++)
            {
                if (songs[i].GetName() == nSong)
                    if (songs[i].GetPreformer() == pSong)
                        return true;
            }
            return false;
        }


    }
        
        
}
