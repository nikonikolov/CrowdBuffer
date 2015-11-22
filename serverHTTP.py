#import datas
import datetime
#execfile("home/niko/Workspace/Beacon")
from place import *
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

p1 = Place("St. Paul's Cathedral", 1)
p2 = Place("The Shard", 2)
p3 = Place("Sushisamba", 3)

listPlaces = [p1, p2, p3]

# Enter a building
@app.route('/enterb', methods = ['GET'])
def enter_building():
	searchid = request.args.get('id', '')
	#print "before"
	idx = FindPlace(int(searchid) , listPlaces)
	#print "after"
	listPlaces[idx].PersonIn()
	#print idx
	#resp = make_response("Foo bar baz")
	resp = Response("Foo bar baz")
	resp.headers['sth'] = 'value'
	return resp
	#return 200

# Exiting a building
@app.route('/exitb', methods = ['GET'])
def exit_building():
	searchid = request.args.get('id', '')
	idx = FindPlace(searchid , listPlaces)
	listPlaces[idx].PersonOut()


# Requesting a suggestions
@app.route('/reuqestplaces', methods = ['GET'])
def request_places():
	searchid = request.args.get('id', '')
	idx = FindPlace(searchid , listPlaces)
	# Use Zun API to return stuff
	dtime = datetime.datetime.time(datetime.datetime.now())
	#return 



if __name__ == '__main__':
	# allow for changes in server without stopping it
	app.debug = True
	# host='0.0.0.0' makes it visible to other machines on the network
	#app.run(host='0.0.0.0')
	app.run()
