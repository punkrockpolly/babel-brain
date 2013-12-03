import random

def mutatePopulation(pPopulation, pMutationProb, pValidChars):
	#mutates a population at pMutationProb
	for geneIndex in range(len(pPopulation)):
		if random.random() < pMutationProb: 
			pPopulation[geneIndex] = mutateGene(pPopulation[geneIndex], pValidChars)
	return pPopulation

def mutateGene(pGene, pValidChars):
	# this function just swaps a single char in the pGene with a validChar
	pGene = list(pGene)
	pValidChars = list(pValidChars)

	pGene[random.randint(0,len(pGene)-1)] = pValidChars[random.randint(0,len(pValidChars)-1)]
	pGene = ("".join(pGene))
	return pGene

#pop = ["XXXXX","XXXXX","XXXXX","XXXXX","XXXXX","XXXXX"]
#listPrint(mutatePopulation(pop,0.05,"1234567890"))



