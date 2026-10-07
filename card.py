# card.py
import pygame
import random

# Define suits and ranks
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, suit, rank_str):
        self.suit = suit
        self.rank_str = rank_str

    def draw(self, screen, x, y):
        # Simple rectangle card with rank text
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 80, 120))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 80, 120), 2)
        font = pygame.font.SysFont(None, 36)
        text = font.render(self.rank_str, True, (0, 0, 0))
        screen.blit(text, (x + 20, y + 40))

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None
