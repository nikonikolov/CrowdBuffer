#import datas
import datetime
from place import *
from flask import Flask
from flask import request
from flask import Response
from hack import *
import demjson


p1 = Place("Bayleys Restaurant", 1)
p2 = Place("Seven Park Place", 2)
p3 = Place("Duck and Waffle", 3)
p4 = Place("Natural History Museum", 4)
p5 = Place("Madame Tussauds", 5)
p6 = Place("British Museum", 6)
p7 = Place("St. Paul's Cathedral", 7)
p8 = Place("Sushisamba", 8)
p9 = Place("The Shard", 9)
p10 = Place("National Maritime Museum", 10)


listPlaces = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


app = Flask(__name__)

# Enter a building
@app.route('/enterb', methods = ['GET'])
def enter_building():
	
	# Search for data
	searchid = request.args.get('id', '')
	searchprevid = request.args.get('prev_id', '')
	searchtime = request.args.get('time_stamp', '')
	dtime = datetime.datetime.time(datetime.datetime.now())
	locations[int(searchid)].add_time_in(dtime, int(searchprevid), searchtime)
	#print "before"
	idx = FindPlace(int(searchid) , listPlaces)
	#print "after"
	listPlaces[idx].PersonIn()
	#print idx
	resp = Response("Foo bar baz")
	resp.headers['sth'] = 'value'
	return resp

# Exiting a building
@app.route('/exitb', methods = ['GET'])
def exit_building():
	searchid = request.args.get('id', '')
	idx = FindPlace(int(searchid) , listPlaces)
	listPlaces[idx].PersonOut()
	dtime = datetime.datetime.time(datetime.datetime.now())
	locations[int(searchid)].add_time_out(dtime)

	resp = Response("Foo bar baz")
	resp.headers['sth'] = 'value'
	return resp

# Requesting a suggestions
@app.route('/reuqestplaces', methods = ['GET'])
def request_places():
	searchid = request.args.get('id', '')
	
	# Get JSON object of suggested data
	json_data = find_suggested_data(int(searchid))

	resp = Response(json_data)
	resp.headers['sth'] = 'value'
	return resp


if __name__ == '__main__':
	# allow for changes in server without stopping it
	app.debug = True
	
	# host='0.0.0.0' makes it visible to other machines on the network
	#app.run(host='0.0.0.0')
	app.run()


def find_suggested_data(id):
	#idx = FindPlace(int(searchid) , listPlaces)
	dtime = datetime.datetime.time(datetime.datetime.now())
	
	# Use Zun API to return suggestions
	suggested_data = suggestLocation(id, dtime) 

	# Encode in JSON
	json_data = demjson.encode(suggested_data)
	return json_data