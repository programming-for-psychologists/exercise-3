
import time
import sys
import random
import numpy as np 
from psychopy import visual,event,core,filters

def makeFilteredNoise(res, radius, shape='gauss'):
    """Dynamically creates gaussian noise https://discourse.psychopy.org/t/creating-bandpass-gaussian-white-noise/2125""" 
    noise = np.random.random([res, res])
    kernel = filters.makeMask(res, shape=shape, radius=radius)
    filteredNoise = filters.conv2d(kernel, noise)
    filteredNoise = (filteredNoise-filteredNoise.min())/(filteredNoise.max()-filteredNoise.min())*2-1
    return filteredNoise
    
win = visual.Window([400,400], monitor='testMonitor',color=[.5,.5,.5])

targetColor = [.4,.4,.4]
displayDuration = .06

shapeLeft = visual.Rect(win,lineColor=targetColor, fillColor=targetColor,size=[100,100],pos=[-100,0],units="pix")
shapeRight = visual.Rect(win,lineColor=targetColor, fillColor=targetColor,size=[100,100],pos=[100,0],units="pix")
fixation = visual.TextStim(win,color="black",height=40,text='+',units="pix")
prompt = visual.TextStim(win,color="black",height=40,text='?',units="pix")

separator=','
trials = open('trials.txt', 'r').readlines()
for curTrial in trials:
	fixation.draw()
	win.flip()
	core.wait(.7)
	(block, masking, side) = curTrial.rstrip().split(separator)
	fixation.draw()
	if side=='left':
		shapeLeft.draw()
	elif side=='right':
		shapeRight.draw()
	win.flip()
	core.wait(displayDuration)
	if masking=="masked":
		visual.ImageStim(win, mask=None,pos=[-.5,0],image=makeFilteredNoise(50, .01)).draw()
		visual.ImageStim(win, mask=None,pos=[.5,0],image=makeFilteredNoise(50, .01)).draw()
	win.flip()
	core.wait(.1)

	prompt.draw()
	win.flip()
	event.waitKeys(keyList=['left','right'])
