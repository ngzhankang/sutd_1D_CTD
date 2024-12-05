import json
import tkinter as tk

# class to load all images and data files, as well as to generate and shuffle cards
class LoadData:
    def __init__(self):
        self.courses = self.load_json('datafiles/info.json')
        self.grade_dict = self.load_json('datafiles/grades.json')
        self.CardImg = self.load_img('datafiles/image1.gif')

    # function to handle json loading
    def load_json(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'File not found: {filename}')
            return {}

    # function to handle image loading
    def load_img(self, filename):
        try:
            rawCard = tk.PhotoImage(filename)
            resized = rawCard.resize((250,250))
            return resized
        except FileNotFoundError:
            print(f'Image not found: {filename}')
            return None
        
    # function to generate decks
    def create_deck(self, ):
        
        # make deck global because we need it later
        global deck
        deck = []

        