# importing libs
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
import json
import random

# import helper classes
# from helpers._Cards import Cards
# from helpers._LoadData import LoadData

# class card
class Card:
    def __init__(self, module_name, grade, weightage):
        self._module_name = module_name
        self._grade = grade
        self._weightage = weightage

# game class
class Game:
    def __init__(self, data_loader):
        self._data_loader = data_loader
        self._deck = self.create__deck()
        self._hand = []
        self._grade_points = data_loader.grade_dict

    def create__deck(self):
        _deck = []
        modules = self._data_loader.courses.get("modules", [])
        for module in modules:
            card = Card(module["module_name"], module["grade"], module["weightage"])
            _deck.append(card)
        random.shuffle(_deck)
        return _deck
    
    def draw_card(self):
        if not self._deck:
            return None
        card = self._deck.pop(0)
        self._hand.append(card)
        return card
    
    def calculate_gpa(self):
        total_weighted_points = 0
        total_weightage = 0

        for card in self._hand:
            grade_point = self._grade_points.get(card.grade, 0)
            total_weighted_points += grade_point * card.weightage
            total_weightage += card.weightage

        if total_weightage == 0:
            return 0
        return round(total_weighted_points / total_weightage, 2)




# grouper class
# https://stackoverflow.com/a/17470842/12347869
class App(tk.Frame):
    def __init__(self, root, game, data_loader):
        super().__init__(root)
        self.root = root
        self.game = game
        self.data_loader = data_loader

        # setup grid layout
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.grid(column=0, row=0, sticky=('NESW'))

        self.setup_ui()
        
        
    def setup_ui(self):
        title_label = tk.Label(self, text="GPA Card Game - Single Player", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.draw_button = tk.Button(self, text="Draw Card", command=self.draw_card)
        self.draw_button.grid(row=1, column=0, pady=10)

        self.card_frame = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2)
        self.card_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")
        self.card_frame.rowconfigure(0, weight=1)
        self.card_frame.columnconfigure(0, weight=1)

        self.card_canvas = tk.Canvas(self.card_frame, bg="white", width=800, height=400)
        self.card_canvas.grid(row=0, column=0, sticky="nsew")

    def draw_card(self):
        card = self.game.draw_card()
        if not card:
            self.end_game()
            return
        self.update_card_display()

    def update_card_display(self):
        """Updates the card display area with the current _hand."""
        self.card_canvas.delete("all")

        x = 20
        for card in self.game._hand:
            gif_path = f"images/{card.module_name}.gif"
            gif_image = self.data_loader.load_img(gif_path)

            if gif_image:
                self.card_canvas.create_image(x + 40, 100, image=gif_image, anchor="nw")
                self.card_canvas.image = gif_image  # Prevent garbage collection
            else:
                self.card_canvas.create_rectangle(x, 20, x + 80, 120, fill="grey")
                self.card_canvas.create_text(x + 40, 70, text="No Image", font=("Arial", 10))

            self.card_canvas.create_text(x + 40, 130, text=f"Grade: {card.grade}", font=("Arial", 10))
            self.card_canvas.create_text(x + 40, 150, text=f"Weight: {card.weightage}", font=("Arial", 10))

            x += 100

    def end_game(self):
        """Displays the final GPA and ends the game."""
        gpa = self.game.calculate_gpa()
        messagebox.showinfo("Game Over", f"Game Over! Your final GPA is {gpa:.2f}")
        self.root.destroy()

        # self.title("GPA Calculator")

        # setting the position where the window will init first
        # https://www.geeksforgeeks.org/how-to-center-a-window-on-the-screen-in-tkinter/
        self.screen_width, self.screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        self.x, self.y = (self.screen_width - self.winfo_reqwidth()) // 2, (self.screen_height - self.winfo_reqheight()) // 2
        self.geometry(f"+{self.x}+{self.y}")
        

        # run the main application over here
        self.mainloop()


# loadData class
class LoadData(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.courses = self.load_json('../datafiles/info.json')
        self.grade_dict = self.load_json('../datafiles/grades.json')
        self.CardImg = self.load_img('../datafiles/image1.gif')

    # function to _handle json loading
    def load_json(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'File not found: {filename}')
            return {}

    # function to _handle image loading
    def load_img(self, filename):
        try:
            rawCard = tk.PhotoImage(filename)
            # resized = rawCard.resize((250,250))
            return rawCard
        except FileNotFoundError:
            print(f'Image not found: {filename}')
            return None

        
def main():
    root = tk.Tk()
    root.title("Single-Player GPA Card Game")

    data_loader = LoadData(root)
    game = Game(data_loader)
    game_ui = App(root, game, data_loader)

    root.mainloop()



if __name__ == '__main__':
    # call the grouper class
    # https://stackoverflow.com/a/75706167/12347869
    main()