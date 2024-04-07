import random


class time:
    
    def __init__(self,hour,minutes):
        self.hour = hour
        self.minutes = minutes
        
    def difference(self,other):
         
        diff=int((other.hour*60 + other.minutes)-(self.hour*60 + self.minutes))
        return diff
        
def bdika(arr):
    a=time(arr[0],arr[1])
    b=time(arr[2],arr[3])
    if a.difference(b) < 180:
        return "המשלוח הגיע בזמן"
    else:
        return "המשלוח התעכב יותר מדי"
    


deli=[i for i in range(100)]
for i  in range(len(timea)):
    deli[i]=[random.randint(0,24),random.randint(0,60),random.randint(0,24),random.randint(0,60)]
print(deli)
for i in range(100):
    print(bdika(deli[i]))

