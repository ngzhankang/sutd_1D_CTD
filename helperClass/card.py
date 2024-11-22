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

def calc_grade(grade_dict, gradelist):
	total_credit = (grade_dict[gradelist[0]]*12) + (grade_dict[gradelist[1]]*12) + (grade_dict[gradelist[2]]*12) + (grade_dict[gradelist[3]]*12)
	GPA = total_credit/(4*12)
	return GPA
