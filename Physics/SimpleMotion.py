import matplotlib.pyplot as plt 
import numpy as np 
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
	
	accel = float(input("please enter Acceleration: "))
except Exception as e:
	accel = None


clear()


if deltaD == None:
	if accel == None:
		deltaD = ((initialV + finalV)/2)*deltaT
		print("Calculated Δd Using deltaT((initialV + finalV)/2)")
	elif finalV == None:
		deltaD = initialV*deltaT+(accel*(deltaT*deltaT))/2
		print("Calculated Δd Using initialV*deltaT+(a*(deltaT^2))/2")
	elif initialV == None:
		deltaD = finalV*deltaT-(accel*(deltaT*deltaT))/2
		print("Calculated Δd Using finalV*deltaT-(a*(deltaT^2))/2")
	elif deltaT == None:
		deltaD = ((finalV*finalV)-(initialV*initialV))/2*accel
		print("Calculated Δd Using ((finalV^2)-(initialV^2))/2*a")
	else:
		deltaD = ((initialV + finalV)/2)*deltaT
		print("Calculated Δd Using ((initialV + finalV)/2)*deltaT")



if finalV == None:
	if accel == None:
		finalV = 2*(deltaD/deltaT)-initialV
		print("Calculated Final Velocity Using 2*(deltaD/deltaT)-initialV")
	elif initialV == None:
		finalV = (deltaD + (accel*(deltaT*deltaT))/2)/deltaT
		print("Calculated Final Velocity Using (deltaD + (a*(deltaT^2))/2)/deltaT")
	elif deltaT == None:
		finalV = math.sqrt((initialV*initialV)+2*accel*deltaD)
		print("Calculated Final Velocity Using ((initialV*initialV)+2*a*deltaD)^0.5")
	elif deltaD == None:
		finalV = initialV + a*deltaT
		print("Calculated Final Velocity Using initialV + a*deltaT")
	else:
		finalV = initialV + accel*deltaT
		print("Calculated Final Velocity Using initialV + a*deltaT")



if initialV == None:
	if accel == None:
		initialV = 2*(deltaD/deltaT) - finalV
		print("Calculated Initial Velocity Using 2*(deltaD/deltaT) - finalV")
	elif finalV == None:
		initialV = (deltaD - (accel*(deltaT*deltaT))/2)/deltaT
		print("Calculated Initial Velocity Using (deltaD - (a*(deltaT^2))/2)/deltaT")
	elif deltaD == None:
		initialV = finalV - accel*deltaT
		print("Calculated Initial Velocity Using finalV - a*deltaT")
	elif deltaT == None:
		initialV = math.sqrt((finalV*finalV)-2*accel*deltaD)
		print("Calculated Initial Velocity Using ((finalV*finalV)-2*a*deltaD)^0.5")
	else:
		initialV = finalV - accel*deltaT
		print("Calculated Initial Velocity Using finalV - a*deltaT")



if deltaT == None:
	if accel == None:
		deltaT = deltaD/((finalV+initialV)/2) 
		print("Calculated Δt Using deltaD/((finalV+initialV)/2)")
	elif deltaD == None:
		deltaT = (finalV - initialV)/accel
		print("Calculated Δt Using (finalV - initialV)/a")
	elif initialV == None:
		deltaT = (-(finalV)+math.sqrt((finalV*finalV)-4*((-a)/2)*(-deltaD)))/(-accel)
		print("Calculated Δt Using (-(finalV)+((finalV^2)-4*((-a)/2)*(-deltaD))^0.5)/(-a)")
	elif finalV == None:
		deltaT = ((-initialV)+math.sqrt((initialV*initialV)-4*(a/2)*(-deltaD)) )/accel
		print("Calculated Δt Using ((-initialV)+((initialV^2)-4*(a/2)*(-deltaD))^0.5)/a")
	else:
		deltaT = (finalV - initialV)/accel
		print("Calculated Δt Using (finalV - initialV)/a")


	
if accel == None:
	if deltaT == None:
		accel = ((finalV*finalV)-(initialV*initialV))/(2*deltaD)
		print("Calculated Acceleration Using ((finalV^2)-(initialV^2))/(2*deltaD)")
	elif deltaD == None:
		accel = (finalV-initialV)/deltaT
		print("Calculated Acceleration Using (finalV-initialV)/deltaT")
	elif initialV == None:
		accel = -((2*(deltaD-(finalV*deltaT)))/(deltaT*deltaT))
		print("Calculated Acceleration Using -((2*(deltaD-(finalV*deltaT)))/(deltaT^2))")
	elif finalV == None:
		accel = (2*(deltaD-(initialV*deltaT)))/(deltaT*deltaT)
		print("Calculated Acceleration Using (2*(deltaD-(initialV*deltaT)))/(deltaT^2)")
	else:
		accel = (finalV-initialV)/deltaT
		print("Calculated Acceleration Using (finalV-initialV)/deltaT")

print("Δd is equal to: ",deltaD)
print("\nΔt is equal to: ",deltaT)
print("\nInitial Velocity is equal to: ",initialV)
print("\nFinal Velocity is equal to: ",finalV)
print("\nAcceleration is equal to: ",accel)





def d(t):
    return ((initialV + finalV)/2)*t
def a(t):
	return (finalV-initialV)/t
def v(t):
	return initialV + accel*t

t = np.arange(0.0, deltaT, 0.1)
plt.figure()
plt.subplot(211)
plt.plot(t, d(t), 'r')
plt.plot(t, a(t), 'k')
plt.plot(t, v(t), 'g')
plt.xlabel('Time (Seconds)')
plt.ylabel('Δd(red), v(green), a(black)') 
plt.show()