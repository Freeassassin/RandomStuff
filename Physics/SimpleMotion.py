import math
try:
	deltaT = int(input("please enter delata T: "))	
except Exception as e:

	deltaT = None


try:
	deltaD = int(input("please enter delata D: "))
except Exception as e:
	deltaD = None


try:
	initialV = int(input("please enter initial V: "))
	
except Exception as e:
	initialV = None
try:
		
	finalV = int(input("please enter final V: "))
except Exception as e:
	finalV = None
try:
	
	a = int(input("please accelaration: "))
except Exception as e:
	a = None



if deltaD == None:

	if a == None:
			deltaD = ((initialV + finalV)/2)*deltaT
	elif finalV == None:
		deltaD = initialV*deltaT+(a*(deltaT^2))/2
	elif initialV == None:
		deltaD = finalV*deltaT-(a*(deltaT^2))/2
	elif deltaT == None:
		deltaD = (finalV^2-initialV^2)2*a




if finalV == None:

	if a == None:
		
		finalV = 2*(deltaD/deltaT) - initialV

	elif initialV == None:

		finalV = (deltaD + (a*(deltaT^2))/2)/deltaT
	
	elif deltaT == None:

		finalV = math.sqrt(initialV^2+2*a*deltaT)

	elif deltaD == None:

		finalV = initialV + a*deltaT

if initialV == None:
	if a == None:

		initialV = 2*(deltaD/deltaT) - finalV

	elif finalV == None:

		initialV = (deltaD - (a*(deltaT^2))/2)/deltaT

	elif deltaD == None:

		initialV = finalV - a*deltaT

	elif deltaT == None:

		initialV = math.sqrt(finalV^2-2*a*deltaD)

if deltaT == None:

	
if a == None:



print(deltaD,deltaT,initialV,finalV,accelaration)


