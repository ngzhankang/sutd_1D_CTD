# import library
# from Card import Card
import json


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


# shuffle existing deck
def shuffle_deck():

    pass
def card(name, grade):
    return set({name, (grade)})


# create starting deck
def start_deck():
    return [
            card("Homework", "B"),
            card("Study", "C"),
            card("Project", "D"),
            card("Research", "C"),
            card("Extra Credit", "B"),
            card("Extra Work", "B-"),
            card("Essay", "B-"),
            card("Lab Work", "C+"),
            card("Finals", "C+"),
            card("Midterm", "C"),
            card("Group Project", "C-"),
            card("Reading", "C-"),
            card("Quiz", "D")
            ]