import math
import os
clear = lambda : os.system('cls')

try:
	deltaT = float(input("please enter Δt: "))	
except Exception as e:

	deltaT = None


try:
	deltaD = float(input("please enter Δd: "))
except Exception as e:
	deltaD = None


try:
	initialV = float(input("please enter Initial Velocity: "))
	
except Exception as e:
	initialV = None
try:
		
	finalV = float(input("please enter Final Velocity: "))
except Exception as e:
	finalV = None
try:
	
	a = float(input("please enter Acceleration: "))
except Exception as e:
	a = None


clear()


if deltaD == None:
	if a == None:
		deltaD = ((initialV + finalV)/2)*deltaT
	elif finalV == None:
		deltaD = initialV*deltaT+(a*(deltaT*deltaT))/2
	elif initialV == None:
		deltaD = finalV*deltaT-(a*(deltaT*deltaT))/2
	elif deltaT == None:
		deltaD = ((finalV*finalV)-(initialV*initialV))/2*a
	else:
		deltaD = ((initialV + finalV)/2)*deltaT



if finalV == None:
	if a == None:
		finalV = 2*(deltaD/deltaT)-initialV
	elif initialV == None:
		finalV = (deltaD + (a*(deltaT*deltaT))/2)/deltaT
	elif deltaT == None:
		finalV = math.sqrt((initialV*initialV)+2*a*deltaD)
	elif deltaD == None:
		finalV = initialV + a*deltaT
	else:
		finalV = initialV + a*deltaT



if initialV == None:
	if a == None:
		initialV = 2*(deltaD/deltaT) - finalV
	elif finalV == None:
		initialV = (deltaD - (a*(deltaT*deltaT))/2)/deltaT
	elif deltaD == None:
		initialV = finalV - a*deltaT
	elif deltaT == None:
		initialV = math.sqrt((finalV*finalV)-2*a*deltaD)
	else:
		initialV = finalV - a*deltaT



if deltaT == None:
	if a == None:
		deltaT = deltaD/((finalV+initialV)/2) 
	elif deltaD == None:
		deltaT = (finalV - initialV)/a
	elif initialV == None:
		deltaT = (-(finalV)+math.sqrt((finalV*finalV)-4*((-a)/2)*(-deltaD)) )/(-a)
	elif finalV == None:
		deltaT = ((-initialV)+math.sqrt((initialV*initialV)-4*(a/2)*(-deltaD)) )/a
	else:
		deltaT = (finalV - initialV)/a


	
if a == None:
	if deltaT == None:
		a = ((finalV*finalV)-(initialV*initialV))/(2*deltaD)
	elif deltaD == None:
		a = (finalV-initialV)/deltaT
	elif initialV == None:
		a = -((2*(deltaD-(finalV*deltaT)))/(deltaT*deltaT))
	elif finalV == None:
		a = (2*(deltaD-(initialV*deltaT)))/(deltaT*deltaT)
	else:
		a = (finalV-initialV)/deltaT

print("Δd is equal to: ",deltaD)
print("\nΔt is equal to: ",deltaT)
print("\nInitial Velocity is equal to: ",initialV)
print("\nFinal Velocity is equal to: ",finalV)
print("\nAcceleration is equal to: ",a)


