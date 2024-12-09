# import library
import json
from random import choice

def load_grades(grade):
    with open('./datafiles/grades.json', 'r') as file:
        return json.load(file)[grade]

class Card:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade 
		self.value = load_grades(grade)

	def __str__(self):
		return f"{self.name} ({self.grade})"

class RandomnizeShopCards:
    def __init__(self, coursework, ownGrade):
        self.coursework = coursework
        self.ownGrade = ownGrade
    
    def shop(self, coursework, ownGrade):
        randomnizedShopCards = {}
        for i in range(len(coursework)):
            randomGrade = choice(ownGrade)
            randomnizedShopCards[coursework[i]] = [load_grades(randomGrade), randomGrade]
        return randomnizedShopCards

# create starting deck
def start_deck():

    return [
            Card("Homework", "B"),
            Card("Study", "C"),
            Card("Project", "D"),
            Card("Research", "C"),
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