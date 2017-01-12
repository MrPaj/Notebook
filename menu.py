class Menu:
	''' This is the menu and options '''
	def __init__(self):
		self.options = {
			"1" : self.show_notes,
			"2" : self.search_note,
			"0" : self.exit
			}
		
	def show_menu(self):
		''' Shows the options of the menu '''
		print ('\n' *100)
		print ('''
This is the main Menu:

1. Show all the notes.
2. Search for a note.
0. Exit the program.
''')
		
	def run(self):
		while True:
			self.show_menu()
			option= input('Please enter an option.')
			action = self.options.get(option)
			if action:
				action()
			else :
				print('{0} is not a valid option'.format(option))
				
	def show_notes(self):
		print ("we are in show notes")
		a=input()
	def search_note(self):
		print ("we are in search note")
		a=input()
	def exit(self):
		sys.exit(0)