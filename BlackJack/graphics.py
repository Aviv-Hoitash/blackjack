import pygame
import time
from blackjack_graphics import *
pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 800
win = pygame.display.set_mode((width, height))

icon = pygame.image.load('Cards/chips.png')

pygame.display.set_caption("Black Jack")
pygame.display.set_icon(icon)
pygame.display.flip()




 
# Create & shuffle the deck, deal two cards to each player





deck = Deck(win)
deck.shuffle()

player_hand = Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())

dealer_hand = Hand()
dealer_hand.add_card(deck.deal())


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    win.fill((34, 79, 56))

    print(outcome)
    
    

    show_cards(player_hand,dealer_hand,[0,0],win,deck)
    hit_button = Button(10,500,100,100,win,(0,255,0),(0,200,0),hit,deck,player_hand,dealer_hand)
    hit_button.button()
    
    stand_button = Button(200,500,100,100,win,(255,0,0),(200,0,0),stand,deck,player_hand,dealer_hand)
    stand_button.button()



    clock.tick(200)
    pygame.display.flip()
    
    if not outcome == '':
        dealer_hand.add_card(deck.deal())
    

    
    if player_hand.value > 21:
            player_busts()
            show_cards(player_hand,dealer_hand,[0,0],win,deck)
            done = True
    # If Player hasn't busted, play Dealer's hand        
    while decision_dict['stand']==1 or done==True:
        if player_hand.value > 21:
            break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit = dealer_hit(deck,dealer_hand,player_hand,win)
                dealer_hand.add_card(hit)
                dealer_hand.adjust_for_ace()
                print(dealer_hand.value)

                show_cards(player_hand,dealer_hand,[0,0],win,deck)
                
                # Show all cards
                
            
                
            
            # Test different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts()
                break

            elif dealer_hand.value > player_hand.value:
                dealer_wins()
                break

            elif dealer_hand.value < player_hand.value:
                player_wins()
                break

            else:
                push()
                break
                
                

