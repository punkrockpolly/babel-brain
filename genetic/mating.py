import string
import random

def nPointCrossover(pGene1,pGene2,pNumChildren,pNumCrossovers):
	# INITIALIZE OFFSPRING LIST
	offspring = []

	# GRAB STR LENGTHS AND DETERMINE GENELENGTH ACCORDINGLY
	len1 = len(pGene1)
	len2 = len(pGene2)
	geneLength = min(len1,len2)
	
	# ASSIGN A VALUE TO THE REMNANT, THE REMAINING CHARS OF THE LONGER GENE
	if len1 == len2: remnant = ""
	elif len1 >	 len2: remnant = pGene1[len2:len1]
	else: remnant = pGene2[len1:len2]

	# DECIDE how to handle remnant: ignore, trim to average of lens, trim to random size
	remnant = remnant

	# DETECT CASE WHERE pNumCrossovers is specified higher than valid
	if pNumCrossovers > geneLength: 
		print "ERROR: NUMBER OF CROSSOVERS MAY NOT EXCEED GENE LENGTH"

	# WE BEGIN GENERATING OFFSRPING TILL WE HAVE ENOUGH!
	loopCount = 0
	while (len(offspring) < pNumChildren) and loopCount < 1000:
		loopCount+=1 #safeguard in case something goes wrong and loops infinitely

		# range(1,geneLength) generates a list of valid crossover points for 
		# the gene (avoiding end charectars 0 and geneLength, which would result in
		# clone on parents. the random.sample returns (pNumCrossover) number of unique
		# and random crossover points from the valid list, in the form of a list.
		randomCrossoverPoints  = random.sample(range(1,geneLength), pNumCrossovers)
		# print randomCrossoverPoints # GREAT FOR DEBUGGING

		# because of the destructive nature of the following of how we build multiple
		#crossove genes we clone the parents and make the children out of the clones.
		parentClone1 = pGene1
		parentClone2 = pGene2
		
		# now we loop for each crossover, applying it to the clones. the end of this
		# process is that the clones now are the children, because they have had the
		#crossovers applied to them iteratively
		for thisCrossover in randomCrossoverPoints:
			tempGene1 = parentClone1 #because of the destructive nature of following operations. 
			# compute offsrping
			parentClone1 = parentClone1[0:thisCrossover] + parentClone2[thisCrossover:geneLength]
			parentClone2 = parentClone2[0:thisCrossover] + tempGene1[thisCrossover:geneLength]

		# ADD OFFSRPING TO LIST
		offspring.append(parentClone1)
		offspring.append(parentClone2)

	# FUTURE DEV. IF YOU WANT TO REMOVE DUPES FROM OFFSPRING (THINK THRU IMPLICATIONS)
	# A SET IN PYTHON HAS NO DUPLICATES. SO WE CONVERT OUT LIST TO A SET AND THEN
	# BACK TO A LIST TO PURGE DUPES. NOTE THAT THE ORDER OF THE LIST IS DESTROYED :(
	# offspring = list(set(offspring)). Also note that we would have to add more
	# offsrping to get to the right number of pNumChildren

	# because genes are added 2 at a time sometimes the offspring list will have
	# more genes than we want. so we return the first pNumChildren items. 
	return offspring[0:pNumChildren]

def twoPointCrossover(pGene1,pGene2,pNumChildren):
	return nPointCrossover(pGene1,pGene2, pNumChildren, 1)

def onePointCrossover(pGene1,pGene2,pNumChildren):
	return nPointCrossover(pGene1,pGene2, pNumChildren, 2)

def cutAndSplice(pGene1,pGene2, pNumChildren):
	# INITIALIZE OFFSPRING LIST
	offspring = []

	# GRAB STR LENGTHS AND DETERMINE GENELENGTH ACCORDINGLY
	len1 = len(pGene1)
	len2 = len(pGene2)
	
	# WE BEGIN GENERATING OFFSRPING TILL WE HAVE ENOUGH!
	loopCount = 0
	while (len(offspring) < pNumChildren) and loopCount < 1000:
		loopCount+=1 #safeguard in case something goes wrong and loops infinitely
		
		# RANDOM CHOOSE CROSSOVERS
		crossover1 = random.randint(1,len1-1)
		crossover2 = random.randint(1,len2-1)
		#print str(crossover1) + " " + str(crossover2)
		#CREATE KIDS
		child1 = pGene1[0:crossover1] + pGene2[crossover2:len2]
		child2 = pGene2[0:crossover2] + pGene1[crossover1:len1]

		# ADD OFFSRPING TO LIST
		offspring.append(child1)
		offspring.append(child2)

	# because genes are added 2 at a time sometimes the offspring list will have
	# more genes than we want. so we return the first pNumChildren items. 
	return offspring[0:pNumChildren]

def uniformCrossover(pGene1,pGene2, pNumChildren):
	# since strings are immutable in python and we want to later assign specific chars
	# we convert the strings to lists first.
	pGene1 = list(pGene1)
	pGene2 = list(pGene2)
	
	offspring = []
	
	# WE BEGIN GENERATING OFFSRPING TILL WE HAVE ENOUGH!
	loopCount = 0
	while (len(offspring) < pNumChildren) and loopCount < 1000:
		loopCount+=1 #safeguard in case something goes wrong and loops infinitely

		for charNum in range(len(pGene1)):
			if (not (pGene1[charNum] == pGene2[charNum])) and (round(random.uniform(0,1)) == 1):
				# SWAP CHARS
				tempChar = pGene1[charNum]
				pGene1[charNum] = pGene2[charNum]
				pGene2[charNum] = tempChar

		offspring.append("".join(pGene1))
		offspring.append("".join(pGene2))

	return offspring[0:pNumChildren]


def halfUniformCrossover():
	#future dev
	return

def listPrint(pList):
	for item in pList:
		print item

#TESTING
#listPrint(cutAndSplice([1,1,1,1,1,1], [0,0,0,0,0,0],12))
#listPrint(nPointCrossover("XXXXXXXXXXXXXXXXXXXX", "OOOOOOOOOOOOOOOOOOOO", 6, 4))
#listPrint(uniformCrossover("111133331111", "111144441111", 12))