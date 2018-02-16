
#2 - variant
"""
Here is a more flexible solution
"""

#a bit more flexible, with type-checking to ensure that arguments are integers
def genTrialList2(numBlocks,numRepsPerBlock, maskToNonMaskRatio,separator=','):
	assert(
		isinstance(numBlocks,int) and 
		isinstance(numRepsPerBlock,int) and 
		isinstance(maskToNonMaskRatio,int))
	maskConditions = ['masked']*maskToNonMaskRatio + ['nonmasked'] #2-to-1 ratio = 66.67% / 33.33%
	targetSides = ['left','right']
	for curBlock in range(numBlocks):
		for curRep in range(numRepsPerBlock):
			for curTargetSide in targetSides:
				for curMaskCondition in maskConditions:
					print str(curBlock+1)+','+curTargetSide+','+curMaskCondition
 

genTrialList2(numBlocks=5,numRepsPerBlock=1,maskToNonMaskRatio=2)