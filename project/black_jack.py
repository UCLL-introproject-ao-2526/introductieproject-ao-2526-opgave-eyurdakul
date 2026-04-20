import copy
import random
import pygame
import constants

pygame.init()

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 1
game_deck = copy.deepcopy(decks * one_deck)
screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
pygame.display.set_caption("Pygame BlackJack")
timer = pygame.time.Clock()
font = pygame.font.Font(constants.DEFAULT_FONT, constants.FONT_SIZE_LARGE)
font_small = pygame.font.Font(constants.DEFAULT_FONT, constants.FONT_SIZE_SMALL)

active = False
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = True
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
add_score = False
results = ["", "Player busted!", "Player wins!", "Dealer wins!", "Tie game!"]

def create_button(coordinates, text, rect_value):
    button = pygame.draw.rect(screen, constants.WHITE, coordinates, 0, 5)
    pygame.draw.rect(screen, constants.GREEN, coordinates, 3, 5)
    deal_text = font.render(text, True, constants.BLACK)
    screen.blit(deal_text, rect_value)
    return button

def draw_game(active, records, result):
    buttons = []
    if not active:
        buttons.append(create_button([150, 20, 300, 100], "DEAL HAND", (165, 50)))
    else:
        buttons.append(create_button([0, 700, 300,100], "HIT ME", (55, 735)))
        buttons.append(create_button([300, 700, 300,100], "STAND", (355, 735)))
        score_text = font_small.render(f"Wins: {records[0]}   Losses: {records[1]}   Draws: {records[2]}", True, constants.WHITE)
        screen.blit(score_text, (15, 840))
    if result != 0:
        screen.blit(font.render(results[result], True, constants.WHITE), (15, 25))
        buttons.append(create_button([150, 220, 300, 100], "NEW HAND", (165, 250)))
    return buttons

def deal_cards(hand, deck):
    card = random.randint(0, len(deck))
    hand.append(deck[card - 1])
    deck.pop(card - 1)
    return hand, deck

def draw_cards(player, dealer, reveal):
    for i in range(len(player)):
        pygame.draw.rect(screen, constants.WHITE, [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
        screen.blit(font.render(player[i], True, constants.BLACK), (75 + 70 * i, 465 + 5 * i))
        screen.blit(font.render(player[i], True, constants.BLACK), (75 + 70 * i, 635 + 5 * i))
        pygame.draw.rect(screen, constants.RED, [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

    for i in range(len(dealer)):
        pygame.draw.rect(screen, constants.WHITE, [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
        if i != 0 or reveal:
            screen.blit(font.render(dealer[i], True, constants.BLACK), (75 + 70 * i, 165 + 5 * i))
            screen.blit(font.render(dealer[i], True, constants.BLACK), (75 + 70 * i, 335 + 5 * i))
        else:
            screen.blit(font.render('???', True, constants.BLACK), (75 + 70 * i, 165 + 5 * i))
            screen.blit(font.render('???', True, constants.BLACK), (75 + 70 * i, 335 + 5 * i))
        pygame.draw.rect(screen, constants.BLUE, [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)

def calculate_score(hand):
    hand_score = 0
    for i in range(len(hand)):
        for j in range(8):
            if hand[i] == cards[j]:
                hand_score += int(hand[i])
        if hand[i] in ["10", "J", "Q", "K"]:
            hand_score += 10
        elif hand[i] == "A":
            if hand_score <= 10:
                hand_score += 11
            else:
                hand_score += 1
    return hand_score

def draw_scores(player, dealer):
    screen.blit(font.render(f"Score[{player}]", True, constants.WHITE), (350, 400))
    if reveal_dealer:
        screen.blit(font.render(f"Score[{dealer}]", True, constants.WHITE), (350, 100))

def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            result = 2
        elif play_score < deal_score <= 21:
            result = 3
        else:
            result = 4
        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False 
    return result, totals, add


run = True
while run:
    timer.tick(constants.FPS)
    screen.fill(constants.BLACK)

    if initial_deal:
        for i in range(2):
              my_hand, game_deck = deal_cards(my_hand, game_deck)
              dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        initial_deal = False

    if active:
        player_score = calculate_score(my_hand)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)
        draw_cards(my_hand, dealer_hand, reveal_dealer)

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)
    buttons = draw_game(active, records, outcome)

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
                    outcome = 0
                    hand_active = True
                    add_score = True
            else:
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
                elif len(buttons) == 3:
                    if buttons[2].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        reveal_dealer = False
                        add_score = True
                        dealer_score = 0
                        player_score = 0
    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True
    pygame.display.flip()