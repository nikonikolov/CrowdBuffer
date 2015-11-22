class Place:
	"Common Class to Store Place information and methods"

	def __init__(self, name, idplace):
		self.name = name
		self.id = idplace
		self.count = 0

	def GetCount(self):
		return self.count

	def GetId(self):
		return self.id

	def GetName(self):
		return self.name

	def PersonIn(self):
		self.count +=1

	def PersonOut(self):
		self.count -=1
		if self.count < 0: self.count = 0

	def Display(self):
		print "Name: " + self.name + " Id: " + self.id + " Count: " + self.count

def FindPlace(placeWanted, listPlaces):
	#print 'hello'
	for idx in range(len(listPlaces)):
		#print idx
		if listPlaces[idx].GetId() == placeWanted : break

	return idx





