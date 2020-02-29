#created 2.29.2020

import vrep
import sys

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID != -1:
	print("Connection Estabilished")
	
else:
	print("Connection Not Sucessful")
	sys.exit("Could Not Conect")


vrep.simxGetObjectHandle(clientID,,simx_opmode_blocking)
