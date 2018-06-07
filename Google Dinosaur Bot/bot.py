from PIL import ImageGrab, ImageOps
import pyautogui
import numpy
import time

class Coordinates():
	replayBtn = (340,390) #based on half the screen in 1366x768 resolution
	dinosaur = (190,408) #based on half the screen in 1366x768 resolution

	
def restartGame():
	pyautogui.click(Coordinates.replayBtn)
	pyautogui.keyDown('down')
    

def pressSpace():
	pyautogui.keyUp('down')
	pyautogui.keyDown('space')
	print('Jump')
	time.sleep(0.01)
	pyautogui.keyUp('space')
	pyautogui.keyDown('down')


def imageGrab():
	box = (Coordinates.dinosaur[0]+60,
			Coordinates.dinosaur[1],
			Coordinates.dinosaur[0]+100,
			Coordinates.dinosaur[1]+5)
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = numpy.array(grayImage.getcolors())
	print(a.sum())
	return a.sum()
    

def main():
	restartGame()
	while True:
		if(imageGrab()!=446): # this value may change based on the screen resolution
			pressSpace()
			time.sleep(0.01)
            
main()
