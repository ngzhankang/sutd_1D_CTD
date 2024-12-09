# im gonna mess around with this file so dont mind me(for real)
# import library
import tkinter as tk
from tkinter import ttk
import json, copy
from random import sample
from utils import load_config, render_deck
from StartScreen import StartScreen
from Enemy import Enemy
from Card import Card

# main logic
class App(ttk.Frame):
    def __init__(self, root):
        self.root = root
        self.turn_limit = 4  # Start with 4 turns for the first encounter
        self.current_turn = 1
        self.deck = self.create_deck()
        self.hand = []
        self.current_enemy = None
        self.encounters = []
        self.difficulty = None
        self.selected_cards = []
        self.selected_classcards = []
        self.selected = []
        self.confirm_button = None  # Track the confirmation button to avoid duplicates
        self.card_buttons = []  # List to keep track of card buttons

        self.start_screen = StartScreen(root, self, tk)

        # Maximise the window and center everything
        self.root.state('normal')  # Ensure the window is not in fullscreen state
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")  # Maximise window size
        self.root.update_idletasks()  # Update the window size
        self.window_width = self.root.winfo_width()  # Get window width
        self.window_height = self.root.winfo_height()  # Get window height

    def setup_ui(self):
        # Layout Frames
        self.top_frame = tk.Frame(self.root)
        self.top_frame.place(relx=0.5, rely=0.1, anchor="center")  # Position top frame in the center

        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.place(relx=0.5, rely=0.2, anchor="center")  # Position stats frame

        self.cards_frame = tk.Frame(self.root)
        self.cards_frame.place(relx=0.5, rely=0.6, anchor="center")  # Position cards frame

        self.actions_frame = tk.Frame(self.root)
        self.actions_frame.place(relx=0.5, rely=0.8, anchor="center")  # Position actions frame

        # Stats Display
        self.enemy_label = tk.Label(self.stats_frame, text="Enemy: None")
        self.enemy_label.grid(row=0, column=0)

        self.enemy_health_label = tk.Label(self.stats_frame, text="Enemy Health: N/A")  # Display for enemy health
        self.enemy_health_label.grid(row=0, column=1)

        self.turn_label = tk.Label(self.stats_frame, text="Turn: 1 / 4")
        self.turn_label.grid(row=0, column=3)

        self.selected_cards_label = tk.Label(self.actions_frame, text="Selected Cards: None")
        self.selected_cards_label.pack()

        self.message_label = tk.Label(self.actions_frame, text="Select 4 cards to deal damage!")
        self.message_label.pack()

        self.reselect_button = tk.Button(self.actions_frame, text="Reselect Cards", command=self.reselect_cards, width=15, height=1)
        self.reselect_button.pack(pady=3)

        self.calculate_button = tk.Button(self.actions_frame, text="Calculate Damage", command=self.calculate_damage, width=15, height=1)
        self.calculate_button.pack(pady=3)

        self.confirm_attack_button = tk.Button(self.actions_frame, text="Confirm Attack", command=self.deal_damage, width=15, height=1)
        self.confirm_attack_button.pack(pady=3)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        # Based on difficulty, create different encounters
        self.encounters = self.create_encounters(difficulty)

    def create_deck(self):
        """Create the player's starting deck with grades mapped to GPA values"""
        return [
            Card("Homework", "A"),
            Card("Study", "A-"),
            Card("Project", "B+"),
            Card("Research", "B+"),
            Card("Extra Credit", "B"),
            Card("Extra Work", "B-"),
            Card("Essay", "B-"),
            Card("Lab Work", "C+"),
            Card("Finals", "C+"),
            Card("Midterm", "C"),
            Card("Group Project", "C-"),
            Card("Reading", "C-"),
            Card("Quiz", "D")
        ]
    
    def create_encounters(self, difficulty):
        """Create different encounters based on the difficulty."""
        # Define base enemies (only names for now)
        base_enemies = [
            "Homework",  
            "Project",   
            "Research",  
            "Midterm Boss",  # Midterm Boss
            "Finals Boss"   # Final Boss
        ]

        # Start with an empty list of encounters
        encounters = []

        # GPA scaling logic based on difficulty
        if difficulty == "Term 1":
            # Term 1: Enemies scale from 1.0 to 5.3 (6 enemies total)
            gpa_scaling = [1.0, 1.8, 2.5, 3.1, 4.0, 5.3]
            for i in range(4):
                encounters.append(Enemy(base_enemies[i], gpa_scaling[i], "Regular"))
            # Midterm Boss (mid-point encounter)
            encounters.append(Enemy(base_enemies[3], gpa_scaling[3], "Midterm"))
            # Finals Boss
            encounters.append(Enemy(base_enemies[4], gpa_scaling[5], "Finals"))

        elif difficulty == "Term 2":
            # Term 2: Enemies scale from 1.0 to 5.3 (5 enemies total)
            gpa_scaling = [1.0, 2.0, 2.8, 3.5, 5.3]
            for i in range(3):
                encounters.append(Enemy(base_enemies[i], gpa_scaling[i], "Regular"))
            # Midterm Boss (mid-point encounter)
            encounters.append(Enemy(base_enemies[3], gpa_scaling[3], "Midterm"))
            # Finals Boss
            encounters.append(Enemy(base_enemies[4], gpa_scaling[4], "Finals"))

        elif difficulty == "Term 3":
            # Term 3: Enemies scale from 1.0 to 5.3 (4 enemies total)
            gpa_scaling = [1.0, 2.5, 4.0, 5.3]
            for i in range(2):
                encounters.append(Enemy(base_enemies[i], gpa_scaling[i], "Regular"))
            # Midterm Boss (mid-point encounter)
            encounters.append(Enemy(base_enemies[3], gpa_scaling[2], "Midterm"))
            # Finals Boss
            encounters.append(Enemy(base_enemies[4], gpa_scaling[3], "Finals"))

        return encounters
    
    def start_game(self):
        self.setup_ui()
        self.next_encounter()  # Start encounter immediately

    def draw_hand(self):
        """Draw 7 cards for the player's hand."""
        # Clear the current hand
        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        # Draw 7 cards from the deck
        self.hand = [card for card in sample(self.deck, 7)]
        self.selected = [str(card) for card in self.hand]
        for card in self.hand:
            button = tk.Button(
                self.cards_frame, 
                text=f"{card.name}\n({card.grade})",
                width=28,  # Fixed width
                height=5,  # Fixed height
                command=lambda c=card: self.select_card(c, self.selected)
            )
            self.card_buttons.append(button)  # Track card buttons
            button.pack(side="left", padx=5, pady=5)

    def select_card(self, card, hand):
        self.message_label.config(text="Select 4 cards to deal damage!")
        """Select or deselect a card for the player."""
        if str(card) in self.selected_cards and str(card) not in hand: # Deselect the card
            hand.append(str(card))
            self.selected_cards.remove(str(card))
            self.selected_classcards.remove(card)
        else: # Select the card
            if len(self.selected_cards) < 4:  # Limit to 4 cards
                hand.remove(str(card))
                self.selected_cards.append(str(card))
                self.selected_classcards.append(card)

        # Update the selected cards label
        selected_card_names = [card for card in self.selected_cards]
        self.selected_cards_label.config(text=f"Selected Cards: {', '.join(selected_card_names)}")

        # Enable "Calculate Damage" buttons if cards are selected
        if len(self.selected_cards) == 4:
            self.message_label.config(text="Now calculate how much damage you would do and then attack!")
            self.calculate_button.config(state=tk.NORMAL)
        else:
            self.confirm_attack_button.config(state=tk.DISABLED)
            self.calculate_button.config(state=tk.DISABLED)

    def calculate_damage(self):
        """Calculate the damage based on selected cards."""
        total_value = sum(card.value for card in self.selected_classcards)
        gpa_damage = round(total_value / 4, 1)
        self.message_label.config(text=f"Calculated Damage: {gpa_damage} GPA")
        self.confirm_attack_button.config(state=tk.NORMAL)

    def reselect_cards(self):
        """Reselect the player's cards by resetting the selected cards and allowing them to pick again."""
        self.selected_cards = []  # Clear the current card selection
        self.selected_classcards = []
        self.selected = [str(card) for card in self.hand]
        self.message_label.config(text="Select 4 cards to deal damage!")
        self.selected_cards_label.config(text="Selected Cards: None")  # Reset the label

        # Disable the "Next Turn" and "Calculate Damage" buttons until cards are selected
        self.confirm_attack_button.config(state=tk.DISABLED)
        self.calculate_button.config(state=tk.DISABLED)

    def deal_damage(self):
        """Deal damage to the enemy and move to the next turn."""
        if self.current_enemy:
            gpa_damage = round(sum(card.value for card in self.selected_classcards) / 4, 1)
            self.current_enemy.gpa -= gpa_damage  # Subtract the GPA damage
            self.message_label.config(text=f"Dealt {gpa_damage} GPA damage to {self.current_enemy.name}")
            self.enemy_health_label.config(text=f"Enemy Health: {self.current_enemy.gpa} GPA")  # Update health label

        # Check if the enemy is defeated
        if self.current_enemy.gpa <= 0:
            self.message_label.config(text=f"{self.current_enemy.name} defeated!")
            self.next_encounter()
        else:
            self.next_turn()

    def next_encounter(self):
        """Move to the next encounter or end the game."""
        if not self.encounters:
            self.game_over("You won!")
            return

        self.current_enemy = self.encounters.pop(0)
        self.enemy_label.config(text=f"Enemy: {self.current_enemy.name}")
        self.enemy_health_label.config(text=f"Enemy Health: {self.current_enemy.gpa} GPA")  # Display initial enemy health
        self.draw_hand()

        self.confirm_attack_button.config(state=tk.DISABLED)
        self.calculate_button.config(state=tk.DISABLED)

    def next_turn(self):
        """Move to the next turn."""
        if self.current_turn >= self.turn_limit:
            self.game_over("Game Over: You ran out of turns!")
        else:
            self.current_turn += 1
            self.turn_label.config(text=f"Turn: {self.current_turn} / {self.turn_limit}")

    def game_over(self, message):
        """Handle game over scenario."""
        # Hide the game elements and show the game over screen
        for widget in self.root.winfo_children():
            widget.place_forget()

        self.game_over_screen(message)

    def game_over_screen(self, message):
        """Display a Game Over screen."""
        # Game Over message
        game_over_label = tk.Label(self.root, text=message, font=("Helvetica", 24))
        game_over_label.place(relx=0.5, rely=0.3, anchor="center")

        # Buttons for Quit and Restart
        quit_button = tk.Button(self.root, text="Quit", command=self.quit_game, width=20, height=2)
        quit_button.place(relx=0.5, rely=0.5, anchor="center")

        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, width=20, height=2)
        restart_button.place(relx=0.5, rely=0.7, anchor="center")

    def quit_game(self):
        """Quit the game."""
        self.root.quit()

    def restart_game(self):
        """Restart the game."""
        for widget in self.root.winfo_children():
            widget.place_forget()  # Hide any elements that might remain
        self.__init__(self.root)  # Reinitialize the game







if __name__ == "__main__":
    root = tk.Tk()
    game = App(root)
    root.mainloop()