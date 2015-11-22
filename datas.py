import place
import datetime

def FindPlace(placeWanted, listPlaces):
	for idx in range(len(listPlaces)):
		if listPlaces[idx].GetId() == placeWanted.GetId() : break

	return idx




p1 = Place("St. Paul's Cathedral", 1)
p2 = Place("The Shard", 2)
p3 = Place("Sushisamba", 3)

listPlaces = [p1, p2, p3]


#print datetime.datetime.time(datetime.datetime.now())
#print datetime.time(15, 8, 24, 78915)