1. create a scene

2. copy all the files in 
C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\python\python
to the working directory 

3. copy remoteApi.dll in
C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\lib\lib\Windows\64Bit
to the working directory

4. Add 
simRemoteApi.start(19999)
in anywhwre in a child script in VREP. This command can be found inside simpleTest.py

5. Then add this to your custom code to initialize

import vrep
import sys

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID != -1:
	print("Connection Estabilished")
	
else:
	print("Connection Not Sucessful")
	sys.exit("Could Not Conect")

6.Sart coding (Run the python file when the simulation is running)

7. Always look for 
https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm
https://www.coppeliarobotics.com/helpFiles/en/remoteApiConstants.htm

