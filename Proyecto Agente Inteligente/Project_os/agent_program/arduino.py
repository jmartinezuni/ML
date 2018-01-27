import pyfirmata
import time

board = pyfirmata.Arduino('COM18')
pin = board.get_pin('d:7:o')

def high_led():
	pin.write(1)

def low_led():
	pin.write(0)

def check_led():
	state_led = pin.read()
	if state_led:
		print 'led is active'
	if not state_led or state_led is None:
		print 'led is not active'

def close_conexion():
	pin.write(0)
	board.exit()