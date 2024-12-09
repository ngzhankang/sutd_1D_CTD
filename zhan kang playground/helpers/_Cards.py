from _LoadData import LoadData

class Cards:
    def __init__(self, name, cred, imagePath):
        self._name = name # module number
        self._cred = cred #module credits
        self._imagePath = LoadData.load_img(imagePath) #path to link the image to the respective cards of the modules
		
    def mod_num(self):
        return self._num
		
	# return module name	
    def mod_name(self):
        return self._name
	
	# return module credits	
    def mod_credits(self):
        return self._cred
