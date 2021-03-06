from math import sin, cos, radians, acos
from random import randrange
import datetime
import math
import matplotlib.pyplot as plt
from collections import OrderedDict

EARTH_RADIUS_IN_MILES = 3958.761
startDate = datetime.datetime(2013, 9, 20,9,00)

def random_date(start,l):
   current = start
   index = 0
   lst = []
   while l >= 0:
      current = current + datetime.timedelta(minutes=randrange(5))
      lst .append(current)
      index += 1
      l-=1
   return lst

class Location:

	def __init__(self, name, id, location_type,gps_location,avg_duration):
		self.name = name
		self.id = id
		self.location_type = location_type
		self.gps_location = gps_location
		self.avg_duration = avg_duration
		self.time_in = []
		self.time_out = []
		self.next = []

	def init_time(self) :
		self.set_time_in()
		self.set_time_out()

	def set_time_in(self):
		self.time_in =  random_date(startDate, 4000)

	def set_time_out(self):
		self.time_out = []
		for i in range(len(self.time_in)):
			self.time_out.append(self.time_in[i] + datetime.timedelta(minutes=randrange(self.avg_duration*2)))
			self.location = locations

	def compute_total_distance(self):
		self.dist = 0
		for i in range(len(locations)):
			if locations[i] != self:
				self.dist += 1/(distance(self.gps_location, locations[i].gps_location))

	def add_time_in(self, time_in, prev_id, time_out):
		if(prev_id != -1) :
			self.time_in.append(time_in)
			locations[prev_id].next.append((time_out, self))

	def add_time_out(self, time_out):
		self.time_out.append(time_out)

	def set_next(self):
		self.next = []
		for j in range(len(self.time_out)-15):
			flag = True
			rand = randrange(math.floor(self.dist))
			for i in range(len(locations)):
				if(locations[i] == self):
					continue
				if rand < ((1/distance(self.gps_location, locations[i].gps_location))*0.8):
					self.next.append(locations[i])
					flag = False
					break;
				rand -= (1/distance(self.gps_location, locations[i].gps_location))*0.8
			if flag:
				self.next.append(None)

	def plot_graph(self):
		num = 0
		cur = 0
		g = []
		sorted_time_out = list(self.time_out)
		sorted_time_out.sort()
		for i in range(len(self.time_in)):
			while(self.time_in[i] > sorted_time_out[cur]):
				num -= 1
				g.append((sorted_time_out[cur],num))
				cur += 1
			num += 1
			g.append((self.time_in[i],num))
		while(num > 1) :
			num -= 1
			g.append((sorted_time_out[cur],num))
			cur += 1
		plt.plot(*zip(*g))
		plt.show()

	def plot_hour_graph(self):
		gg = []
		for i in range (24):
			gg.append((i,0))
		num = 0
		cur = 0
		g = []
		sorted_time_out = list(self.time_out)
		sorted_time_out.sort()
		for i in range(len(self.time_in)):
			while(self.time_in[i] > sorted_time_out[cur]):
				num -= 1
				g.append((sorted_time_out[cur],num))
				cur += 1
			num += 1
			g.append((self.time_in[i],num))
		while(num > 1) :
			num -= 1
			g.append((sorted_time_out[cur],num))
			cur += 1
		curr_h = g[0][0].hour
		gg[curr_h] = (curr_h, g[0][1])
		for i in range(len(g)):
			print curr_h
			if g[i][0].hour == 0 and curr_h ==23:
				curr_h = 0
				gg[curr_h] = (curr_h, g[i][1]+gg[curr_h][1])
			elif g[i][0].hour > curr_h:
				curr_h = g[i][0].hour
				gg[curr_h] = (curr_h, g[i][1]+gg[curr_h][1])
		plt.plot(*zip(*gg))
		plt.show()


	def print_time(self):
		for x in self.time_out:
  			print x.strftime("%d/%m/%y %H:%M")


class Gps_location:

	def __init__(self, lat, longi):
		self.lat = lat
		self.longi = longi
"""
class Preferences:

	def __init__(self, max_dist, location_type):
		self.max_dist = max_dist
		self.location_type = location_type
"""

class User:

	def __init__(self, name, location):
		self.name = name
		self.location = location

def distance(location1, location2):
    lat_a = radians(location1.lat)
    lat_b = radians(location2.lat)
    delta_long = radians(location2.longi- location1.longi)
    cos_x = (
        sin(lat_a) * sin(lat_b) +
        cos(lat_a) * cos(lat_b) * cos(delta_long)
        )
    return acos(cos_x) * EARTH_RADIUS_IN_MILES


def suggestLocation(id, currentTime):
	suggest = []
	location_count = dict()
	loc = locations[id]
  	for location in locations:
  		location_count[location.name] = 0
	for i in range(len(loc.next)):
		if(abs(loc.next[0][i]- currentTime) < datetime.timedelta(minutes=60)) :
			#if loc.next[i] != None:
			location_count[loc.next[1][i].id] += 1
	d_sorted_by_value = OrderedDict(sorted(location_count.items(), key=lambda x: x[1], reverse = True))
	keyss = d_sorted_by_value.keys()
	#print keyss
	for i in range(5):
		suggest.append(keyss[i])
	return suggest


locations = []
#preferences = Preferences(10, "restaurant");
baileys = Location("baileys", 0, "restaurant", Gps_location(51.480936, -0.204203),40)
locations.append(baileys)

seven_park_place = Location("seven park place", 1, "restaurant", Gps_location(51.506295, -0.140369), 120)
locations.append(seven_park_place)

duck_and_waffle = Location("duck and waffle", 2, "restaurant", Gps_location(51.516211, -0.080881), 100)
locations.append(duck_and_waffle)

natural_history_museum = Location("natural history museum", 3, "tourism", Gps_location(51.496829, -0.176346), 150)
locations.append(natural_history_museum)

natural_science_museum = Location("natural science museum", 4, "tourism", Gps_location(51.497770, -0.174490), 150)
locations.append(natural_science_museum)

madame_tussauds = Location("madame tussauds", 5, "tourism", Gps_location(51.523030, -0.154967), 150)
locations.append(madame_tussauds)

british_museum = Location("british museum", 6, "tourism", Gps_location(51.519553, -0.126989), 150)
locations.append(british_museum)

st_paul_cathedral = Location("st paul cathedral", 7, "tourism", Gps_location(51.514006, -0.098361), 80)
locations.append(st_paul_cathedral)

sushi_samba = Location("SUSHISAMBA", 8, "restaurant", Gps_location(51.516450, -0.080978), 50)
locations.append(sushi_samba)

the_shard = Location("the shard", 9, "tourism", Gps_location(51.504539, -0.086301), 90)
locations.append(the_shard)

national_maritime_museum = Location("national maritime museum", 10, "tourism", Gps_location(51.481015, -0.005300), 90)
locations.append(national_maritime_museum)

location_a = Location("location a", 11, "restaurant", Gps_location(51.486968, -0.020824), 60)
locations.append(location_a)

location_b = Location("location b", 12, "tourism", Gps_location(51.492419, -0.010868), 120)
locations.append(location_b)
