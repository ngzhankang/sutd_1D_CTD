class StartScreen:
    def __init__(self, root, game, tk):
        self.root = root
        self.game = game
        self.tk = tk
        self.root.title("Choose Your Difficulty")
        self.photo = self.tk.PhotoImage(file="./assets/bgimage.png")
        self.setup_ui()

    def setup_ui(self):
        # Layout for difficulty selection
        pic_label = self.tk.Label(self.root, image=self.photo)
        pic_label.pack()

        self.welcome_label = self.tk.Label(self.root, text="'Study Up Till Death'", font=("Old School Adventures", 32))
        self.welcome_label.place(relx=0.5, rely=0.2, anchor="center")  # Center the title label

        self.title_label = self.tk.Label(self.root, text="Select Difficulty", font=("Old School Adventures", 20))
        self.title_label.place(relx=0.5, rely=0.35, anchor="center")  # Center the title label

        # Buttons for difficulty
        self.term1_button = self.tk.Button(self.root, text="Term 1 (Easy)", font=("Old School Adventures", 8), width=20, height=2, bg='#59BB7B', fg='black', command=lambda: self.start_game("Term 1"))
        self.term1_button.place(relx=0.3, rely=0.5, anchor="center")  # Center the term 1 button

        self.term2_button = self.tk.Button(self.root, text="Term 2 (Medium)", font=("Old School Adventures", 8), width=20, height=2, bg='#F8333C', fg='white', command=lambda: self.start_game("Term 2"))
        self.term2_button.place(relx=0.5, rely=0.5, anchor="center")  # Center the term 2 button

        self.term3_button = self.tk.Button(self.root, text="Term 3 (Hard)", font=("Old School Adventures", 8), width=20, height=2, bg='#FCAB10', fg='black', command=lambda: self.start_game("Term 3"))
        self.term3_button.place(relx=0.7, rely=0.5, anchor="center")  # Center the term 3 button

    def start_game(self, difficulty):
        self.game.set_difficulty(difficulty)
        self.hide_start_screen()  # Hide the start screen
        self.game.start_game()  # Start the game with the selected difficulty

    def hide_start_screen(self):
        # Remove the start screen elements gracefully
        for widget in self.root.winfo_children():
            widget.place_forget()  # Use place_forget instead of pack_forget