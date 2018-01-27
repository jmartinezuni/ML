import swapi
from random import randint

def planet():
	swapi.get_planet(randint(1,61))

def film():
	swapi.get_film(randint(1,7))
	
def vehicle():
	swapi.get_vehicle(randint(1,39))

def starship():
	swapi.get_starship(randint(1,37))

def specie():
	swapi.get_specie(randint(1,37))

def person():
	swapi.get_person(randint(1,87))


#61 planets
#7 films
#39 vehicles
#37 starships
#37 species
#87 people