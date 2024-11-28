#  import code.py file from helper folder to use code from code.py file
from . import code
# import json library to read json files
import json
# import copy library to use deepcopy to copy lists
import copy

# open info.json file in datafiles folder to read the content as a dictionary
with open('datafiles\info.json', 'r') as file:
    courses = json.load(file)

# open grades.json file in datafiles folder to read the content as a dictionary
with open('datafiles\grades.json', 'r') as file:
    grade_dict = json.load(file)

# introduction to gpa calculator
print('Welcome to the best GPA calculator for SUTD!')
# asks user for name, and greets the user
name = input('What is your name? ')
print('Hello', name + '! Nice to meet you!')

# create variable to be able to quit while loop whenever needed
state = True

# while loop to ensure inputs continually run until user wants to quit programme or programme provides final result
while state == True:
  # enquire user on current term he/she is in to know what modules they are taking and whether they have electives to choose from
  term = input('Please enter your current term (1-3): ')
  #newline after input
  print()
  
  # try except statement to ensure user's term input is an int else return error print and asks user to input again
  try:
    term = int(term)

    # if else statement to ensure term user inputs is within terms 1 to 3 which are the valid terms this programme can calculate
    # else returns error print and asks user to input again
    if 1 <= term <= 3:
      # creates string of term number so that the correct term can be referenced to in courses dictionary retrieved from json file
      termstr = 'Term ' + str(term)
      # retrieves relevant list of courses and grades based on term user is in from courses dictionary for easier access by programme
      courseslist = list(courses[termstr][0].keys())
      gradeslist = list(courses[termstr][0].values())

      # special case for term 3 users as programme needs user to select what electives they have chosen for term 3
      if term == 3:
        # gradeslist should have 4 elements as only 4 main modules are taken in term 3
        gradeslist = gradeslist[:-2]
        # create deep copy of courselist so copy can be edited without editing the original course list
        courseslist3 = copy.deepcopy(courseslist)
        # empty list created to register electives chosen by user
        electivelist = []

        # second while loop to ensure that user is not brought back to start of program whenever there is an error and instead goes back to the start of the elective choosing part
        while state == True:
          # shows user current electives user has chosen so that user knows what he/she has chosen
          # only shows once user has chosen at least one elective to not clutter user's screen
          if len(electivelist) != 0:
            print('Your current selected electives:')
            print()
            for j in range(1, len(electivelist)+1):
              print('({}) {}'.format(j, electivelist[j-1]))
            print()
          # shows user the electives that he/she has not chosen
          # will not be shown once the user has chosen two electives as he/she does not need to look at the remaining electives and lessens clutter on screen for user
          if len(electivelist) != 2:
            print('Please select your chosen elective(s) ({} left) for term 3! (1 - {}): '.format(len(courseslist3)-4, len(courseslist3)-2))
            print()
            for i in range(1, len(courseslist3)-1):
              print('({}) {}'.format(i, courseslist3[i+1]))
            print()
          # shows user 3 other inputs user can input to run other functions of program
          # reset to reset their choices, continue to continue on after selecting their two electives and quit to quit the entire program
          print('Press (R) to reset.')
          print('Press (C) to continue.')
          print('Press (Q) to quit.')
          print()

          # asks user for input
          choice = input('Input an option: ')
          print()

          # try except statement to ensure user's input is an int else return error print and asks user to input again
          try:
            # if elif else statement to ensure user's input is a valid input else return error print and asks user to input again
            # if user inputs q, whole program will be shut down if they do not want to run the program anymore
            if choice.upper() == 'Q':
              print('Quitting...')
              state = False
            # if user inputs r, their choice of electives will be reset in case they chose the wrong electives
            elif choice.upper() == 'R':
              print('Resetting...')
              courseslist3 = copy.deepcopy(courseslist)
              electivelist = []
              print()
            # if user inputs c, user will continue on to the next part of the program where they can calculate their GPA
            elif choice.upper() == 'C':
              # checks if user has selected two electives before allowing user to proceed
              if len(electivelist) != 2:
                print('Please select 2 electives before proceeding!')
                print()
              # if user has selected two electives, original list of courses will be updated to remove the 2 electives user is not taking
              # proceeds on to next part of program once list of course is updated
              else:
                for course in courseslist[2:]:
                  if course not in electivelist:
                    courseslist.remove(course)
                print('Continuing...')
                print()
                break
            # checks to see if user selects and option between 1 and 4 as there is only 4 elective options to choose from
            elif 1 <= int(choice) <= 4:
              # checks if this is the first or second elective chosen to print approriate response
              # also appends to list of electives the elective user has chosen for easier access in other parts of code
              # error will be printed if user tries to select more than two electives
              if len(courseslist3) == len(courseslist): 
                electivelist.append(courseslist3.pop(int(choice)+1))
                print('First elective selected!')
              elif len(courseslist3) == len(courseslist)-1:
                electivelist.append(courseslist3.pop(int(choice)+1))
                print('Second elective selected!')
              else:
                print('You already selected 2 electives! Please reset (R) to reselect the electives or continue (C) on!')
              print()
          
          #error print occuring when there is any errors occuring
          except:
            print('Please input a valid option!')
            print()            

      # third while loop to ask user to input their grades and ensure program doesn't loop back to start of program
      while state == True:
        # shows user their modules and enquires user on their grades for each module
        print('Please select the course you want to update with your grades (1 - {}): '.format(len(courseslist)))
        for i in range(1, len(courseslist)+1):
          print('({}) {}: {}'.format(i, courseslist[i-1], gradeslist[i-1][1]))
        print()
        print('Press (C) to calculate GPA.')
        print('Press (B) to back out.')
        print('Press (Q) to quit.')
        print()

        # enquire user for an input to know what user wants to do
        selection = input('Input an option: ')
        print()
        # try except statement to ensure user's input is an int else return error print and asks user to input again
        try:
          # allows user to calculate their grades once they are done inputting all their grades
          if selection.upper() == 'C':
            print('Calculating GPA...')
            # checks if user has filled up all the grades before proceeding to calculate
            if any('-' in lists for lists in gradeslist):
              print('You have not updated all your grades yet! Unable to calculate...')
              print()
            # calculate user's GPA by running the calc_grade function
            else:
              gradelist = []
              for lists in gradeslist:
                gradelist.append(lists[1])
              gpa = code.calc_grade(grade_dict, gradelist)
              print('Your GPA is... \n{}'.format(gpa))
              # maybe add diff prints for diff scores (im too laze to do now)
              state = False
          # allows user to head back to reselect their term
          elif selection.upper() == 'B':
            print('Backing out...')
            print()
            break
          # allows user to quit the entire program
          elif selection.upper() == 'Q':
            print('Quitting...')
            state = False
          # displays to user the valid grade inputs that can be inputted when the user chooses a module to update their grades
          elif 1 <= int(selection) <= len(gradeslist):
            print('Allowed input for grades: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]'. format(*list(grade_dict.keys())))
            grade = input('Please input your grade for {}: '.format(courseslist[int(selection)-1]))
            print()
            if grade in list(grade_dict.keys()):
              # updates grades in gradeslist
              gradeslist[int(selection)-1][1] = grade
              print('Updating grade...')
            # print error statement to inform user wrong grade was inputted
            else:
              print('Please only input correct grade values [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]'. format(*list(grade_dict.keys())))
            print()
          # print error statement to inform user that that is not a valid option selected
          else:
            print('Please input a valid option!')
            print()
        # print error statement to inform user that that is not a valid option selected if any errors occur
        except:
          print('Please input a valid option!')
          print()

    #error print occuring if input is not between 1 and 3
    else:
      print('Please input a valid term number between 1 and 3!')

  #error print occuring when there is any errors occuring
  except:
    print('Please input a valid term number between 1 and 3!')