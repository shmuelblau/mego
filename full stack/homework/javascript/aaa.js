let nam="";
let ans = 0
console.log(calculet(nam))




let s =[1,2,3,4,5,6,7,8,9,'+','-','x','%','0','.','(',')'];
function calculet(str){
    if(str==""){return 0}
    for(let i =0;i<str.length;i++){
        if(str[i]=='-'){
            if(str[i+1]=='-'){
                str=str.slice(0,i)+'+'+str.slice(i+2)
            }
            if(str[i+1]=='+' ){
                str=str.slice(0,i)+'-'+str.slice(i+2)
            }
            if(str[i-1]=='+' ){
                str=str.slice(0,i-1)+'-'+str.slice(i+1)
            }


        }
    }
    let r=0
    let l=0
    
    for(let x = 0; x < str.length; x++){
       if(str[x]=='('){
          l=x 
        }
       if(str[x]==')'){
          r=x
          break;
       }

    }
    if (r!=0){
        return calculet(str.slice(0,l)+String(calculet(str.slice(l+1,r))) +str.slice(r+1))
    }
    for (let i=str.length-1;i>0;i--){
        
        if (str[i]=='-'){
            return calculet(str.slice(0,i))+calculet(str.slice(i+1))*-1
        }
        if (str[i]=='+'){
            return calculet(str.slice(0,i))+calculet(str.slice(i+1))
        }
    }
    for (let i=0; i<str.length;i++){
        if (str[i]=='x'){
            return calculet(str.slice(0,i))*calculet(str.slice(i+1))
        }
        if (str[i]=='%'){
            return calculet(str.slice(0,i))/calculet(str.slice(i+1))
        }
        
    }
    return parseFloat(str)
}

for(let i of s ){
    
    document.getElementById('n'+i).onclick=function(){
        nam+=i
        document.getElementById("aaa").innerHTML=nam;
    }

}
        document.getElementById('nd').onclick=function(){
            
            nam=nam.slice(0,-1)
            document.getElementById("aaa").innerHTML=nam;
        }
        document.getElementById('nc').onclick=function(){
            nam=''
            document.getElementById("aaa").innerHTML=nam;
        }
        document.getElementById('na').onclick=function(){
            nam+=ans.toString()
            document.getElementById("aaa").innerHTML=nam;
        }
        document.getElementById('n=').onclick=function(){
            ans=calculet(nam)
            nam =nam + '=' + ans
            document.getElementById("aaa").innerHTML=nam;
            nam=''
        }



            