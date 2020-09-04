import pystray
import networkscan
from time import sleep
from random import randint 
from subprocess import check_output
from PIL import Image, ImageDraw, ImageFont
from pystray import Menu as menu, MenuItem as item
WIDTH = 800
HEIGHT = 800
WhiteDevices = []
BlackDevices = []
connectedDevices = []
COLORS = ["black","red","green","blue"]
FONT = ImageFont.truetype("arial.ttf", 600)

MACWHITELIST = [
("ac-87-a3-35-33-3c","IMac"),
("50-02-91-46-d1-76","Smart Light"),
("50-02-91-46-c0-32","Smart Light"),
("84-f3-eb-dd-5d-a3","Smart Light"),
("84-f3-eb-dd-c6-31","Smart Light"),
("44-07-0b-30-4f-05","Google Home"),
("f0-ef-86-41-50-0a","chromecast"),
("d6-4a-8c-47-f8-50","Pixel 2XL")]

MACBLACKLIST = [
("84-41-67-c7-14-70","Rene Old Iphone"),
("20-e8-74-82-8f-2d","Rene Iphone"),
("4c-74-bf-08-23-7f","Mom Iphone"),
("","Mom Tablet")]

def network_scan():

	global WhiteDevices 
	global BlackDevices 
	global connectedDevices 

	my_scan = networkscan.Networkscan("192.168.0.0/24")

	my_scan.run()

	aprResponse = str(check_output("arp -a", shell=True).decode()).split("\r\n")

	WhiteDevices = []
	BlackDevices = []
	connectedDevices = []

	for i in range(4,len(aprResponse)-1):

		if aprResponse[i].split()[2] == "dynamic":
		
			connectedDevices.append(aprResponse[i].split())

	for device in connectedDevices:

		for mac in MACBLACKLIST:

			if device[1] == mac[0]:

				device[2] = "black"

				device.append(mac[1])
				
				break

		for mac in MACWHITELIST:

			if device[1] == mac[0]:

				device[2] = "white"

				device.append(mac[1])

				break

	for device in connectedDevices:

		if device[2] == "black":
		
			BlackDevices.append(device)
		
		elif device[2] == "white":
		
			WhiteDevices.append(device)

		else:
		
			device[2] = "black"
		
			device.append("Unkown Device")
		
			BlackDevices.append(device) 

def make_icon():
	
	network_scan()

	pic = Image.new('RGB', (WIDTH, HEIGHT), COLORS[randint(0,3)])

	d = ImageDraw.Draw(pic)

	d.text((200,100), str(len(BlackDevices)), fill=(255,255,255,255), font= FONT)

	return pic

def fillList(connectedDevices=None,i=None,j=None):

	if i != None:

		return connectedDevices[i][j]

def btnpress():

	pass

def setup(icon):

	icon.visible = True
	while True:
		sleep(30)

		icon.visible = False
		icon.icon = make_icon()
		icon.visible = True
		icon.menu = menu(
			item("White Devices",
				menu(lambda: ( item("Ip: {} Mac: {} Device: {}".format(fillList(WhiteDevices,i,0),fillList(WhiteDevices,i,1),fillList(WhiteDevices,i,3)), btnpress())for i in range(0,len(WhiteDevices)))
					)
				),

			item("Black Devices",
				menu(lambda: ( item("Ip: {} Mac: {} Device: {}".format(fillList(BlackDevices,i,0),fillList(BlackDevices,i,1),fillList(BlackDevices,i,3)), btnpress())for i in range(0,len(BlackDevices)))
					)
				)
			)
		
WHicon = pystray.Icon('Whos Home?',make_icon(),"Whos Home?",menu= menu(
	item("White Devices",
		menu(lambda: ( item("Ip: {} Mac: {} Device: {}".format(fillList(WhiteDevices,i,0),fillList(WhiteDevices,i,1),fillList(WhiteDevices,i,3)), btnpress())for i in range(0,len(WhiteDevices)))
			)
		),

	item("Black Devices",
		menu(lambda: ( item("Ip: {} Mac: {} Device: {}".format(fillList(BlackDevices,i,0),fillList(BlackDevices,i,1),fillList(BlackDevices,i,3)), btnpress())for i in range(0,len(BlackDevices)))
			)
		)
	))

WHicon.run(setup)

WHicon.stop()