# import library
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