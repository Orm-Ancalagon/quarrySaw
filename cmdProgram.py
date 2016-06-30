from cmd import Cmd

class testCommand(Cmd):
	someVariable = "this is testy variable"
	
	def do_greeting(self, line):
		print("hello", someVariable)

	def do_end(self, line):
		return True
	
	def setavariable(self, line):
		somevariable = "line"

if __name__ == "__main__":
	testCommand().cmdloop()






