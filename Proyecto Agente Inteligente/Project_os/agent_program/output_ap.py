from commands import commands
from input_ap import get_match
import arduino
import twitter
#import facebook
import opencv
import scrapy
import swapi

def arduino_to_action(text):
	try:
		if get_match(text, 'arduino')[0]: # devuelve (bool, index_function)
			index = get_match(text, 'arduino')[1]
			if index == 0:
				arduino.high_led()
			if index == 1:
				arduino.low_led()
			if index == 2:
				arduino.check_led()
	except:
		pass


def twitter_to_action(text):
	try:
		if get_match(text, 'twitter')[0]:
			index = get_match(text, 'twitter')[1]
			if index == 0:
				twitter.post_tweet(['@rokiier'], 'bots are awesome!') #aca usar expresiones regulares para personalizar to_user
			if index == 1:
				txt = twitter.read_tweet(True)
				arduino_to_action(txt)
			if index == 2:
				txt = twitter.get_tweet('starwars')
				arduino_to_action(txt)
			if index == 3:
				twitter.get_trends('local')
	except:
		pass

def cv_to_action(text):
	try:
		if get_match(text, 'opencv')[0]:
			index = get_match(text, 'opencv')[1]
			if index == 0:
				opencv.control_by_cam() 
				#arduino_to_action(txt)
		
	except:
		pass

def facebook_to_action(text):
	try:
		if get_match(text, 'facebook')[0]:
			index = get_match(text, 'facebook')[1]
			if index == 0:
				facebok.get_posts()

	except:
		pass

def scrapy_to_action(text):
	try:
		if get_match(text, 'scrapy')[0]:
			index = get_match(text, 'scrapy')[1]
			if index == 0:
				scrapy.data_from_reddit()
			if index == 1:
				scrapy.data_from_itebooks()
	except:
		pass

def swapi_to_action(text):
	try:
		if get_match(text, 'swapi')[0]:
			index = get_match(text, 'swapi')[1]
			if index == 0:
				i = swapi.get_planet(randint(1,61))
				print i
			if index == 1:
				i = swapi.get_film(randint(1,7))
				print i
			if index == 2:
				i = swapi.get_vehicle(randint(1,39))
				print i
			if index == 3:
				i = swapi.get_starship(randint(1,37))
				print i
			if index == 4:
				i = wapi.get_specie(randint(1,37))
				print i
			if index == 5:
				i =  swapi.get_person(randint(1,87))
				print i
	except:
		pass

