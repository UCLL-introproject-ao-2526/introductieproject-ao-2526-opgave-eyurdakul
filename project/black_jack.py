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

active = False
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = True
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False

def create_button(coordinates, text, rect_value):
    button = pygame.draw.rect(screen, "white", coordinates, 0, 5)
    pygame.draw.rect(screen, "green", coordinates, 3, 5)
    deal_text = font.render(text, True, "black")
    screen.blit(deal_text, rect_value)
    return button

def draw_game(active, records):
    buttons = []
    if not active:
        buttons.append(create_button([150, 20, 300, 100], "DEAL HAND", (165, 50)))
    else:
        buttons.append(create_button([0, 700, 300,100], "HIT ME", (55, 735)))
        buttons.append(create_button([300, 700, 300,100], "STAND", (355, 735)))
        score_text = font_small.render(f"Wins: {records[0]}   Losses: {records[1]}   Draws: {records[2]}", True, "white")
        screen.blit(score_text, (15, 840))
    return buttons

def hit_button_clicked():
    print("HIT")

def stand_button_clicked():
    print("STAND")

def deal_cards(hand, deck):
    card = random.randint(0, deck)
    hand.append(deck[card - 1])
    deck.pop(card - 1)
    return hand, deck

def draw_cards(player, dealer, reveal):
    for i in range(len(player)):
        pygame.draw.rect(screen, 'white', [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
        screen.blit(font.render(player[i], True, 'black'), (75 + 70 * i, 465 + 5 * i))
        screen.blit(font.render(player[i], True, 'black'), (75 + 70 * i, 635 + 5 * i))
        pygame.draw.rect(screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

    for i in range(len(dealer)):
        pygame.draw.rect(screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
        if i != 0 or reveal:
            screen.blit(font.render(dealer[i], True, 'black'), (75 + 70 * i, 165 + 5 * i))
            screen.blit(font.render(dealer[i], True, 'black'), (75 + 70 * i, 335 + 5 * i))
        else:
            screen.blit(font.render('???', True, 'black'), (75 + 70 * i, 165 + 5 * i))
            screen.blit(font.render('???', True, 'black'), (75 + 70 * i, 335 + 5 * i))
        pygame.draw.rect(screen, 'blue', [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)

def calculate_score(hand):
    hand_score = 0
    aces_count = hand.count("A")
    for i in range(len(hand)):
        for j in range(8):
            if hand[i] == cards[j]:
                hand_score += int(hand[i])

run = True
while run:
    timer.tick(fps)
    screen.fill("black")

    if initial_deal:
        for i in range(2):
              my_hand, game_deck = deal_cards(my_hand, game_deck)
              dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        initial_deal = False

    if active:
        draw_cards(my_hand, dealer_hand, reveal_dealer)

    buttons = draw_game(active, records)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
            else:
                if buttons[0].collidepoint(event.pos):
                    hit_button_clicked()
                if buttons[1].collidepoint(event.pos):
                    stand_button_clicked()
    pygame.display.flip()