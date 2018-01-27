import aiml
import os

path = os.getcwd()+'\data'
os.chdir(path)

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
	msg = raw_input("Enter your message >> ")
	if msg == "quit" or msg == 'bye':
		exit()
	else:
		print kernel.respond(msg)
		#change to other decoders