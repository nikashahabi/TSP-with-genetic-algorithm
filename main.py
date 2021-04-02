import random

class Individual:
    size = None
    map = None
    def __init__(self, string=None):
        if string is None:
            self.string = self.setRandomString()
        else:
            self.string = string
        self.fit = self.computeFitness()
    def computeFitness(self):
        d = 0
        for i in range(Individual.size):
            start = int(self.string[i])
            end = int(self.string[i+1])
            distance = Individual.map[start][end]
            if  distance == float("inf"):
                d = float("inf")
                break
            d += distance
        return d

    def setRandomString(self):
        list = []
        string = ""
        for i in range(Individual.size):
            while 1:
                rand = random.randrange(0, Individual.size)
                if rand not in list:
                    string = string + str(rand)
                    list.append(rand)
                    break
        string = string + string[0]
        return string
    @staticmethod
    def partiallyMappedCrossover(individual1, individual2):
        i = random.randrange(0, Individual.size+1)
        j = random.randrange(0,Individual.size+1)
        while j == i:
            j = random.randrange(0, Individual.size+1)
        if j < i:
            i, j = j, i
        child1 = individual1.string[i:j]
        child2 = individual2.string[i:j]
        map1to2 = {}
        map2to1 = {}
        for k in range(i, j):
            map1to2[individual1.string[k]] = individual2.string[k]
            map2to1[individual2.string[k]] = individual1.string[k]
        'child 1 is now getting complete'
        child1half = ""
        for k in range(0, i):
            temp = individual2.string[k]
            while temp in child1:
                temp = map1to2[temp]
            child1half = child1half + temp
        child1 = child1half + child1
        for k in range(j, Individual.size):
            temp = individual2.string[k]
            while temp in child1:
                temp = map1to2[temp]
            child1 = child1 + temp
        child2half = ""
        for k in range(0, i):
            temp = individual1.string[k]
            while temp in child2:
                temp = map2to1[temp]
            child2half = child2half + temp
        child2 = child2half + child2
        for k in range(j, Individual.size):
            temp = individual1.string[k]
            while temp in child2:
                temp = map2to1[temp]
            child2 = child2 + temp
        child1 = child1 + child1[0]
        child2 = child2 + child2[0]
        finalChild = Individual(random.choice([child1, child2]))
        return finalChild

    def muteWithSmallProb(self, prob):
        rand = random.uniform(0,1)
        if rand <= prob:
            ij = random.sample(range(0, Individual.size), 2)
            i = ij[0]
            j = ij[1]
            self.string = swapElements(i, j, self.string)
            if i == 0 or j == 0:
                 self.string = self.string[0: Individual.size] + self.string[0]


class Population:
    size = None

    def __init__(self, isEmpty):
        self.individuals = []
        if isEmpty is False:
            for i in range(Population.size):
                self.individuals.append(Individual())

    def pickWithWeights(self):
        lst = []
        weights = []
        for ind in self.individuals:
            lst.append(ind)
            weights.append(ind.fit)
        rands = random.choices(lst, weights, 2)
        return rands[0], rands[1]

    def addIndividual(self, individual):
        self.individuals.append(individual)

    def bestIndividual(self):
        best = float("inf")
        for individual in self.individuals:
            if individual.fit <= best:
                bestInd = individual
                best = individual.fit
        return bestInd

    def isFit(self, fitEnough):
        for individual in self.individuals:
            if individual.fit <= fitEnough:
                return True
        return False

def swapElements(i, j, string):
    strlist = list(string)
    strlist[i], strlist[j] = strlist[j], strlist[i]
    stringnew = "".join(strlist)
    return stringnew


def geneticAlgorithm(map, initialPopulation = None, iterations = 100, fitEnough = 20, populationSize = 4, muteProb= 0.1):
    i = 0
    individualSize = len(map)
    Population.size = populationSize
    Individual.size = individualSize
    Individual.map = map
    if initialPopulation is None:
        initialPopulation = Population(False)
    currentPopulation = initialPopulation
    while i < iterations and initialPopulation.isFit(fitEnough) is False:
        print("generic algorithm ", str(i) + "th iteration" )
        newPopulation = Population(True)
        for i in range(populationSize):
            x, y = currentPopulation.pickWithWeights()
            child = Individual.partiallyMappedCrossover(x, y)
            child.muteWithSmallProb(muteProb)
            newPopulation.addIndividual(child)
        currentPopulation = newPopulation
    return(currentPopulation.bestIndividual())


map = [[0, 2, 3],
       [2,0, 0],
       [100,1,0]]
geneticAlgorithm(map=map)