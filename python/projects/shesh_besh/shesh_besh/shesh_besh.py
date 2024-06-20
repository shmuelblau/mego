import random
def Printer(board):
    print('\n    ','▬'*41)
    for i in range(1,9):
        print('    ▌', end = '')
        for j in range(12,0,-1):
            piece = board[j]
            if(piece > 0 and piece >= i):
                print(' ● ', end = '')
            elif(piece < 0 and -piece >= i):
                print(' ○ ', end = '')
            else:
                print('   ', end = '')
            if j == 7:
                print('▐', end = '')
                if -board[0] >= i:
                    print(' ○ ▌', end = '')
                else:
                    print('   ▌', end = '')
        print('▐')
    i = j = 0
    for i in range(6,0,-1):
        print('    ▌', end = '')
        for j in range(13,25):
            piece = board[j]
            if(piece > 0 and piece >= i):
                print(' ● ', end = '')
            elif(piece < 0 and -piece >= i):
                print(' ○ ', end = '')
            else:
                print('   ', end = '')
            if j == 18:
                print('▐', end = '')
                if board[25] >= i:
                    print(' ● ▌', end = '')
                else:
                    print('   ▌', end = '')
        print('▐')
    print("")
def throwing():
    dice=[0,0]
    
    dice[0] = random.randint(1,6)
    dice[1] = random.randint(1,6)
    dices = [dice[0],dice[1],0,0]
    if dice[1] == dice[0]:
       dices[2] = dice[1]
       dices[3] = dice[1]
    return dices

def check_won(board):
    
    for i in range(26):
        if board[i] > 0:
            for j in range(26):
                if board[j]<0:
                    return False
                
    return True
def check(board,player,dice,loc):
    if loc > 25:
        return "Type a number between 0 and 25"
    if player % 2 == 0:
        if board[loc] < 1:
            return "You have no game pieces in place"
        if board[loc+dice]<-1:
            return "The position is occupied by the other player"
        if loc+dice > 24:
            c=0
            for i in (0,19):
                if board[i] > 0:
                    c += 1
            if c > 0:
                return "You can't take out before you put everything in the house"
    else:
        if board[loc] >- 1 :
            return "You have no game pieces in place"
        if board[loc-dice] > 1 :
            return "The position is occupied by the other player"
        if loc-dice < 1:
            c=0
            for i in (7,25):
                if board[i] > 0:
                    c += 1
            if c > 0:
                return "You can't take out before you put everything in the house"
            

    return True
def ispossibie(board,player,dice,choices):
    
    for j in range(4):
        if choices[j] == 1:
            i=0
            while i < 26 :
                 if check(board,player,dice[j],i) == True:
                    
                    return True
                 i+=1
    return False        
   
def transfer(board,player,dice,loc):
    if player % 2 == 0:
        if dice+loc > 24:
            board[loc] -= 1
            
        else:
            if board[loc+dice] == -1:
                board[loc+dice] += 1
                board[25] -= 1
                
            board[loc] -= 1
            board[loc+dice] += 1
            #
            print(board[loc+dice])
    else:
        if loc-dice < 1:
            board[loc]+=1
        else:
            if board[loc-dice] == 1:
                board[loc-dice]-=1
                board[0]+=1
                
            board[loc]+=1
            board[loc-dice]-=1
           
    return board

#board=[0,2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2,0]
board=[0,2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2,0]
player=0
dice=[0,0]
choices=[1,1,0,0]
Printer(board)

while True:
    
    dice = [0,0]
    dice[0] = random.randint(1,6)
    dice[1] = random.randint(1,6)
    choices = [1,1,0,0]
    if dice[1] == dice[0]:
        choices[2] = 1
        choices[3] = 1
        dice = [dice[0]] * 4
    print("player: {}   Your dice are: {} {}".format(player%2,dice[0],dice[1]))
    
    while True:
        if board[(player%2)  *25] != 0 :
             if ispossibie(board,player,dice,choices) == False:
                
                break 
             
             choiceply = int(input("you have a game pieces out enter namber dice to play"))
             if check(board,player,dice[choiceply],(player%2)*25) == True:
                board = transfer(board,player,dice[choiceply],(player%2)*25)
                choices[choiceply] = 0
                #
                print("buzha")
             else:
                 print(check(board,player,dice[choiceply],(player%2)*25))
        else:
            break
        
           
    
    while True:    
        
        if ispossibie(board,player,dice,choices) == False:
            
            break
        
        while True:  
            
            choiceply=int(input("Type the number of the dice you want to play with"))
            if (choiceply >-1 and choiceply<4) and choices[choiceply]!= 0 :
                break
            
        loc=int(input("Where do you want to insert the number {}".format(dice[choiceply])))
        if check(board,player,dice[choiceply],loc) == True:
            board=transfer(board,player,dice[choiceply],loc)
            choices[choiceply]=0
            #
            print("buzha")
        else:
            print(check(board,player,dice[choiceply],loc))
        if sum(choices)==0:
            break
       
    Printer(board)
    if check_won == False:
        print("player namber {} won!!!".format(player%2))
        break
    player+=1
                
      
    



























        
    
     
        
    
            
