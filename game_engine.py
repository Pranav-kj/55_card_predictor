# game_engine.py

import pygame

rank_map = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13
}

class GameEngine:
    def __init__(self):
        self.score = 0
        self.streak = 0
        self.message = ""
        self.message_color = (255, 255, 255)

    def evaluate_guess(self, current_card, next_card, guess):
        current_val = rank_map[current_card.rank_str]
        next_val = rank_map[next_card.rank_str]

        if next_val == current_val:
            # Task 3: Tie handling
            self.message = "PUSH / TIE! Rank matched."
            self.message_color = (255, 255, 0)  # yellow
            return "tie"

        elif (guess == "HIGHER" and next_val > current_val) or \
             (guess == "LOWER" and next_val < current_val):
            # Task 2: Win streak multiplier
            self.streak += 1
            if self.streak >= 5:
                self.score += 3
            elif self.streak >= 3:
                self.score += 2
            else:
                self.score += 1
            self.message = f"CORRECT! {current_val} vs {next_val}"
            self.message_color = (0, 255, 0)  # green
            return "correct"

        else:
            self.streak = 0
            self.message = f"WRONG! {current_val} vs {next_val}"
            self.message_color = (255, 0, 0)  # red
            return "wrong"

    def render(self, screen, current_card, next_card):
        # Task 4: Side-by-side reveal
        current_card.draw(screen, x=100, y=200)
        next_card.draw(screen, x=300, y=200)
        pygame.display.flip()
        pygame.time.wait(1000)  # pause for 1 second
