##Create list
cities = ['Oakland', 'Atlanta', 'New York City', 'Seattle', 'Memphis', 'Miami', 'Boston', 'Los Angeles', 'Denver', 'New Orleans']
print(cities)

games = ['ff1', 'ff2', 'ff3', 'ff4', 'ff5', 'ff6', 'ff7', 'ff8', 'ff9', 'ff10']
print(games)

##Indexing
print(cities[0], cities[3], cities[-1])
print(games[1], games[3], games[-2])

##List slicing new_list = list[start index:stop index(not included)]
less_cities =  cities[0:9:2]
less_games = games[3:7]

##Changin values list[index] = new value
cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"
print(cities)

##List methods
##append() --> add value at end of list
##extend([]) --> adding lists
##insert() --> add item to specific index 

cities.append("Oakland")
cities.extend(["New York", "Los Angeles"])
cities.insert(0, "Miami")

##Deleting
##pop() --> deletes index from function call 
##clear() --> removes all current data in list
##remove() --> deletes elements called by name in func
##del list[index] --> index delete 
del cities[0]
print(cities)

cities.pop(1)
print(cities)

cities.remove("Denver")
print(cities)