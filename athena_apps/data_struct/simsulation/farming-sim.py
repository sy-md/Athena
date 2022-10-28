class node: # plant
	def __init__(self,val=None):
		self.plant = val
		self.next = None

class linkedlist: # plot
	def __init__(self):
		self.fld = [[]]
		self.nxfld = None

class farm:
	def __init__(self):
		self.tick = 1
		self.bank = 50
		self.inventory = {}
		self.type = { "dirt" : "#","water" : "~" }

frm = farm()
fld = linkedlist()

tmp = [] #json



