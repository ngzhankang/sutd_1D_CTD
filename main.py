# import library
import tkinter as tk
from tkinter import messagebox, ttk
from random import sample, randint, shuffle
from utils import *
from StartScreen import StartScreen
from Enemy import Enemy
import tkinter.font as tkFont
# from Card import Card

# main logic
class App(ttk.Frame):
    def __init__(self, root):
        self.root = root
        self.turn_limit = 0
        self.current_turn = 1
        self.deck = start_deck()
        self.hand = []
        self.current_enemy = None
        self.encounters = []
        self.difficulty = None
        self.selected_cards = []
        self.selected_classcards = []
        self.confirm_button = None  # Track the confirmation button to avoid duplicates
        self.card_buttons = {}  # List to keep track of card buttons
        self.wallet = 20
        self.tkFont = tkFont
        self.buttonclicks = 0
        self.tk = tk

        self.start_screen = StartScreen(root, self, tk)

        # Maximise the window and center everything
        self.root.state('zoomed')
        self.root.update_idletasks()  # Update the window size
        self.window_width = self.root.winfo_width()  # Get window width
        self.window_height = self.root.winfo_height()  # Get window height
        self.photo = self.tk.PhotoImage(file="./assets/bgshop2.png")
        self.winphoto = self.tk.PhotoImage(file="./assets/winningbg2.png")
        self.root.title('Study Up Till Death')
   

    def setup_ui(self):
        # Layout Frames
        self.top_frame = tk.Frame(self.root, bg='#1B1B1B')
        self.top_frame.place(relx=0.5, rely=0.1, anchor="center")  # Position top frame in the center

        self.stats_frame = tk.Frame(self.root, bg='#1B1B1B')
        self.stats_frame.place(relx=0.5, rely=0.2, anchor="center")  # Position stats frame

        self.cards_frame = tk.Frame(self.root, bg='#1B1B1B')
        self.cards_frame.place(relx=0.5, rely=0.4, anchor="center")  # Position cards frame

        self.actionsinfo_frame = tk.Frame(self.root, bg='#1B1B1B')
        self.actionsinfo_frame.place(relx=0.5, rely=0.6, anchor="center")  # Position actions frame

        self.actions_frame = tk.Frame(self.root, bg='#1B1B1B')
        self.actions_frame.place(relx=0.5, rely=0.7, anchor="center")  # Position actions frame

        # Stats Display     

        self.turn_label = tk.Label(self.stats_frame, text="Turn: 1 / 4",font=("Old School Adventures", 13), bg='#1B1B1B', fg='#F1C130')
        self.turn_label.grid(row=0, column=0)

        self.enemy_label = tk.Label(self.stats_frame, text="Enemy: None", font=("Old School Adventures", 21), bg='#1B1B1B', fg='white')
        self.enemy_label.grid(row=2, column=0)

        self.enemy_health_label = tk.Label(self.stats_frame, text="❤️‍🩹Enemy Health: N/A", font=("Old School Adventures", 13), bg='#1B1B1B', fg='#FF4F4F')  # Display for enemy health
        self.enemy_health_label.grid(row=4, column=0)

        self.selected_cards_label = tk.Label(self.actionsinfo_frame, text="Selected Cards: None", font=("Poppins", 13), bg='#1B1B1B', fg='white')
        self.selected_cards_label.pack()

        self.wallet_label = tk.Label(self.actionsinfo_frame, text=f"🪙Gold: {self.wallet}", font=("Poppins", 13), bg='#1B1B1B', fg='#F1C130')
        self.wallet_label.pack()

        self.message_label = tk.Label(self.actionsinfo_frame, text="🃏Select 4 cards to deal damage!", font=("Poppins", 16), bg='#1B1B1B', fg='white')
        self.message_label.pack()

        self.reselect_button = tk.Button(self.actions_frame, text="Reselect Cards", command=lambda:[self.update_count(), self.reselect_cards()], width=15, height=1, font=("Poppins", 10), bg='#F0F0F0', fg='#444444')
        self.reselect_button.grid(pady=3, padx=4, row=0, column=1)

        self.calculate_button = tk.Button(self.actions_frame, text="Calculate Damage", command=self.calculate_damage, width=15, height=1, font=("Poppins", 10), bg='#5F5F5F', fg='white')
        self.calculate_button.grid(pady=3, padx=4, row=0, column=2)

        self.confirm_attack_button = tk.Button(self.actions_frame, text="Confirm Attack", command=self.deal_damage, width=15, height=1, font=("Poppins", 10), bg='#444444', fg='white')
        self.confirm_attack_button.grid(pady=3, padx=4, row=0, column=3)

        self.win_button = tk.Button(self.actions_frame, text="win", command=lambda: self.game_over('You win!'), width=15, height=1, font=("Poppins", 10), bg='#444444', fg='white')
        self.win_button.grid(pady=3, padx=4, row=1, column=3)

        self.show_deck_button = tk.Button(self.actions_frame, text="Show Deck", command=self.show_deck, width=15, height=1, font=("Poppins", 10), bg='#444444', fg='white')
        self.show_deck_button.grid(pady=3, padx=4, row=1, column=1)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        # Based on difficulty, create different encounters
        self.encounters = self.create_encounters(difficulty)
    
    def create_encounters(self, difficulty):
        """Create different encounters based on the difficulty."""
        # Define base enemies (only names for now)
        base_enemies = [
            "Homework",  
            "Project",   
            "Research"
        ]

        bosses = [
            "Midterms",
            "Finals"
        ]

        # Start with an empty list of encounters
        encounters = []

        # GPA scaling logic based on difficulty
        if difficulty == "Term 1":
            # Term 1: Enemies scale from 1.0 to 5.3 (9 enemies total)
            self.turn_limit = 21
            gpa_scaling = [1.0, 1.6, 2.2, 2.8, 3.4, 4.0, 4.5, 5.1, 5.3]
            for i in range(len(gpa_scaling)):
                random = randint(0, len(base_enemies)-1)
                if i == len(gpa_scaling)-1:
                    encounters.append(Enemy(bosses[1], gpa_scaling[i]))
                elif i == len(gpa_scaling)//2:
                    encounters.append(Enemy(bosses[0], gpa_scaling[i]))
                else:
                    encounters.append(Enemy(base_enemies[random], gpa_scaling[i]))   

        elif difficulty == "Term 2":
            # Term 2: Enemies scale from 1.0 to 5.3 (7 enemies total)
            self.turn_limit = 14
            gpa_scaling = [1.0, 1.7, 2.4, 3.2, 3.9, 4.6, 5.3]
            for i in range(len(gpa_scaling)):
                random = randint(0, len(base_enemies)-1)
                if i == len(gpa_scaling)-1:
                    encounters.append(Enemy(bosses[1], gpa_scaling[i]))
                elif i == len(gpa_scaling)//2:
                    encounters.append(Enemy(bosses[0], gpa_scaling[i]))
                else:
                    encounters.append(Enemy(base_enemies[random], gpa_scaling[i]))

        elif difficulty == "Term 3":
            # Term 3: Enemies scale from 1.0 to 5.3 (5 enemies total)
            self.turn_limit = 7
            gpa_scaling = [1.0, 2.0, 2.8, 3.5, 5.3]
            for i in range(len(gpa_scaling)):
                random = randint(0, len(base_enemies)-1)
                if i == len(gpa_scaling)-1:
                    encounters.append(Enemy(bosses[1], gpa_scaling[i]))
                elif i == len(gpa_scaling)//2:
                    encounters.append(Enemy(bosses[0], gpa_scaling[i]))
                else:
                    encounters.append(Enemy(base_enemies[random], gpa_scaling[i]))

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
        self.card_buttons = {}
        for card in self.hand:
            button = tk.Button(
                self.cards_frame, 
                text=f"{card.name}\n({card.grade})",
                width=self.window_width//110, 
                height=5,
                command=lambda c=card: self.select_card(c),
                bg = '#BF1010',
                fg = '#F1C232',
                font=("Old School Adventures", 10)
            )
            self.card_buttons[card] = button  # Track card buttons
            button.pack(side="left", padx=5, pady=5)

    def select_card(self, card):
        self.message_label.config(text="Select 4 cards to deal damage!")
        """Select or deselect a card for the player."""
        if str(card) in self.selected_cards: # Deselect the card
            self.selected_cards.remove(str(card))
            self.selected_classcards.remove(card)
            self.card_buttons.get(card).config(bg = '#BF1010', fg = '#F1C232', font=("Old School Adventures", 10))
        else: # Select the card
            if len(self.selected_cards) < 4:  # Limit to 4 cards
                self.selected_cards.append(str(card))
                self.selected_classcards.append(card)
                self.card_buttons.get(card).config(bg = '#C4BFFA', fg = '#05349B', font=("Old School Adventures", 10))

        # Update the selected cards label
        self.selected_cards_label.config(text=f"Selected Cards: {', '.join(self.selected_cards)}", fg='#C4BFFA', font=("poppins",13))

        # Enable "Calculate Damage" buttons if cards are selected
        if len(self.selected_cards) == 4:
            self.message_label.config(text="Now calculate how much damage you would do and then attack!")
            self.calculate_button.config(state=tk.NORMAL)
        else:
            self.confirm_attack_button.config(state=tk.DISABLED)
            self.calculate_button.config(state=tk.DISABLED)

    def calculate_damage(self):
        """Calculate the damage based on selected cards."""
        self.buttonclicks = 0
        total_value = sum(card.value for card in self.selected_classcards)
        gpa_damage = round(total_value / 4, 1)
        self.message_label.config(text=f"Calculated Damage: {gpa_damage} GPA")
        self.confirm_attack_button.config(state=tk.NORMAL)

    def reselect_cards(self):
        """Reselect the player's cards by resetting the selected cards and allowing them to pick again."""
        for key in self.card_buttons.keys():
            self.card_buttons.get(key).config(bg = '#CC0000',
                fg = '#F1C232',
                font=("Old School Adventures", 10))
        self.selected_cards = []  # Clear the current card selection
        self.message_label.config(text="Select 4 cards to deal damage!")
        self.selected_cards_label.config(text="Selected Cards: None")  # Reset the label

        # Disable the "Next Turn" and "Calculate Damage" buttons until cards are selected
        self.confirm_attack_button.config(state=tk.DISABLED)
        self.calculate_button.config(state=tk.DISABLED)

        if self.buttonclicks == 69:
            random = randint(1, 10)
            if random == 5:
                self.show_event2_window()
            else:
                self.show_event_window()

    def update_count(self):
        self.buttonclicks += 1

    def deal_damage(self):
        self.buttonclicks = 0
        self.confirm_attack_button.config(state=tk.DISABLED)
        self.calculate_button.config(state=tk.DISABLED)
        """Deal damage to the enemy and move to the next turn."""
        if self.current_enemy:
            gpa_damage = round(sum(card.value for card in self.selected_classcards) / 4, 1)
            self.current_enemy.gpa = round(self.current_enemy.gpa - gpa_damage, 1)  # Subtract the GPA damage
            self.selected_cards = []  # Clear the current card selection
            self.selected_classcards = []
            self.selected = [str(card) for card in self.hand]
            self.selected_cards_label.config(text="Selected Cards: None")
            self.message_label.config(text=f"Dealt {gpa_damage} GPA damage to {self.current_enemy.name}")
            self.enemy_health_label.config(text=f"Enemy Health: {self.current_enemy.gpa} GPA")  # Update health label
            self.draw_hand()

        # Check if the enemy is defeated
        if self.current_enemy.gpa <= 0:
            self.current_turn += 1
            self.message_label.config(text=f"{self.current_enemy.name} defeated!")
            random = randint(1, 700)
            if random == 365:
                self.show_event_window()
            else:
                self.show_shop()
        else:
            self.next_turn()

    def next_encounter(self):
        self.selected_cards = []  # Clear the current card selection
        self.selected_classcards = []
        self.selected = [str(card) for card in self.hand]
        """Move to the next encounter or end the game."""
        if not self.encounters:
            self.game_over("You won!")
            return
        
        self.current_enemy = self.encounters.pop(0)
        self.turn_label.config(text=f"Turn: {self.current_turn} / {self.turn_limit}")
        self.selected_cards_label.config(text="Selected Cards: None")
        self.enemy_label.config(text=f"Enemy:  {self.current_enemy.name}")
        self.message_label.config(text="Select 4 cards to deal damage!")
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

    def confirm_close(self, window):
        result = tk.messagebox.askyesno("Confirm", "Are you sure you want to exit the shop?")
        if result:
            self.skip_shop(window)
            # If 'No', simply return and let the user stay in the shop window

    def close_window(self, window):
        window.destroy()  # Close the shop window

    def show_event_window(self):
        """Open event window"""
        event_window = tk.Toplevel(self.root)  # Create a new popup window
        event_window.title("Clown Encounter")
        event_window.geometry("400x300")
        # moves window to center
        x = (event_window.winfo_screenwidth() - event_window.winfo_reqwidth()) / 2 - 100
        y = (event_window.winfo_screenheight() - event_window.winfo_reqheight()) / 2 - 100
        event_window.geometry("+%d+%d" % (x, y))
        event_window.deiconify()

        name = tk.Label(event_window, text='(UN)LUCKY??')
        name.place(relx=0.5, rely=0.4, anchor='center')

        addcard = tk.Label(event_window, text='Card with Grade F added to deck!')
        addcard.place(relx=0.5, rely=0.5, anchor='center')

        self.deck.append(Card("F*CKED UP", "F"))

        btn = tk.Button(event_window, text='RIP :(', command=lambda: self.close_window(event_window))
        btn.place(relx=0.5, rely=0.6, anchor='center')

        event_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(event_window))

    def show_event2_window(self):
        """Open event 2 window"""
        event2_window = tk.Toplevel(self.root)  # Create a new popup window
        event2_window.title("Fortunate Encounter")
        event2_window.geometry("400x300")
        # moves window to center
        x = (event2_window.winfo_screenwidth() - event2_window.winfo_reqwidth()) / 2 - 100
        y = (event2_window.winfo_screenheight() - event2_window.winfo_reqheight()) / 2 - 100
        event2_window.geometry("+%d+%d" % (x, y))
        event2_window.deiconify()

        name = tk.Label(event2_window, text='LUCKY YOU!')
        name.place(relx=0.5, rely=0.4, anchor='center')

        addcard = tk.Label(event2_window, text='Card with Grade A- added to deck!')
        addcard.place(relx=0.5, rely=0.5, anchor='center')

        self.deck.append(Card("Productive Study Date", "A-"))

        btn = tk.Button(event2_window, text='cutee', command=lambda: self.close_window(event2_window))
        btn.place(relx=0.5, rely=0.6, anchor='center')

        event2_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(event2_window))

    def show_deck(self):
        """Display deck window."""
        # create a new window for the deck
        deck_window = tk.Toplevel(self.root)
        deck_window.title("Deck")

        # maximise window
        deck_window.state('zoomed')
        deck_window.update_idletasks()

        # when window close, close window
        deck_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(deck_window))

        # create frame to center cards
        cards_frame = tk.Frame(deck_window)
        cards_frame.pack(expand=True)
        cards_frame.place(relx=0.5, rely=0.5, anchor="center")

        # loop through each card in deck
        columns = 4
        for index, card in enumerate(self.deck):

            # create button for card
            button = tk.Button(
                cards_frame,
                text=f"{card.name} ({card.grade})",
                width=self.window_width//110, 
                height=5,
                bg = '#BF1010',
                fg = '#F1C232',
                font=("Old School Adventures", 10)
            )

            # calculate row and column of card
            row = index // columns
            column = index % columns

            # create button into grid
            button.grid(row=row, column=column, padx=10, pady=10)


    def show_shop(self):
        """Display a shop after defeating the boss."""
        # Create a popup window for the shop
        self.shop_window = tk.Toplevel(self.root)
        self.shop_window.title("Shop")
        self.shop_window.state("zoomed")
        pic_label = self.tk.Label(self.shop_window, image=self.photo)
        pic_label.place(x=0, y=0)

        self.shop_title=tk.Frame(self.shop_window, bg='#1B1B1B')
        self.shop_title.place(relx=0.5, rely=0.1, anchor="center")  # Position top frame in the center

        self.shop_items=tk.Frame(self.shop_window, bg='#1B1B1B')
        self.shop_items.place(relx=0.5, rely=0.5, anchor="center")  # Position top frame in the center

        self.shop_exit=tk.Frame(self.shop_window, bg='#1B1B1B')
        self.shop_exit.place(relx=0.5, rely=0.8, anchor="center")  # Position top frame in the center

        # List of items in the shop
        coursework = ["Study", "Research", "Extra Work", "Essay", "Lab Work", "Group Project", "Reading", "Quiz", " 3D Print", "Consultation", "Peer Review", "Presentation"]
        ownGrade = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
        items_for_sale = RandomnizeShopCards.shop(root, coursework, ownGrade)

        # Prevent user from closing the window with the X button
        self.shop_window.protocol("WM_DELETE_WINDOW", lambda: self.confirm_close(self.shop_window))  # Disable the close button entirely

        # Display the items for sale
        tk.Label(self.shop_title, text="Welcome to the shop!", font=("Old School Adventures", 20), bg='#1B1B1B', fg='#F1C232').pack(pady=10)



        # Display items in a 4x4 grid
        max_columns = 4  # Maximum columns per row
        row_index = 0
        col_index = 0

        for item, cost in items_for_sale.items():
            # Create the button
            button = tk.Button(
                self.shop_items,
                text=f"{item}\n({cost[1]}) - {cost[0]} gold",
                width=15,
                height=3,
                bg = '#BF1010',
                fg = '#F1C232',
                font=("Old School Adventures", 10),
                command=lambda i=item, c=cost[0], g=cost[1]: [
                    self.purchase_item(i, c, self.shop_window, items_for_sale),
                    self.deck.append(Card(i, g))
                ]
            )
            # Place the button in the grid
            button.grid(row=row_index, column=col_index, padx=5, pady=5)

            # Update row and column indices for the next button
            col_index += 1
            if col_index >= max_columns:
                col_index = 0
                row_index += 1
  

        # Option to skip shopping
        skip_button = tk.Button(
            self.shop_exit,
            text="Skip and collect bonus gold",
            command=lambda: self.skip_shop(self.shop_window)
        )
        skip_button.pack(pady=10)

    def bring_main_to_front(self):
        self.shop_window.lift()  # Raise the main window
        self.shop_window.attributes('-topmost', True)  # Keep it on top
        self.shop_window.attributes('-topmost', False)  # Allow normal behaviour afterward

    def purchase_item(self, item, cost, window, buttons):
        """Handle item purchase logic."""
        if self.wallet >= cost:
            self.wallet -= cost
            self.wallet_label.config(text=f"🪙Gold: {self.wallet}")
            messagebox.showinfo("Purchase Successful", f"Successfully purchased {item}!")
            window.destroy()
            # self.check_victory_condition()
        else:
            messagebox.showerror("Not enough gold", "You don't have enough gold for that item!")

            self.bring_main_to_front()

            # Disable all buttons to prevent retry spamming
            for btn in buttons:
                btn.config(state=tk.DISABLED)
                
                # Optionally, allow them to skip or exit the shop manually
                tk.Button(window, text="Close Shop", command=lambda: self.skip_shop(window)).pack(pady=3)


        # Allow exiting the shop screen after the choice is made
        # window.destroy()
        self.next_encounter()

    def skip_shop(self, window):
        """Handle skipping the shop and collecting bonus gold."""
        bonus_gold = 5  # The amount of gold rewarded for skipping
        self.wallet += bonus_gold
        self.wallet_label.config(text=f"Gold: {self.wallet}")
        messagebox.showinfo("Skip Shop", f"You received {bonus_gold} bonus gold! Total Gold: {self.wallet}")
        window.destroy()  # Close the shop window
        # self.check_victory_condition()
        self.next_encounter()  # Proceed to the next encounter

    def game_over(self, message):
        """Handle game over scenario."""
        # Hide the game elements and show the game over screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.game_over_screen(message)

    def game_over_screen(self, message):
        """Display a Game Over screen."""
        pic_label = self.tk.Label(self.root, image=self.winphoto)
        pic_label.place(x=0, y=0)

        # Game Over message
        game_over_label = tk.Label(self.root, text=message, font=("Old School Adventures", 25), bg='#1B1B1B', fg='#F1C232')
        game_over_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Buttons for Quit and Restart
        quit_button = tk.Button(self.root, text="Quit", command=self.quit_game, width=20, height=2, font=("Old School Adventures", 9), bg='white', fg='#05349B')
        quit_button.place(relx=0.3, rely=0.7, anchor="center")

        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, width=20, height=2, font=("Old School Adventures", 9), bg='white', fg='#05349B')
        restart_button.place(relx=0.7, rely=0.7, anchor="center")

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