class Individual:
    def __init__(self, size, string=None):
        if string is None:
            self.createRandomIndividual()
        else:
            self.string = string
        self.size = size
    def computeFitness(self, map):

    def createRandomIndividual(self):


    def reproduce(individual1, individual2):
        return
    def muteWithSmallProb(self):


class Population:
    def __init__(self, individualSize, populationSize, isEmpty):
        self.individualSize = individualSize
        self.populationSize = populationSize
        self.individuals = []
        if isEmpty is False:
            for i in range(populationSize):
                self.individuals.append(Individual(individualSize))
    def pickRand(self):
    def addIndividual(self, individual):
        self.individuals.append()
    def bestIndividual(self):
        best = float("inf")
        for individual in self.individuals:
            if individual.fit <= best:
                bestInd = individual
                best = individual.isFit
        return bestInd
    def isFit(self, fitEnough):
        for individual in self.individuals:
            if individual.fit <= fitEnough:
                return True
        return False
    'map ro yejuri vared konam ke betune fitness hesab kone'


def geneticAlgorithm(map, initialPopulation = None, iterations = 100, fitEnough = None, populationSize = 4):
    i = 0
    individualSize = len(map)
    if initialPopulation is None:
        initialPopulation = Population(individualSize, populationSize, False)
    currenPopulation = initialPopulation
    while i < iterations and initialPopulation.isFit(fitEnough) is False:
        newPopulation = Population(individualSize, populationSize, True)
        for i in range(populationSize):
            x = currenPopulation.pickRand()
            y = currenPopulation.pickRand()
            child = Individual.reproduce(x, y)
            child.muteWithSmallProb()
            newPopulation.addIndividual(child)
        currenPopulation = newPopulation
    return(currenPopulation.bestIndividual())






