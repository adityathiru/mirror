class requirements_generator:
	def __init__(self, requirements_dict):
		self.requirements_dict = requirements_dict
		self.path = ""
	def display_requirements_dict(self):
		print(self.requirements_dict)

	def python_modules_requirements(self):
		f = open(self.path+"./requirements.txt",'w+')
		for i in self.requirements_dict["pylibs"]:
			print(i)
			f.write(i+"\n")

if __name__ == '__main__':
	# requirements_generator({"1":1}).display_requirements_dict()
	requirements_generator({"pylibs":["1","2","3"]}).python_modules_requirements()