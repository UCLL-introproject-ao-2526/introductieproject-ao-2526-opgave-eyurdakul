import pygame
import os
from settings import CARD_WIDTH, CARD_HEIGHT
from constants import BORDER_RADIUS

class Renderer:
    def __init__(self, screen):
        self._screen = screen
        self._font = pygame.font.SysFont('arial', 20, bold=True)

        background_path = os.path.join('assets', 'card_background.png')
        self._card_back = pygame.image.load(background_path).convert_alpha()
        self._card_back = pygame.transform.scale(self._card_back, (CARD_WIDTH, CARD_HEIGHT))

        self._suit_images = {
            1: pygame.image.load(os.path.join('assets/suits', 'hearts.png')).convert_alpha(),
            2: pygame.image.load(os.path.join('assets/suits', 'diamonds.png')).convert_alpha(),
            3: pygame.image.load(os.path.join('assets/suits', 'spades.png')).convert_alpha(),
            4: pygame.image.load(os.path.join('assets/suits', 'clubs.png')).convert_alpha(),
        }

        for k in self._suit_images:
            self._suit_images[k] = pygame.transform.scale(self._suit_images[k], (15, 15))

    def draw_card(self, card, x, y, reveal=True):
        pygame.draw.rect(self._screen, (255, 255, 255), (x, y, CARD_WIDTH, CARD_HEIGHT), border_radius=BORDER_RADIUS)
        pygame.draw.rect(self._screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), width=2, border_radius=BORDER_RADIUS)

        if reveal:
            suit_key = card.symbol.value
            suit_img = self._suit_images[suit_key]

            color = (200, 0, 0) if suit_key in [1, 2] else (0, 0, 0)

            rank_text = self._font.render(card.text, True, color)

            self._screen.blit(rank_text, (x + 5, y + 5))
            self._screen.blit(suit_img, (x + 5, y + 25))

            self._screen.blit(rank_text, (x + CARD_WIDTH - 20, y + 5))
            self._screen.blit(suit_img, (x + CARD_WIDTH - 20, y + 25))

            self._screen.blit(rank_text, (x + 5, y + CARD_HEIGHT - 40))
            self._screen.blit(suit_img, (x + 5, y + CARD_HEIGHT - 20))

            self._screen.blit(rank_text, (x + CARD_WIDTH - 20, y + CARD_HEIGHT - 40))
            self._screen.blit(suit_img, (x + CARD_WIDTH - 20, y + CARD_HEIGHT - 20))
        else:
            self._screen.blit(self._card_back, (x, y))