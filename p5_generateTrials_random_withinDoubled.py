#4
"""
Randomize the trial list *within* blocks
"""

import random

separator = ','
blocks = 5
trialType = ['masked']*2 + ['nonmasked']*1
locations = ['right', 'left']
repeats=2


def generateTrialList(blocks,trialType,locations,repeats):
	trialList=[]
	for curBlock in range(blocks):
		trialList.append([])
		for curRepeat in range(repeats):
			for curTrialType in trialType:
				for curLocation in locations:
					trialList[curBlock].append(separator.join((str(curBlock+1), curTrialType, curLocation)))

	for curBlock in trialList:
		random.shuffle(curBlock)
		for curTrialList in curBlock:
			print curTrialList

generateTrialList(blocks,trialType,locations,repeats)