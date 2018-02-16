#standard solution
def repetition1(letters,numberBeforeSwitch, numRepetitions):
	for curRepeatSequence in range(numRepetitions):
		for curElt in letters:
			for curRepeatElement in range(numberBeforeSwitch):
				print curElt
 
 
#another solution with an intermediate list that's then duplicated as needed
def repetition2(letters,numberBeforeSwitch, numRepetitions):
	newList =[]
	for curElement in letters:
		newList.extend([curElement]*numberBeforeSwitch)
	newList *=numRepetitions
	for curElt in newList:
		print curElt
 
 
#the solution above using list comprehension (try to unpack what's going on here)
def repetition3(letters,numberBeforeSwitch, numRepetitions):
	newList= [[curElt]*numberBeforeSwitch for curElt in letters]*numRepetitions #newLists is a list of lists; need to flatten in
	for curElt in sum(newList,[]): #to flatten the list
		print curElt
 
#if we want to print the elements individually, we can join them into a string (using newline as a separator) as we create the list.
def repetition4(letters,numberBeforeSwitch, numRepetitions):
	for curElt in ['\n'.join([curLetter]*numberBeforeSwitch) for curLetter in letters]*numRepetitions:
		print curElt

