import datetime

#Keep record of the highest note id.
last_id = 0

class Note:
	''' This is a note containing the required information '''
	
	def __init__(self, memo, tags=''):
		''' initialise the note with a memo and blank tag '''
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id= last_id
		
	def match(self, filter):
		''' Returns True if filter is a substring of memo '''
		return filter in self.memo
	
	def show(self):
		'''shows the attributes of a Note '''
		print ('ID: ' +str(self.id))
		print ('Memo: ' +self.memo)
		print ('Tags: ' +self.tags)
		print ()
		

	
class Notebook:
		''' This a notebook,basically a list of Notes and operations '''
		def __init__ (self):
			self.notes =[]
		
		def add_note (self, note):
			self.notes.append(note)
		
		def find_notes (self, memo):
			return [note for note in self.notes if note.match(memo)]