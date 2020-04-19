import numpy as np
from PIL import ImageGrab
import pynput
import cv2
import time
import os
from pynput.keyboard import Key, Listener
from math import sqrt
from collections import Counter

KEYBOARD = pynput.keyboard.Controller()

last_time = time.time()

time.sleep(2)

clear = lambda: os.system('cls')

def cal_distance(x1,y1,x2,y2):

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	return processed_img

def get_map(image):
    game_map = []
    for i in range(0,20):
        row = []
        for j in range(0,10):
            if image[15+(i*30)][15+(j*30)] > 50:
                row.append(1)
            elif 50 > image[15+(i*30)][15+(j*30)] > 0:
                row.append(2)
            else:
                row.append(0)
        game_map.append(row)

    return game_map

def get_shape(game_map):

    shape = []
    for j in range(0,20):
        for i in range(0,10):
            if game_map[j][i] == 2:
                shape.append([i+1,j+1])
    x = [cal_distance(shape[0][0],shape[0][1],shape[1][0],shape[1][1]),
    cal_distance(shape[1][0],shape[1][1],shape[2][0],shape[2][1]),
    cal_distance(shape[2][0],shape[2][1],shape[3][0],shape[3][1]),
    cal_distance(shape[3][0],shape[3][1],shape[0][0],shape[0][1])]

    if x == [1.0,1.0,1.0,3.0]:
        shape = 0
    elif x ==[1.0,1.4142135623730951,1.0,1.4142135623730951]:
        shape = 1
    else:
        shape = 2

    return shape

def count_zeros(game_map):

    zeros = 0
    heightSET = False
    for j in range(0,16):
        for i in range(0,10):
            if game_map[j+4][i] == 0:
                zeros += 1
            else:
                if not heightSET:
                    height = -1*(j-16)
                    heightSET = True

    return zeros,height

def determine_action(actions):
    #min(data, key = lambda t: t[1])
    best_action = actions[0]
    for i in actions:
        if i[2] == min([i[2],best_action[2]], key = lambda t: t[1]):
            best_action = i

    action = best_action

    return action


while(True):
    
    for i in range(0,4):
        KEYBOARD.press(pynput.keyboard.Key.left)
        KEYBOARD.release(pynput.keyboard.Key.left)
        time.sleep(0.005)                
    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
    printscreen = process_img(printscreen)
    game_map = get_map(printscreen)
    shape = get_shape(game_map)


    actions = []

    if shape == 0:

        for i in range(0,2):
            printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
            printscreen = process_img(printscreen)  
            game_map = get_map(printscreen)
            
            if i == 0:
            
                for j in range(0,6):
                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    game_map = get_map(printscreen)

                    actions.append([i,j,count_zeros(game_map)])

                    KEYBOARD.press(pynput.keyboard.Key.right)
                    KEYBOARD.release(pynput.keyboard.Key.right)
                    time.sleep(0.005) 

                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    
                    game_map = get_map(printscreen)    
                    

                
                for i in range(0,6):

                    KEYBOARD.press(pynput.keyboard.Key.left)
                    KEYBOARD.release(pynput.keyboard.Key.left)
                    time.sleep(0.005)            

            if i == 1:

                for j in range(0,9):
                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    game_map = get_map(printscreen)
                    actions.append([i,j,count_zeros(game_map)])
                
                    KEYBOARD.press(pynput.keyboard.Key.right)
                    KEYBOARD.release(pynput.keyboard.Key.right)

                    time.sleep(0.005) 

                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    
                    game_map = get_map(printscreen)    

                
                for i in range(0,9):

                    KEYBOARD.press(pynput.keyboard.Key.left)
                    KEYBOARD.release(pynput.keyboard.Key.left)
                    time.sleep(0.005)


            KEYBOARD.press(pynput.keyboard.Key.up)
            KEYBOARD.release(pynput.keyboard.Key.up)
            time.sleep(0.005)                

            KEYBOARD.press(pynput.keyboard.Key.left)
            KEYBOARD.release(pynput.keyboard.Key.left)
            time.sleep(0.005)                

            KEYBOARD.press(pynput.keyboard.Key.left)
            KEYBOARD.release(pynput.keyboard.Key.left)
            time.sleep(0.005)     

    elif shape == 1:

        printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
        printscreen = process_img(printscreen)
        game_map = get_map(printscreen)

        for j in range(0,8):
            printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
            printscreen = process_img(printscreen)
            game_map = get_map(printscreen)
            actions.append([0,j,count_zeros(game_map)])
        
            KEYBOARD.press(pynput.keyboard.Key.right)
            KEYBOARD.release(pynput.keyboard.Key.right)

            time.sleep(0.005) 

            printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
            printscreen = process_img(printscreen)
            
            game_map = get_map(printscreen)    

        for i in range(0,8):

            KEYBOARD.press(pynput.keyboard.Key.left)
            KEYBOARD.release(pynput.keyboard.Key.left)
            time.sleep(0.005)   
      
    elif shape == 2:

        for i in range(0,4):
            printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
            printscreen = process_img(printscreen)
            game_map = get_map(printscreen)

            if i == 0 or i == 2:

                for j in range(0,7):
                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    game_map = get_map(printscreen)
                    actions.append([i,j,count_zeros(game_map)])
                
                    KEYBOARD.press(pynput.keyboard.Key.right)
                    KEYBOARD.release(pynput.keyboard.Key.right)

                    time.sleep(0.005) 

                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    
                    game_map = get_map(printscreen)    
                    


                
                for i in range(0,7):

                    KEYBOARD.press(pynput.keyboard.Key.left)
                    KEYBOARD.release(pynput.keyboard.Key.left)
                    time.sleep(0.005)            

            if i == 1 or i == 3:

                for j in range(0,8):
                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    game_map = get_map(printscreen)
                    actions.append([i,j,count_zeros(game_map)])
                
                    KEYBOARD.press(pynput.keyboard.Key.right)
                    KEYBOARD.release(pynput.keyboard.Key.right)

                    time.sleep(0.005) 

                    printscreen =  np.array(ImageGrab.grab(bbox=(150,275,455,870)))
                    printscreen = process_img(printscreen)
                    
                    game_map = get_map(printscreen)    
                    

                
                for i in range(0,8):

                    KEYBOARD.press(pynput.keyboard.Key.left)
                    KEYBOARD.release(pynput.keyboard.Key.left)
                    time.sleep(0.005)            


            KEYBOARD.press(pynput.keyboard.Key.left)
            KEYBOARD.release(pynput.keyboard.Key.left)
            time.sleep(0.005)                

            KEYBOARD.press(pynput.keyboard.Key.left)
            KEYBOARD.release(pynput.keyboard.Key.left)
            time.sleep(0.005)                

            KEYBOARD.press(pynput.keyboard.Key.up)
            KEYBOARD.release(pynput.keyboard.Key.up)
            time.sleep(0.005)

    action = determine_action(actions)
    for i in range(0,action[0]):
        KEYBOARD.press(pynput.keyboard.Key.up)
        KEYBOARD.release(pynput.keyboard.Key.up)
        time.sleep(0.005)
    KEYBOARD.press(pynput.keyboard.Key.left)
    KEYBOARD.release(pynput.keyboard.Key.left)
    time.sleep(0.005)                

    KEYBOARD.press(pynput.keyboard.Key.left)
    KEYBOARD.release(pynput.keyboard.Key.left)
    time.sleep(0.005)

    KEYBOARD.press(pynput.keyboard.Key.left)
    KEYBOARD.release(pynput.keyboard.Key.left)
    time.sleep(0.005)  

    for i in range(0,action[1]):
        KEYBOARD.press(pynput.keyboard.Key.right)
        KEYBOARD.release(pynput.keyboard.Key.right)
        time.sleep(0.005)    

    KEYBOARD.press(pynput.keyboard.Key.space)
    KEYBOARD.release(pynput.keyboard.Key.space)
    time.sleep(0.005)   
    print(action,"\n",action[2][1],"\n\n\n\n") 


"""   
    cv2.imshow('window',printscreen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
"""