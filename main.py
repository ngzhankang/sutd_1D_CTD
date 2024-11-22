from helperClass import card
import json
import copy

with open('datafiles\info.json', 'r') as file:
    courses = json.load(file)

with open('datafiles\grades.json', 'r') as file:
    grade_dict = json.load(file)

print('Welcome to the best GPA calculator for SUTD!')
name = input('What is your name? ')
print('Hello', name + '! Nice to meet you!')

state = True

while state == True:
  term = input('Please enter your current term (1-3): ')
  print()

  try:
    term = int(term)

    if 1 <= term <= 3:
      termstr = 'Term ' + str(term)
      courseslist = list(courses[termstr][0].keys())
      gradeslist = list(courses[termstr][0].values())

      if term == 3:
        gradeslist = gradeslist[:-2]
        courseslist3 = copy.deepcopy(courseslist)
        electivelist = []

        while state == True:
          if len(electivelist) != 0:
            print('Your current selected electives:')
            print()
            for j in range(1, len(electivelist)+1):
              print('({}) {}'.format(j, electivelist[j-1]))
            print()
          if len(electivelist) != 2:
            print('Please select your chosen elective(s) ({} left) for term 3! (1 - {}): '.format(len(courseslist3)-4, len(courseslist3)-2))
            print()
            for i in range(1, len(courseslist3)-1):
              print('({}) {}'.format(i, courseslist3[i+1]))
            print()
          print('Press (R) to reset.')
          print('Press (C) to continue.')
          print('Press (Q) to quit.')
          print()

          choice = input('Input an option: ')
          print()

          try:
            if choice == 'Q' or choice == 'q':
              print('Quitting...')
              state = False
            elif choice == 'R' or choice == 'r':
              print('Resetting...')
              courseslist3 = copy.deepcopy(courseslist)
              electivelist = []
              print()
            elif choice == 'C' or choice == 'c':
              if len(electivelist) != 2:
                print('Please select 2 electives before proceeding!')
                print()
              else:
                for course in courseslist[3:]:
                  if course not in electivelist:
                    courseslist.remove(course)
                print('Continuing...')
                print()
                break
            elif 1 <= int(choice) <= 4:
              if len(courseslist3) == len(courseslist): 
                electivelist.append(courseslist3.pop(int(choice)+1))
                print('First elective selected!')
              elif len(courseslist3) == len(courseslist)-1:
                electivelist.append(courseslist3.pop(int(choice)+1))
                print('Second elective selected!')
              else:
                print('You already selected 2 electives! Please reset (R) to reselect the electives or continue (C) on!')
              print()
                
          except:
            print('Please input a valid option!')
            print()            

      while state == True:

        print('Please select the course you want to update with your grades (1 - {}): '.format(len(courseslist)))
        for i in range(1, len(courseslist)+1):
          print('({}) {}: {}'.format(i, courseslist[i-1], gradeslist[i-1][1]))
        print()
        print('Press (C) to calculate GPA.')
        print('Press (B) to back out.')
        print('Press (Q) to quit.')
        print()

        selection = input('Input an option: ')
        print()
        try:
          if selection == 'C' or selection == 'c':
            print('Calculating GPA...')
            if any('-' in lists for lists in gradeslist):
              print('You have not updated all your grades yet! Unable to calculate...')
              print()
            else:
              gradelist = []
              for lists in gradeslist:
                gradelist.append(lists[1])
              gpa = card.calc_grade(grade_dict, gradelist)
              print('Your GPA is... \n{}'.format(gpa))
              #maybe add diff prints for diff scores (im too laze to do now)
              state = False
          elif selection == 'B' or selection == 'b':
            print('Backing out...')
            print()
            break
          elif selection == 'Q' or selection == 'q':
            print('Quitting...')
            state = False
          elif 1 <= int(selection) <= len(gradeslist):
            print('Allowed input for grades: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]'. format(*list(grade_dict.keys())))
            grade = input('Please input your grade for {}: '.format(courseslist[int(selection)-1]))
            print()
            if grade in list(grade_dict.keys()):
              gradeslist[int(selection)-1][1] = grade
              print('Updating grade...')
            else:
              print('Please only input correct grade values [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]'. format(*list(grade_dict.keys())))
            print()
          else:
            print('Please input a valid option!')
            print()
        except:
          print('Please input a valid option!')
          print()

    else:
      print('Please input a valid term number between 1 and 3!')

  except:
    print('Please input a valid term number betwe1en 1 and 3!')