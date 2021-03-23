import pygame
import os

card_image = {'2_C': '2_C.png', '3_C': '3_C.png', '4_C': '4_C.png', '5_C': '5_C.png', '6_C': '6_C.png',
              '7_C': '7_C.png', '8_C': '8_C.png', '9_C': '9_C.png', '10_C': '10_C.png', 'J_C': 'J_C.png',
              'Q_C': 'Q_C.png', 'K_C': 'K_C.png', 'A_C': 'A_C.png', '2_D': '2_D.png', '3_D': '3_D.png',
              '4_D': '4_D.png', '5_D': '5_D.png', '6_D': '6_D.png', '7_D': '7_D.png', '8_D': '8_D.png',
              '9_D': '9_D.png', '10_D': '10_D.png', 'J_D': 'J_D.png', 'Q_D': 'Q_D.png', 'K_D': 'K_D.png',
              'A_D': 'A_D.png', '2_H': '2_H.png', '3_H': '3_H.png', '4_H': '4_H.png', '5_H': '5_H.png',
              '6_H': '6_H.png', '7_H': '7_H.png', '8_H': '8_H.png', '9_H': '9_H.png', '10_H': '10_H.png',
              'J_H': 'J_H.png', 'Q_H': 'Q_H.png', 'K_H': 'K_H.png', 'A_H': 'A_H.png', '2_S': '2_S.png',
              '3_S': '3_S.png', '4_S': '4_S.png', '5_S': '5_S.png', '6_S': '6_S.png', '7_S': '7_S.png',
              '8_S': '8_S.png', '9_S': '9_S.png', '10_S': '10_S.png', 'J_S': 'J_S.png', 'Q_S': 'Q_S.png',
              'K_S': 'K_S.png', 'A_S': 'A_S.png','face_down':'face_down.png'}
gui_deck = {}

# A_S = pygame.image.load(os.path.join("C:/Users/Hilla/Aviv coding/Poker/Cards","A_S.png"))
for card in card_image.keys():
    card_gui = pygame.image.load(os.path.join("C:/Users/Hilla/Aviv coding/Python/Working On/BlackJack/Cards/", card_image[card]))
    card_gui = pygame.transform.scale(card_gui, (100, 130))
    gui_deck[card] = card_gui


def show_card(win, loc, gui):
    win.blit(gui, loc)
