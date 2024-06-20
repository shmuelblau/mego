import random
def GetWords(nam):
    #Receives a number and returns an array that contains a number of words retrieved from the file
    file=open("wordlist.text",'r')
    test=file.read()
    ollwords=test.split()
    words=[]
    for i in range(nam):
        words.append(ollwords[random.randint(0,len(ollwords))])
    return words

def GetCauntWords():
    #Returns a number
    while True:
        nam=input("Type the number of words")
        if nam.isdigit():
            nam=int(nam)
            break
    return nam
def GetLetter(Player):
    #Receives a player's name and asks him to enter a letter, checks for correctness and returns
    while True:
        letter=input(Player+"  Please type a letter to guess")
        if len(letter)==1 and('a' <= letter <= 'z' or 'A'<= letter <= 'Z'):
            break
    return letter.lower()
def Players():
    #Requests a number of players and their name and returns in an array
    NanesOfPlayers=[]
    while True:
        nam=input("Type the number of players")
        if nam.isdigit():
            nam=int(nam)
            break
    for i in range(nam):
        name=input(f"Type the player's name: {i+1}")
        NanesOfPlayers.append(name)
    return NanesOfPlayers


def StartGame(NamesOfPlayers,words):
    #Receives arrays of words and player names and activates the game
    print("Let's start playing!!!")
    namberOfPlayers = len(NamesOfPlayers)
    PlayersScore =[0]*len(NamesOfPlayers)
    Counter = 0
    for word in words:

        FollWord=[i for i in word]
        CodedWord=['x']*len(word)
        print(FollWord)
        print(CodedWord)



        while FollWord != CodedWord:

            Guess = GetLetter(NamesOfPlayers[Counter % namberOfPlayers])
            for i in range(len(FollWord)):
                if Guess == FollWord[i]:

                    CodedWord[i] = FollWord[i]
                    PlayersScore[Counter % namberOfPlayers] += 1
                    print(f"You guessed the letter: {Guess}  correctly the word right now is: {''.join(CodedWord)}")

            print(f"the word right now is: {''.join(CodedWord)}")

            Counter+=1
        print("The word is fully understood")
    big=0
    for i in range( len(PlayersScore)):
        if PlayersScore[i]> PlayersScore[big]:
            big=i
    print(f"The winning player is: {NamesOfPlayers[big]}")
def Game():
    #Asks for a number of players and their names,
    #asks for a number of words and gets them, calls the game function with these variables
    names=Players()
    words=GetWords(GetCauntWords())
    StartGame(names,words)


Game()





