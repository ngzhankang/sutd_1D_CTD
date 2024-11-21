# class module
class Module:

	# params: name, 
	def __init__(self, num, name, cred): #initialises module class with 3 arguments
		self._num = num # module number
		self._name = name #module name
		self._cred = cred #module credits
			
	# return module number
	def mod_num(self):
		return self._num
		
	# return module name	
	def mod_name(self):
		return self._name
	
	# return module credits	
	def mod_credits(self):
		return self._cred