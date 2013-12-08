import string
import random


def theSolution():
    # Define solution
    return "HACKER SCHOOL IS AWESOME"


def levD(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


def randomString(pLength):
    # RETURN UPPERCASE, lowercase, Numb3rs.
    # Uses this awesome compact method:
#http://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
    return ''.join(random.choice(string.ascii_uppercase +
                                 string.ascii_lowercase +
                                 string.digits + " ") for x in range(pLength))
    # if pLength == 'None': pLength = random.randint(3,30)
    # return ''.join(random.choice(string.ascii_uppercase + " ") for x in range(pLength))


def solutionFound():
    print("SOLUTION FOUND")
    quit()


def theFitnessOf(pGene):
    # Returns fitness of a particular gene.
    # the max fitness should be a percentage closeness
    # based on the max length of string.
    sol = theSolution()
    if pGene == sol: solutionFound()
    maxFitness = len(sol)
    return levD(pGene, sol)
    # return 100 * ((maxFitness - levD(pGene,sol)) / float(maxFitness))


def mutationsOf(pGene):
    # MUTATE A SMALL PERCENTAGE
    return pGene


def theOffspringOf(pGene1, pGene2, pNumChildren):
    # NOTE ADD OTHER MATING METHODS
    # genes must be the same length for this to work correctly.
    geneLength = len(pGene1) if (len(pGene1) < len(pGene2)) else len(pGene2)
    offspring = []
    loopNum = 0
    while (len(offspring) < pNumChildren) and loopNum < 1000:
        loopNum += 1
        # BY GOING FROM 1 to geneLength - 1
        # we prevent 0 and geneLength from becoming crossover points.
        crossoverPoint = random.randint(1, geneLength - 1)

        # generate children
        child1 = pGene1[0:crossoverPoint] + pGene2[crossoverPoint:geneLength]
        child2 = pGene2[0:crossoverPoint] + pGene1[crossoverPoint:geneLength]

        # add the children to the list
        offspring.append(child1)
        offspring.append(child2)

    return offspring


def someRandomGenes(generationSize):
    return [randomString(len(theSolution())) for x in range(generationSize)]


def getxy(grid, x, y):
    return grid[y][x]


def setxy(grid, x, y, val):
    grid[y][x] = val
    return grid


# CURRENTLY UNUSED
def levDist(pString1, pString2):
# initialize costs
    tLen1 = len(pString1)
    tLen2 = len(pString2)

    tSubCost = 1
    tDelCost = 1  # tDelCost & tAddCost assigned but never used
    tAddCost = 1

    # the range should be the (len of the string + 1)
    tDist = [[0 for i in range(tLen1 + 1)] for j in range(tLen2 + 1)]

    for x in range(tLen1 + 1):
        tDist = setxy(tDist, x, 0, x)
        for y in range(tLen2 + 1):
            tDist = setxy(tDist, 0, y, y)
            # I DONT UNDERSTAND WHY THESE ARE x-1 and y-1 but it seems to work.
            if pString1[x - 1] == pString2[y - 1]:
                tCost = 0
            else:
                tCost = tSubCost
                tMinCost = min((getxy(tDist, x - 1, y) + 1),
                               (getxy(tDist, x, y - 1) + 1),
                               (getxy(tDist, x - 1, y - 1) + tCost))
                tDist = setxy(tDist, x, y, tMinCost)

    return getxy(tDist, x, y)


def mainLoop(pGenes, pGenerationNum):
    ##INIT
    numchildren = 6

    if pGenes is None:
        print("A NEW GENERATION WAS STARTED")
        ##CONSTANTS
        generationSize = 2000
        pGenerationNum = 1
        ## IF FIRST GEN THEN CREATE FIRST GENERATION
        genes = someRandomGenes(generationSize)
    else:
        if pGenerationNum is None: pGenerationNum = 1
        genes = pGenes
        generationSize = len(pGenes)

    ## INTIALIZE A DICTIONARY TO STORE GENE FITNESS AND A VAR TO STORE
    ## TOTAL GENERATION FITNESS
    geneFitness = dict()
    generationFitness = 0

    ## CALCULATE FITNESS FOR EACH GENE, STORE IN DICT AND PRINT
    for thisGene in genes:
        geneFitness[thisGene] = theFitnessOf(thisGene)
        generationFitness += geneFitness[thisGene]
        # print("     {0}                        {1}".format(
        #       thisGene, geneFitness[thisGene]))

    ## DETERMINE GENERATIONAL AVERAGE AND PRINT
    avgGenFitness = float(generationFitness) / generationSize
    print("AVG GENERATION FITNESS: {0}".format(avgGenFitness))

    ## KILL GENES THAT DID NOT PERFORM ABOVE AVERAGE
    ## PRODUCE REPORT FOR DEATHS AND REPRODUCTION
    test1 = len(geneFitness.keys())
    print("WHAT HAPPENED... GENERATION # {0} :".format(pGenerationNum))
    for thisGene in geneFitness.keys():
        if geneFitness[thisGene] >= avgGenFitness:
            print("DIED W/O REPRODUCING:    {0}                       {1}"
                  .format(thisGene, geneFitness[thisGene]))
            del geneFitness[thisGene]

    # ASSIGN SURVIVING GENES TO THE MAIN GENES LIST
    test2 = len(geneFitness.keys())
    genes = geneFitness.keys()

    ## INIT EMPTY OFFSPRING LIST
    offspring = []
    print('')

    ## PRODUCE REPORT ON
    # for thisGene in genes:
    #   print("REPRODUCED:  {0} {1}".format(thisGene, geneFitness[thisGene]))

    ## CHOOSE MATES (FIRST AND LAST ITEMS IN LIST) PRODUCE OFFSPRING AND REPORT

    while len(genes) >= 2:
        # print("==FAMILY==")
        # print("PARENT1: {0}  {1}".format(genes[0], geneFitness[genes[0]]))
        # print("PARENT2: {0}  {1}".format(genes[-1], geneFitness[genes[-1]]))
        newOffspring = theOffspringOf(genes[-1], genes[0], numchildren)
        offspring.append(newOffspring)
        # print("OFFSPRING: {0}".format(newOffspring))
        # print("=====")

        # get rid of first and last itmes
        # now that they have reporduced, they die. their children live on.
        genes.pop(0)
        genes.pop(-1)

    # FORMAT THE OFFSPRING LIST
    # flattens the weirdly nested list of offspring
# http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python

    offspring = [item for sublist in offspring for item in sublist]
    print('')
    print("NUM DIED: {0}".format(test1 - test2))
    print("GENERATION # {0} :".format(pGenerationNum))
    print("NUM KIDS: {0}".format(len(offspring)))
    print("AVG PARENTS' GENERATION FITNESS: {0}".format(avgGenFitness))

    ## SINCE THE OFFSPRING IS THE NEW GENERATION, THEY BECOME THE genes LIST:
    pGenerationNum += 1
    #genes = offspring

    keepgoing = raw_input("Continue? ")
    if not keepgoing == 'y':
        quit()
    else:
        mainLoop(offspring, pGenerationNum)


#print(theFitnessOf("HACKER SCTTTR"))
mainLoop(None, None)
