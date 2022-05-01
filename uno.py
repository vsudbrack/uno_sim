import numpy as np
import random as rd

class Card:
    def __init__(self, number, color):
        self.color = color
        self.number = number

    def __repr__(self):
        return "%s-%d"%(self.color, self.number)
    
    def __eq__(self, other):
        if((self.color == other.color) and (self.number == other.number)): return True
        else: return False

class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.insert(0, card)

    def read(self, num):
        return self.cards[num]

    def get_rnd(self):
        return self.cards.pop(rd.randint(0, self.len()-1))

    def get_top(self):
        return self.cards.pop(0)

    def len(self):
        return len(self.cards)

    def shuffle(self):
        rd.shuffle(self.cards)

    def play_by_color(self, turn_card):
        for my_card in self.cards:
            if( my_card.color == turn_card.color):
                self.cards.remove(my_card)
                return my_card

        for my_card in self.cards:
            if( my_card.number == turn_card.number):
                self.cards.remove(my_card)
                return my_card
        
        return (False) # Blocked

    def play_by_number(self, turn_card):
        for my_card in self.cards:
            if( my_card.number == turn_card.number):
                self.cards.remove(my_card)
                return my_card
        
        for my_card in self.cards:
            if( my_card.color == turn_card.color):
                self.cards.remove(my_card)
                return my_card

        return (False) # Blocked    

def sim(N0 = 7):
    # Creates main deck of cards
    mainDeck = Deck()
    nms = [*range(10), *range(1,10)]
    for new_card in [Card(i, j) for i in nms for j in ["R", "G", "Y", "B"]]: mainDeck.add(new_card)
    if(mainDeck.len()!=76): return("Error in deck") # Check for 76
    mainDeck.shuffle()

    # Number of players
    Player1 = Deck()
    Player2 = Deck()

    for i in range(N0): 
        new_card = mainDeck.get_rnd()
        Player1.add(new_card)
        new_card = mainDeck.get_rnd()
        Player2.add(new_card)

    #print(Player1.len() )
    #print(Player2.len() )
    #print(mainDeck.len())

    restTable = Deck()
    table_card = mainDeck.get_top()
    restTable.add(table_card)

    #print("Let's start playing: Go!")

    while mainDeck.len() > 2:
        if(Player1.len() == 0): return(1) # Playing color first wins
        elif(Player2.len() == 0): return(2) # Playing number first wins

        table_card = restTable.read(0)
        out = Player1.play_by_color(table_card)
        if (out): restTable.add(out)
        else: Player1.add(mainDeck.get_top())

        table_card = restTable.read(0)
        out = Player2.play_by_number(table_card)
        if (out): restTable.add(out)
        else: Player2.add(mainDeck.get_top())

    return(0) # Both tied because the mainDeck ran out of cards

hist = [0,0,0]
for i in range(100000):
    result = sim()
    hist[result] += 1

print(hist / np.sum(hist))

