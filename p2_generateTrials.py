
#2
"""
Suppose we are interested in finding out the efficacy of a particular kind of masking technique and want to examine if it's more effective in the left vs. right visual field. Let's code a basic trial list for an experiment in which we display an image on either the left or the right side of the screen. Both sides of the screen are then masked, and we are interested in measuring people's ability (e.g., accuracy, reaction time) in responding whether the image was on the right or left side of the screen, while comparing responses on masked vs. nonmasked trials.

To do this, we need to generate a list of trials in which some proportion is masked and some is not masked. Within each condition, we want the image on the left side displayed with some proportion of the time, and on the right the remaining times.

Let's begin by having 2/3 masked trials and 1/3 non-masked trials. Within each level of the masking factor, half of the targets should be on the left and half on the right. Let's have 5 blocks with each block having all the possible trial types.
"""

separator = ','
blocks = 5
trialType = ['masked']*2 + ['nonmasked']*1
locations = ['right', 'left']

def generateTrialList(blocks,trialType,locations):
	trialList=[]
	for curBlock in range(blocks):
		for curTrialType in trialType:
			for curLocation in locations:
				trialList.append(separator.join((str(curBlock+1), curTrialType, curLocation)))
	for curTrial in trialList:
		print curTrial

generateTrialList(blocks,trialType,locations)