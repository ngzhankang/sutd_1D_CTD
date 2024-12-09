class StartScreen:
    def __init__(self, root, game, tk):
        self.root = root
        self.game = game
        self.tk = tk
        self.root.title("Choose Your Difficulty")
        self.setup_ui()

    def setup_ui(self):
        # Layout for difficulty selection
        self.title_label = self.tk.Label(self.root, text="Select Difficulty", font=("Helvetica", 24))
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")  # Center the title label

        # Buttons for difficulty
        self.term1_button = self.tk.Button(self.root, text="Term 1 (Easy)", width=20, height=2, command=lambda: self.start_game("Term 1"))
        self.term1_button.place(relx=0.5, rely=0.4, anchor="center")  # Center the term 1 button

        self.term2_button = self.tk.Button(self.root, text="Term 2 (Medium)", width=20, height=2, command=lambda: self.start_game("Term 2"))
        self.term2_button.place(relx=0.5, rely=0.5, anchor="center")  # Center the term 2 button

        self.term3_button = self.tk.Button(self.root, text="Term 3 (Hard)", width=20, height=2, command=lambda: self.start_game("Term 3"))
        self.term3_button.place(relx=0.5, rely=0.6, anchor="center")  # Center the term 3 button

    def start_game(self, difficulty):
        self.game.set_difficulty(difficulty)
        self.hide_start_screen()  # Hide the start screen
        self.game.start_game()  # Start the game with the selected difficulty

    def hide_start_screen(self):
        # Remove the start screen elements gracefully
        for widget in self.root.winfo_children():
            widget.place_forget()  # Use place_forget instead of pack_forget