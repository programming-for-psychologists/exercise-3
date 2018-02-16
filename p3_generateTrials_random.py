#3
"""
Randomize the trial list
"""


import random

def generateTrialListRandom():
	blocks = 5
	trialType = ['masked','masked','nonmasked']
	locations = ['right', 'left']
	trialList=[]
	separator = ','
	for curBlock in range(blocks):
		for curTrialType in trialType:
			for curLocation in locations:
				trialList.append(separator.join((str(curBlock+1), curTrialType, curLocation)))
	random.shuffle(trialList)
	for curTrial in trialList:
		print curTrial

generateTrialListRandom()
