import copy
import random
import pygame

pygame.init()

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 1
game_deck = copy.deepcopy(decks * one_deck)
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pygame BlackJack")
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 44)
font_small = pygame.font.Font("freesansbold.ttf", 36)

active = True
records = [0, 0, 0]
player_score = 0
dealer_score = 0

def create_button(coordinates, text, rect_value):
    button = pygame.draw.rect(screen, "white", coordinates, 0, 5)
    pygame.draw.rect(screen, "green", [150, 20, 300, 100], 3, 5)
    deal_text = font.render(text, True, "black")
    screen.blit(deal_text, rect_value)
    return button

def draw_game(active, records):
    buttons = []
    if not active:
        buttons.append(create_button([150, 20, 300, 180], "DEAL HAND", (165, 50)))
    else:
        buttons.append(create_button([0, 700, 300,100], "HIT ME", (55, 735)))
        buttons.append(create_button([300, 700, 300,100], "STAND", (355, 735)))
        score_text = font_small.render(f"Wins: {records[0]}.   Losses: {records[1]}.   Draws: {records[2]}", True, "white")
        screen.blit(score_text, (15, 840))

run = True
while run:
    timer.tick(fps)
    screen.fill("black")
    buttons = draw_game(active, records)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()