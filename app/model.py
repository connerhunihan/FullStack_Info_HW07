import pymongo

#gets you the handler on the mongo client
client = pymongo.MongoClient()
#choose the data base
db = client.megalab

# Choose Collection
def chooseCollection(collectionChoice):
	collection = db[collectionChoice]
	return collection

### Users ###

# Insert value
def insertUser(collection, email, username, password, first, last):
	collection.insert({"Email":email, "Username":username, "Password":password, "First":first, "Last" :last})

# Find users
def findUsers(collection):
	friends = collection.find()
	if friends.count() is not 0:
		return friends
	else:
		return []

# Update field
def updateUser(field, value):
	#???
	pass

# Append to field
def appendUser(field, value):
	#???
	pass

def display():
	return collection

### Trips ###

# Insert value
def insertTrip(collection, title, destination, participants):
	collection.insert({"Title":title, "Destination":destination, "Participants":participants})

# Find instance by username
def findTrips(collection, username):
	trips = collection.find({'Participants':username})
	return trips

# Remove trip
def removeTrip(collection,value):
	collection.remove({'Title':value})