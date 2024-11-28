import json

def load_config():
    # load datas
    with open('.datafiles/info.json', 'r') as file1, \
         open('datafiles/grades.json', 'r') as file2:
        courses, grade_dict = json.load(file1), json.load(file2)
        return courses, grade_dict

def render_deck(courses, grade_dict):
    termstr = 'Term ' + str(term)
    courelist = list(courses[termstr][0].keys())