from output_ap import arduino_to_action
from output_ap import twitter_to_action
from output_ap import facebook_to_action
from output_ap import cv_to_action
from output_ap import scrapy_to_action
from output_ap import swapi_to_action
from input_ap import machine_recognition

EXIT = False

while not EXIT:
    text = machine_recognition()
    text = raw_input('>>>')
    arduino_to_action(text)
    twitter_to_action(text)
    facebook_to_action(text)
    cv_to_action(text)
    scrapy_to_action(text)
    swapi_to_action(text)

    if text.lower() == 'salir':
        EXIT = True