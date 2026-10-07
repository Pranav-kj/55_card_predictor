import pygame
import sys
from game_engine import GameEngine
from card import Card, Deck  # assuming you have card.py with Card/Deck classes

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("High-Low Card Predictor - Pygame Edition")
font = pygame.font.SysFont(None, 36)

# Initialize deck and engine
deck = Deck()
current_card = deck.draw_card()
engine = GameEngine()

# Buttons
higher_button = pygame.Rect(150, 400, 120, 50)
lower_button = pygame.Rect(370, 400, 120, 50)

def draw_button(rect, text, color):
    pygame.draw.rect(screen, color, rect)
    txt_surface = font.render(text, True, (255, 255, 255))
    screen.blit(txt_surface, (rect.x + 10, rect.y + 10))

running = True
while running:
    screen.fill((0, 100, 0))  # green background

    # Draw current card
    current_card.draw(screen, x=250, y=150)

    # Draw score and deck info
    score_surface = font.render(f"Score: {engine.score}", True, (255, 255, 0))
    deck_surface = font.render(f"Deck: {len(deck.cards)} left", True, (255, 255, 255))
    streak_surface = font.render(f"Streak: {engine.streak}", True, (0, 200, 255))

    screen.blit(score_surface, (20, 20))
    screen.blit(deck_surface, (400, 20))
    screen.blit(streak_surface, (20, 60))

    # Draw buttons
    draw_button(higher_button, "HIGHER", (0, 200, 0))
    draw_button(lower_button, "LOWER", (200, 0, 0))

    # Draw message
    if engine.message:
        msg_surface = font.render(engine.message, True, engine.message_color)
        screen.blit(msg_surface, (150, 350))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if deck.cards:  # only if cards remain
                next_card = deck.draw_card()
                if higher_button.collidepoint(event.pos):
                    result = engine.evaluate_guess(current_card, next_card, "HIGHER")
                elif lower_button.collidepoint(event.pos):
                    result = engine.evaluate_guess(current_card, next_card, "LOWER")
                else:
                    result = None

                if result:
                    # Render both cards side-by-side before moving on
                    engine.render(screen, current_card, next_card)

                    # Update current card for next round
                    current_card = next_card
