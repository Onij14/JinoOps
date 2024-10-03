destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Cairo, Egypt', ['historical site', 'art']]

def get_destination_index(destination):
	destination_index = destinations.index(destination)
	return destination_index
print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))


def get_traveler_location(traveler):
	traveler_destination = traveler[1]
	traveler_destination_index = get_destination_index(traveler_destination)
	return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[] for destination in destinations]
print(attractions)

def add_attraction(destination, attraction):
	destination_index = get_destination_index(destination)
	if destination in destinations:
		attractions_for_destination = attractions[destination_index]
		attractions_for_destination.append(attraction)
	return attractions_for_destination
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)