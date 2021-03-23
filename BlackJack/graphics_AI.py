import pygame
import time
from blackjack_graphics_AI import *
import neat


def game(genomes,config):
    pygame.init()

    clock = pygame.time.Clock()

    width = 1000
    height = 800
    win = pygame.display.set_mode((width, height))

    icon = pygame.image.load('Cards/chips.png')

    pygame.display.set_caption("Black Jack")
    pygame.display.set_icon(icon)
    pygame.display.flip()

    global outcome, hit, busted
    outcome = ''

    white = (255,255,255)


    huge_font = pygame.font.Font('freesansbold.ttf', 50)
    large_font = pygame.font.Font('freesansbold.ttf', 32)
    small_font = pygame.font.Font('freesansbold.ttf', 20)


    nets = []
    ge = []

    # Create & shuffle the deck, deal two cards to each player



    for _,g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)

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
        

        output = nets[0].activate((player_hand.value,len(dealer_hand.cards),dealer_hand.value,dealer_hand.aces,player_hand.aces,dealer_hand.check_blackjack))
        if output[0]>0:
            hit(deck,hand,dealer_hand,win)
        else:
            stand(deck,hand,dealer_hand,win)

        win.fill((34, 79, 56))

    
        
    
        show_cards(player_hand,dealer_hand,[0,0],win,deck)
        hit_button = Button(10,500,100,100,win,(0,255,0),(0,200,0),hit,deck,player_hand,dealer_hand)
        hit_button.button()
        
        stand_button = Button(200,500,100,100,win,(255,0,0),(200,0,0),stand,deck,player_hand,dealer_hand)
        stand_button.button()

        player_value = Writer("Player Value: " + str(player_hand.value), white, large_font, win, [0, 350])
        outcome_writing = Writer(outcome, white, huge_font, win, [400, 400])

        hit_writing = Writer("HIT", white, small_font, win, [45, 550])
        stand_writing = Writer("STAND" , white, small_font, win, [220, 550])

        player_value.show_writing()
        outcome_writing.show_writing()
        hit_writing.show_writing()
        stand_writing.show_writing()

        



        clock.tick(200)
        pygame.display.flip()

        
        if not outcome == '':
            dealer_hand.add_card(deck.deal())
        
        if player_hand.value > 21:
                busted = True
                outcome = player_busts()
                show_cards(player_hand,dealer_hand,[0,0],win,deck)
        # If Player hasn't busted, play Dealer's hand        
        while decision_dict['stand']==1 or busted==True:
            if player_hand.value > 21:
                break
            if player_hand.value <= 21:
                while dealer_hand.value < 17:
                    deal_hit = dealer_hit(deck,dealer_hand,player_hand,win)
                    dealer_hand.add_card(deal_hit)
                    dealer_hand.adjust_for_ace()

                    show_cards(player_hand,dealer_hand,[0,0],win,deck)
                    
                    # Show all cards
                    
                
                    
                
                # Test different winning scenarios
                if dealer_hand.value > 21:
                    outcome = dealer_busts()
                    break

                elif dealer_hand.value > player_hand.value:
                    outcome = dealer_wins()
                    break

                elif dealer_hand.value < player_hand.value:
                    outcome = player_wins()
                    break

                else:
                    outcome = push()
                    break
        
        if outcome == "Player Busted!":
            ge[0].fitness -= 3
            nets.pop(0)
            ge.pop(0)
            running = False
            break
        if outcome =="Dealer Wins!":
            ge[0].fitness -=1
            nets.pop(0)
            ge.pop(0)
            running = False
            break

    
        if outcome == "Player Wins!":
            ge[0].fitness += 4
            decision_dict['stand']=0
            decision_dict['hit']=0
            running = False
            game()

        if outcome == "Dealer Busted!":
            ge[0].fitness += 2
            decision_dict['stand']=0
            decision_dict['hit']=0
            running = False
            game()


        if outcome == "Dealer and Player tie! It's a push!":
            ge[0].fitness += 2
            decision_dict['stand']=0
            decision_dict['hit']=0
            running = False
            game()
            

                


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    #p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    #p.add_reporter(stats)

    winner = p.run(game,100)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,"config-feedforward.txt")
    run(config_path)
                

