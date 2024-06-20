def a (n):
    def b (n,result):

        if len(n)<2:
            return result and True
        if type(n[0])!=type(n[-1]):
            return False
        if type(n[0])== int:
            return b(n[1:-1],result) and n[0]==n[-1]
        if type(n[0])== float:
            return b(n[1:-1],result) and n[0]==n[-1]
        if type(n[0]) == list or type(n[0]) ==tuple or(type(n[0]) ==str and len(n[0])>1):
            return b(n[1:-1],result)and b(list(n[0]+n[-1])[1:-1],result) and list(n[0]+n[-1])[0]==list(n[0]+n[-1])[-1]
        if type(n[0]) == str:
            return  n[0] == n[-1]
    return b(n,True)
s=["abc",(5.6,1.2),1,(2,1),'g',[2,'k'],['k',2],'g',(1,2),1,(1.2,5.6),"cba"]
print(a(s))




