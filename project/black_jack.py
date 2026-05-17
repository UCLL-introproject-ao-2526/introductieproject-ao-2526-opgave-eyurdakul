import pygame
import os
import constants

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, FPS
from enums import SoundLibrary
from mixer import Mixer
from deck import Deck
from renderer import Renderer

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Pygame BlackJack')
timer = pygame.time.Clock()
font_path = os.path.join('assets', constants.DEFAULT_FONT)
font = pygame.font.Font(font_path, constants.FONT_SIZE_LARGE)
font_small = pygame.font.Font(font_path, constants.FONT_SIZE_SMALL)
background_image = pygame.image.load(os.path.join('assets', 'background.jpeg')).convert()

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

mixer = Mixer(pygame.mixer)
game_deck = Deck()
renderer = Renderer(screen)

"""
Helper methode for calculating the button position
"""
def calculate_button_x_position(count, position=1):
    button_space = count * BUTTON_WIDTH
    gap_size = (SCREEN_WIDTH - button_space) / (count + 1)
    return (gap_size * position) + (BUTTON_WIDTH * (position - 1))

"""
Creates buttons based on the game status
"""
def draw_game(active, records, result):
    buttons = []
    if not active:
        buttons.append(renderer.draw_button(font, calculate_button_x_position(1), 20, 'DEAL HAND'))
    else:
        buttons.append(renderer.draw_button(font, calculate_button_x_position(2, 1), 700, 'HIT ME'))
        buttons.append(renderer.draw_button(font, calculate_button_x_position(2, 2), 700, 'STAND'))
        score_text = font_small.render(f'Wins: {records[0]}   Losses: {records[1]}   Draws: {records[2]}', True, constants.WHITE)
        screen.blit(score_text, (15, 840))
    if result != 0:
        if result == 1:
            mixer.play(SoundLibrary.LOSE)
        elif result == 2:
            mixer.play(SoundLibrary.WIN)
        screen.blit(font.render(constants.RESULTS[result], True, constants.WHITE), (15, 25))
        buttons.append(renderer.draw_button(font, calculate_button_x_position(1), 220, 'NEW HAND'))
    return buttons

"""
Draws the cards put on the table
"""
def draw_cards(player, dealer, reveal):
    for i in range(len(player)):
        renderer.draw_card(player[i], 70 + (70 * i), 460 + (5 * i))
    for i in range(len(dealer)):
        renderer.draw_card(dealer[i], 70 + (70 * i), 160 + (5 * i), (i != 0 or reveal))

"""
Calculates the score of a hand based on Blackjack rules
"""
def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        if card.text in ['J', 'Q', 'K']: score += 10
        elif card.text == 'A':
            score += 11
            aces += 1
        else: score += int(card.text)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

"""
Draws the current score on screen
"""
def draw_scores(player, dealer):
    screen.blit(font.render(f'Score: {player}', True, constants.WHITE), (350, 400))
    if reveal_dealer:
        screen.blit(font.render(f'Score: {dealer}', True, constants.WHITE), (350, 100))

"""
Based on the status of the game, players hand and the dealers hand, checks whether the player wins or loses
"""
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
    timer.tick(FPS)
    screen.blit(background_image, (0, 0))

    if initial_deal:
        game_deck.create()
        for i in range(2):
              my_hand.append(game_deck.deal())
              dealer_hand.append(game_deck.deal())
        initial_deal = False

    if active:
        player_score = calculate_score(my_hand)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand.append(game_deck.deal())
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
                    mixer.play(SoundLibrary.CLICK)
                    mixer.play(SoundLibrary.SHUFFLE)
                    active = True
                    initial_deal = True
                    game_deck.create()
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    add_score = True
            else:
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand.append(game_deck.deal())
                    mixer.play(SoundLibrary.CARD)
                elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
                    mixer.play(SoundLibrary.CHIP)
                elif len(buttons) == 3:
                    if buttons[2].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck.create()
                        mixer.play(SoundLibrary.SHUFFLE)
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