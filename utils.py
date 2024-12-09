# import library
import json
from random import choice


def load_config():
    # load datas
    with open('.datafiles/info.json', 'r') as file1, \
         open('datafiles/grades.json', 'r') as file2:
        courses, grade_dict = json.load(file1), json.load(file2)
        return courses, grade_dict

def load_grades(grade):
    with open('./datafiles/grades.json', 'r') as file:
        return json.load(file)[grade]


### DECK UTILITY FUNCTIONS


def render_deck(courses, grade_dict):
    termstr = 'Term ' + str(term)
    courelist = list(courses[termstr][0].keys())


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
        print(randomnizedShopCards)
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


class Cards:
  def __init__(self):
    self.name_ls = ["Study", "Research", "Extra Work", "Essay", "Lab Work", "Group Project", "Reading", "Quiz", " 3D Print", "Consultation", "Peer Review", "Presentation"]
    self.grade_ls = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
    
  def hand(self):
    hand = {}
    for i in range(len(self.name_ls)):
      hand[self.name_ls[i]] = choice(self.grade_ls)
    return hand

cards = Cards()
hand = cards.hand()
# print(hand)