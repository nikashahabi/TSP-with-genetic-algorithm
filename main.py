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
        for i in range(self.size):
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
    def reproduce(individual1, individual2):
        rand = random.randrange(0, )
    def muteWithSmallProb(self, prob):
        rand = random.uniform(0,1)
        if rand <= prob:
            i = random.randrange(0, )
    'in do ta tabe akhari mundan'



class Population:
    size = None
    def __init__(self, isEmpty):
        self.individuals = []
        if isEmpty is False:
            for i in range(Population.populationSize):
                self.individuals.append(Individual())
    def pickRand(self):
        rand = random.randrange(0, self.populationSize)
        return self.individuals[rand]
    def addIndividual(self, individual):
        self.individuals.append(individual)
    def bestIndividual(self):
        best = float("inf")
        for individual in self.individuals:
            if individual.fit <= best:
                bestInd = individual
                best = individual.Fit
        return bestInd
    def isFit(self, fitEnough):
        for individual in self.individuals:
            if individual.fit <= fitEnough:
                return True
        return False



def geneticAlgorithm(map, initialPopulation = None, iterations = 100, fitEnough = None, populationSize = 4, muteProb= 0.1):
    i = 0
    individualSize = len(map)
    Population.size = populationSize
    Individual.size = individualSize
    Individual.map = map
    if initialPopulation is None:
        initialPopulation = Population(False)
    currentPopulation = initialPopulation
    while i < iterations and initialPopulation.isFit(fitEnough) is False:
        newPopulation = Population(True)
        for i in range(populationSize):
            x = currentPopulation.pickRand()
            y = currentPopulation.pickRand()
            child = Individual.reproduce(x, y)
            child.muteWithSmallProb(muteProb)
            newPopulation.addIndividual(child)
        currentPopulation = newPopulation
    return(currentPopulation.bestIndividual())








