from time import sleep
import pynput
import keyboard
import sys
import os
from pynput.keyboard import Key, Listener

KEYBOARD = pynput.keyboard.Controller()
MOUSE = pynput.mouse.Controller()
URL = "https://tellonym.me/mulockconfessions"
done = False
while not done:
	
	
	for i in range(0,40):

		MOUSE.position = (50, 470)
		MOUSE.click(pynput.mouse.Button.left, 1)
		KEYBOARD.type("Im Bored In Physics")
		MOUSE.position = (700, 570)
		MOUSE.click(pynput.mouse.Button.left, 1)
		sleep(3)
		MOUSE.position = (200, 60)
		MOUSE.click(pynput.mouse.Button.left, 1)
		KEYBOARD.type(URL)
		KEYBOARD.press(pynput.keyboard.Key.enter)
		KEYBOARD.release(pynput.keyboard.Key.enter)
		sleep(3)
		if keyboard.is_pressed('escape'):
			done = True
			break
	
	MOUSE.position = (1175, 545)
	MOUSE.click(pynput.mouse.Button.left, 1)
	MOUSE.position = (1175, 300)
	sleep(1)
	MOUSE.click(pynput.mouse.Button.left, 1)
	sleep(6)
	MOUSE.position = (1175, 545)