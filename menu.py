import sys
import notebook

class Menu:
	''' This is the menu and options '''
	def __init__(self):
		self.options = {
			"1" : self.create_note,
			"2" : self.show_notes,
			"3" : self.search_note,
			"4" : self.delete_note,
			"0" : self.exit
			}
		self.nbook = notebook.Notebook()
		
	def show_menu(self):
		''' Shows the options of the menu '''
		print ('\n' *100)
		print ('''
This is the main Menu:

1. Create note.
2. Show all the notes.
3. Search for a note.
4. Delete a note.
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
		print ("See below the notes we have")
		for note in self.nbook.notes:
			note.show()
		a=input()
		
	def search_note(self):
		word = input ("Please enter word to search for: ")
		found_notes= self.nbook.find_notes(word)
		if found_notes:
			for note in self.nbook.find_notes(word):
				note.show()
		else :
			print ("nothing found")
		a=input()
		
	def create_note(self):
		body = input("Please introduce the body of the note: ")
		tags = input("Please introduce any tags (split by comma) for this note: ")
		self.nbook.add_note(notebook.Note(body,tags))
		
	def delete_note(self):
		id= input("Please introduce the id of the note you want to delete: ")
			
		
	def exit(self):
		sys.exit(0)
		
if __name__ == "__main__":
	Menu().run()