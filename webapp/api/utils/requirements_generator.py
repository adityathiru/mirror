import os


class RequirementsGenerator:
	def __init__(self, requirements_dict, requirements_path):
		self.requirements_dict = requirements_dict
		self.path = requirements_path

	def display_requirements_dict(self):
		print(self.requirements_dict)

	def python_modules_requirements(self):
		requirements_path = os.path.join(self.path, "requirements.txt")
		with open(requirements_path, 'w') as f:
			f.writelines('\n'.join(self.requirements_dict["pylibs"]))
		return requirements_path


if __name__ == '__main__':
	RequirementsGenerator({"pylibs": ["sckikit-learn", "numpy", "matplotlib"]}, '').python_modules_requirements()