from SimpleCV import Display, Camera, time
from SimpleCV import *

def movement_check(x = 0,t=1):
	directionX = ""
	if x > t:
		directionX = 'Encender el foco' #Right
	if x < -1*t:
		directionX = "Apagar el foco" #Left

	if directionX is not "":
		return directionX
	else:
		return "No Motion"

def control_by_cam():
	scale_amount = (200,150)
	d = Display(scale_amount)
	cam = Camera(0)
	prev = cam.getImage().flipHorizontal().scale(scale_amount[0],scale_amount[1])
	time.sleep(0.5)
	t = 0.5
	buffer = 20
	count = 0
	while d.isNotDone():
		current = cam.getImage().flipHorizontal()
		current = current.scale(scale_amount[0],scale_amount[1])
		if( count < buffer ):
			count = count + 1
		else:
			fs = current.findMotion(prev, window=15, method="BM")
			lengthOfFs = len(fs)
			if fs:
				dx = 0
				for f in fs:
					dx = dx + f.dx
				dx = (dx / lengthOfFs)
				motionStr = movement_check(dx,t)
				current.drawText(motionStr,10,10)
		prev = current
		time.sleep(0.01)
		current.save(d)
		return motionStr

