from utils import load_grades

# class module
class Card:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade 
		self.value = load_grades(grade)

	def __str__(self):
		return f"{self.name} ({self.grade})"
			
# 	# return module number
# 	def mod_num(self):
# 		return self._num
		
# 	# return module name	
# 	def mod_name(self):
# 		return self._name
	
# 	# return module credits	
# 	def mod_credits(self):
# 		return self._cred

# # function to calculate grades
# def calc_grade(grade_dict, gradelist):
# 	total_credit = 0
# 	# add total grade scores based on what the scores are with relation to the grades to calculate the GPA
# 	for elem in gradelist:
# 		total_credit += grade_dict[elem]*12
# 	GPA = round(total_credit/(4*12), 2)
# 	return GPA
