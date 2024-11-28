# class module
class Card:
	def __init__(self, name, cred, imagePath): #initialises module class with 3 arguments
		self._name = name # module number
		self._cred = cred #module credits
		self._imagePath = imagePath #path to link the image to the respective cards of the modules
			
	# return module number
	def mod_num(self):
		return self._num
		
	# return module name	
	def mod_name(self):
		return self._name
	
	# return module credits	
	def mod_credits(self):
		return self._cred

# function to calculate grades
def calc_grade(grade_dict, gradelist):
	total_credit = 0
	# add total grade scores based on what the scores are with relation to the grades to calculate the GPA
	for elem in gradelist:
		total_credit += grade_dict[elem]*12
	GPA = round(total_credit/(4*12), 2)
	return GPA
