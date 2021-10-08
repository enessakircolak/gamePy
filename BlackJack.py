

import random

class croupier:
    def __init__(self,cards):
        self.cards = cards
        self.tableHand = []
        self.playerHand = []
        self.card = []
        self.draw = 4
        print("Croupier shuffle !!!")
    
    def drawCard(self):
        self.card = self.cards[(self.draw)]
        self.draw += 1
        return self.card
    
    def start(self):
        self.playerHand = self.cards[2:4]
        self.tableHand = self.cards[0:2]
        return 

    def table(self):
        self.tableHand 
        return self.tableHand
    
    def player(self):
        self.playerHand 
        return self.playerHand
    
    def position(self):
        print(f"Table Hand =  {game.table()[0]}  ?")
        print(f"Player Hand =  {game.player()}  ")
        

class BlackJack:
    def __init__(self):
        #self.play = play
        #self.ctrl = []
        #self.number = 0
        game.start()
        game.position()
        self.ctrl = Check(game.playerHand) 
        self.number = self.ctrl.sum()
        print(self.number)
        
    def tabeltake(self):
        game.tableHand.append(game.drawCard())
        return game.tableHand
    def take(self):
        game.playerHand.append(game.drawCard())
        return game.playerHand
    
    def showTime(self):
        while True:
            print("\n")
            decision = input("Do you want a card ? (yes=Y , no = N) = ")
            print("\n")
            if decision == "N" or decision == "n":             
                break
          
            elif decision == "Y" or decision == "y" :
                
                oyna.take()
                game.position()
                #self.ctrl = Check(game.playerhand)
                self.number = self.ctrl.sum()
                print(f"Total = {self.number}")
                if self.number > 21 :
                    print("End of the game  :'( ")
                    break    
        return self.number
    

class Check:
    def __init__(self , hand):
        self.hand = hand 
        self.total = 0
        self.ctrl = 0
        self.ctrlA = 0
        self.ctrlT = []
        self.masa = 0
    def sum(self):
        self.total = 0
        self.ctrlA = 0
        for i in self.hand:
            
            if type(i) == int :
                self.total += i 
            elif i == "J":
                self.total += 10
            elif i == "Q":
                self.total += 10
            elif i == "K":
                self.total += 10
            elif i == "A":
                self.ctrlA += 1
        if self.total > 10 :
            for i in range (0,self.ctrlA):
                self.total += 1
        elif self.total < 11 and self.ctrlA > 0 :
            self.total += 11
            self.total += (self.ctrlA) - 1

                        
        
        return self.total

    def tableSum(self):
        while True:
            self.ctrlT = Check(game.tableHand)
            self.masa = self.ctrlT.sum()
            
            if self.masa <= 16:
                oyna.tabeltake()
            elif self.masa > 16:      
                break
        return self.masa

    def Final(self):
        a = playerctrl.sum()
        b = tablectrl.sum()

        if a > 21 and b > 21 :
            print("draw")      
        elif a == b :
            print("draw") 
        elif a > 21:
            print("table win")
        elif b > 21 :
            print("player win")       
        elif a > b:
            print("player win")                 
        else:
            print("table win")
        
        print("!!!!!!!")
        print("\n")
                      
        #compare
                          
while True:               
    cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]*4
    random.shuffle(cards)
    
    game = croupier(cards)

    #oyun = 2 
    oyna = BlackJack()
    oyna.showTime()

    
    playerctrl = Check(game.playerHand)
    tablectrl = Check(game.tableHand)
    tablectrl.tableSum()
    print(f"Player = {game.playerHand} = {playerctrl.sum()}")
    print(f"Table = {game.table()} = {tablectrl.tableSum()} ")
    playerctrl.Final()
    
    





