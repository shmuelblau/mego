import pygame
import random
def check_won(board):
    a=0
    for i in range(26):
        if board[i] > 0:
            a += 1
            break
    for i in range(26):
        if board[i] < 0:
            a += 1
            break
    if a > 1:
        return False
    return True
def check(board, player, dice, loc, ifempty = True):
    if ifempty and board[(player % 2) * 25] != 0 and (player % 2) * 25 != loc:
        return "You have  game pieces out"
    if dice == 0:
        return False
    if loc > 25:
        return "Type a number between 0 and 25"
    if player % 2 == 0:
        if board[loc] < 1:
            return "You have no game pieces in place"
        if loc + dice < 25 and board[loc + dice] < -1:
            return "The position is occupied by the other player"
        if loc+dice > 24:
            c = 0
            for i in range(0,19):
                if board[i] > 0:
                    c += 1
            if c > 0:
                return "You can't take out before you put everything in the house"
    else:
        if board[loc] > -1 :
            return "You have no game pieces in place"
        if loc - dice > 0 and board[loc-dice] > 1:
            return "The position is occupied by the other player"
        if loc - dice < 1:
            c = 0
            i = 0
            for i in range(7,25):
                if board[i] < 0:
                    c += 1
            
            if c > 0:
                return "You can't take out before you put everything in the house"
            

    return True
def ispossibie(board,player,dice):
    
        for j in range(4):
            if dice[j] > 0:
                i = 0
                while i < 26 :
                     if check(board,player,dice[j],i) == True:
                    
                        return True
                     i += 1
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
            board[loc] += 1
        else:
            if board[loc-dice] == 1:
                board[loc-dice] -= 1
                board[0] += 1
                
            board[loc] += 1
            board[loc-dice] -= 1
           
    return board
def throwing():
    dice = [0,0]
    
    dice[0] = random.randint(1,6)
    dice[1] = random.randint(1,6)
    dices = [dice[0],dice[1],0,0]
    if dice[1] == dice[0]:
       dices[2] = dice[1]
       dices[3] = dice[1]
    return dices




def print_sirkel_0(loc):
    pygame.draw.circle(screen,[0,200,100],[loc[0],loc[1]],15)
def print_sirkel_1(loc):
    pygame.draw.circle(screen,[255,255,255],[loc[0],loc[1]],15)
    
def print_dice(dices):
    dice = [0] * 6
    dice[0] = pygame.image.load('dice1.jpg')
    dice[1] = pygame.image.load('dice2.jpg')
    dice[2] = pygame.image.load('dice3.jpg')
    dice[3] = pygame.image.load('dice4.jpg')
    dice[4] = pygame.image.load('dice5.jpg')
    dice[5] = pygame.image.load('dice6.jpg')
    
    loc=[200,520]
    for i in range(4):
        if dices[i] > 0:
            screen.blit(dice[dices[i]-1],loc)
        loc[0] += 80
    pygame.display.flip()
    

def printr(board,dices):
    #Receives a board and printer
    screen.fill((0, 0, 0))
    x  =[0]*len(board)
    for i in range(len(board)):
        x[i]=board[i]
    
    screen.blit(img,(0,0))
    
    loc=[20,20]
    for i in range(1,13):
        loc[1]=20
        if x[i]>0:
            
            j=x[i]
            while(j>0):
                print_sirkel_0(loc)
                loc[1]+=40
                j-=1
            
        if loc[0]==220:
            loc[0]+=20
        loc[0]+=40
        
    loc=[20,20]
    for i in range(1,13):
        loc[1]=20
        if x[i]<0:
            
            j=x[i]
            while(j<0):
                print_sirkel_1(loc)
                loc[1]+=40
                j+=1
            
        if loc[0]==220:
            loc[0]+=20
        loc[0]+=40
     
    loc=[480,480]
    for i in range(13,25):
        
        loc[1]=480
        if x[i]>0:
            
            j=x[i]
            while(j>0):
                print_sirkel_0(loc)
                loc[1]-=40
                j-=1
            
        loc[0]-=40
        if loc[0]==240:
            loc[0]-=20
    
    loc=[480,480]
    for i in range(13,25):
        
        loc[1]=480
        if x[i]<0:
            
            j=x[i]
            while(j<0):
                print_sirkel_1(loc)
                loc[1]-=40
                j+=1
            
        loc[0]-=40
        if loc[0]==240:
            loc[0]-=20
            
    loc=[250,230]  
    
    if x[0]>0:
        for i in range(x[0]):
           print_sirkel_0(loc)
           loc[1]-=40
           x[0]-=1
    
    loc=[250,270]  
    
    if x[25]<0:
        i=x[25]
        while(i<0):
           print_sirkel_1(loc)
           loc[1]+=40
           i+=1
            
    print_dice(dices)
            
    pygame.display.flip()

def Click_loc(loc):
        
    j=0
    for i in range(1,13):
        if loc[0]>j and loc[0]<(j+40) and loc[1]<200:
            return i
        
        j+=40
        if j ==240 :
            j+=20
        
    j=500
    for i in range(13,25):
        if loc[0]<j and loc[0]> (j-40) and loc[1]>300 and loc[1]<500:
            return i
        j-=40
        if j == 260:
            j-=20
    
    if loc[0]<260 and loc[0]>240 and loc[1]<250:
        return 0
    if loc[0]<260 and loc[0]>240 and loc[1]>250 and loc[1]<500:
        return 25
    j=200
    for i in range(4):
        if loc[0] > j and loc[0] < j+50 and loc[1]>520 and loc[1]<560:
            return i+100
        j+=80


pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 640
IMAGE='shesh.jpg'


size=(WINDOW_WIDTH,WINDOW_HEIGHT)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Game")
img=pygame.image.load(IMAGE)
clock=pygame.time.Clock()

board=[0,2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2,0]
#board=[0]*26
player=0
choices=[200,200]
dices=throwing()
print(dices)

finish=True
while finish:
    printr(board,dices)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish=False
            

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
             choices.append(Click_loc(pygame.mouse.get_pos()))
             
             choices.pop(0)
             print(choices,"a")
             

    
    if  check_won(board):
        
        break
    
    if sum(dices)==0:
        print("kkk")
        player+=1
        dices=throwing()
        print(dices)
        print(player)

    if  ispossibie(board,player,dices):
        pass
    else:
        print('sss')
        
        dices=[0]*4
        
        
    # if board[(player%2)*25] !=0:
    #     if choices[0]!=None and choices[1]!=None and choices[0] > 99 and choices[0]<104 and choices[1] >-1 and choices[1] < 26 :
    #         choices[1]=player%2*25
        
     
    if choices[0]!=None and choices[1]!=None and choices[0] > 99 and choices[0]<104 and choices[1] >-1 and choices[1] < 26 :
        if check(board,player,dices[choices[0]-100],choices[1]) == True:
            board=transfer(board,player,dices[choices[0]-100],choices[1])
            print(12)
            dices[choices[0]-100]=0
        
             



   # printr(board,dices)        
    
    
        
    
        
    
   # Click_loc()
    clock.tick(60)
    

