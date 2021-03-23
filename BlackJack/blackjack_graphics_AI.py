import random
from deck import *

suits = ('Clubs', 'Diamonds', 'Hearts', 'Spaides')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


decision_dict = {'hit':0,'stand':0}

global busted
busted = False





class Writer():
    def __init__(self, writing, color, font, win, location):
        self.writing = writing
        self.color = color
        self.win = win
        self.location = location
        self.font = font

    def show_writing(self):
        text = self.font.render(self.writing, False, self.color)
        self.win.blit(text, (self.location[0], self.location[1]))

# CLASS DEFINTIONS:

class Button():
    def __init__(self, x, y, w, h, win, active_color, inactive_color, func,deck,hand,dealer_hand):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.win = win
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.func = func
        self.deck = deck
        self.hand = hand
        self.dealer_hand = dealer_hand

    def button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(self.win, self.active_color,
                             (self.x, self.y, self.w, self.h))
            for event in pygame.event.get():
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    self.func(self.deck,self.hand,self.dealer_hand,self.win)

        else:
            pygame.draw.rect(self.win, self.inactive_color,
                             (self.x, self.y, self.w, self.h))


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

class Deck:
    
    def __init__(self,win):
        self.win = win
        self.deck = []  # start with an empty list
        self.gui_cards = {}
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

        for card in range(len(self.deck)):
            self.gui_cards[self.deck[card]] = list(gui_deck.keys())[card]
                
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

    

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def check_blackjack(self):
        if self.aces>=1 or self.value == 10:
            return 1
        else:
            return 0
            

def hit(deck,hand,dealer_hand,win):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    show_cards(hand,dealer_hand,[0,0],win,deck)
    decision_dict['hit'] = 1

def dealer_hit(deck,hand,dealer_hand,win):
    return deck.deal()
    show_cards(hand,dealer_hand,[0,0],win,deck)


def stand(deck,hand,dealer_hand,win):
    decision_dict['stand'] = 1
    decision_dict['hit'] = 0
    

    


    

    
def show_cards(player,dealer,location,win,deck):
    global busted
    if busted==False:
        show_card(win,(location[0], location[1]), gui_deck['face_down'])
        for x,card in enumerate(dealer.cards):
            show_card(win, (location[0]+120*(x+1), location[1]), gui_deck[deck.gui_cards[card]])

    


        for x,card in enumerate(player.cards):
            show_card(win, (location[0]+120*x, location[1]+670), gui_deck[deck.gui_cards[card]])
        
    
    
    if player.value>21 or decision_dict['stand']==1:
        busted = True
        for x,card in enumerate(dealer.cards):
            show_card(win, (location[0]+120*x, location[1]), gui_deck[deck.gui_cards[card]])
        for x,card in enumerate(player.cards):
            show_card(win, (location[0]+120*x, location[1]+670), gui_deck[deck.gui_cards[card]])
    


 
    
def player_busts():
    return "Player Busted!"


def player_wins():
    return "Player Wins!"
    

def dealer_busts():
    return "Dealer Busted!"
    
    
def dealer_wins():
    return "Dealer Wins!"

    
    
def push():
    return "Dealer and Player tie! It's a push!"
    

