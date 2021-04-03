import random


class Individual:
    'defines an individual in a population'
    size = None
    map = None

    def __init__(self, string=None):
        if string is None:
            self.string = self.setRandomString()
        else:
            self.string = string
        self.fit = self.computeFitness()

    def __repr__(self):
        rep = 'string = ' + self.string + ' fitness = ' + str(self.fit)
        return rep

    def computeFitness(self):
        'returns the disdance of a path which is the fitness of an individual O(n)'
        d = 0
        for i in range(Individual.size):
            start = int(self.string[i])
            end = int(self.string[i+1])
            distance = Individual.map[start][end]
            if distance == float("inf"):
                d = float("inf")
                break
            d += distance
        return d

    @staticmethod
    def setRandomString():
        'returns a random path in form of a string O(n)'
        lst = []
        string = ""
        for i in range(Individual.size):
            while 1:
                rand = random.randrange(0, Individual.size)
                if rand not in lst:
                    string = string + str(rand)
                    lst.append(rand)
                    break
        string = string + string[0]
        return string

    @staticmethod
    def partiallyMappedCrossover(individual1, individual2):
        'returns child of individual1 and individual2, using partially mapped crossover O(n)'
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
        'performs mutation on an individual with a small probability O(1)'
        rand = random.uniform(0, 1)
        if rand <= prob:
            ij = random.sample(range(0, Individual.size), 2)
            i = ij[0]
            j = ij[1]
            self.string = swapElements(i, j, self.string)
            if i == 0 or j == 0:
                self.string = self.string[0: Individual.size] + self.string[0]


class Population:
    'population class. has a list of individuals'
    size = None

    def __init__(self, isEmpty):
        self.individuals = []
        if isEmpty is False:
            for i in range(Population.size):
                self.individuals.append(Individual())

    def __repr__(self):
        rep = ''
        for ind in self.individuals:
            rep = rep + "\n" + repr(ind)
        return rep

    def pickWithWeights(self):
        'returns a random individual based on individuals weights (1/fitness) O(populationsize)'
        lst = []
        weights = []
        for ind in self.individuals:
            lst.append(ind)
            weights.append(1 / ind.fit)
        rands = random.choices(population=lst, weights=weights, k=2)
        return rands[0], rands[1]

    def addIndividual(self, individual):
        self.individuals.append(individual)

    def bestIndividual(self):
        'returns an individual with the lowest fitness'
        best = float("inf")
        for individual in self.individuals:
            if individual.fit <= best:
                bestInd = individual
                best = individual.fit
        return bestInd

    def overall(self):
        'returns the average fitness of a population'
        sum = 0
        for ind in self.individuals:
            if ind.fit == float("inf"):
                return float("inf")
            sum += ind.fit
        return sum / len(self.individuals)



def swapElements(i, j, string):
    'swaps ith and jth position of a string and returns the new string'
    strlist = list(string)
    strlist[i], strlist[j] = strlist[j], strlist[i]
    stringnew = "".join(strlist)
    return stringnew


def print2dlst(lst):
    for xs in lst:
        print(" ".join(str(xs)))


def geneticAlgorithm(mapp, initialPopulation=None, iterations=100, populationSize=4, muteProb=0.05):
    'performs genetic algorithm'
    i = 0
    individualSize = len(mapp)
    Population.size = populationSize
    Individual.size = individualSize
    Individual.map = mapp
    print("genetic algorithm is executed")
    print("population size = ", populationSize)
    print("individual length/ number of cities = ", individualSize)
    print2dlst(mapp)
    print("--------------------------")
    if initialPopulation is None:
        initialPopulation = Population(False)
    currentPopulation = initialPopulation
    while i < iterations:
        print("genetic algorithm ", str(i+1) + "th iteration" )
        print("current population : ")
        print(repr(currentPopulation))
        print("--------------------------")
        newPopulation = Population(True)
        for k in range(populationSize):
            x, y = currentPopulation.pickWithWeights()
            print("x,y picked for " + str(k+1) + "th reproduction:")
            print(repr(x) +"    " +repr(y))
            child = Individual.partiallyMappedCrossover(x, y)
            print("child after partially mapped crossover:")
            print(repr(child))
            child.muteWithSmallProb(muteProb)
            print("child after mutation with probability of " + str(muteProb))
            print(repr(child))
            newPopulation.addIndividual(child)
        print("next population generated")
        print("--------------------------")
        # if currentPopulation.overall() <= newPopulation.overall():
        #     break
        currentPopulation = newPopulation
        i += 1
    print("the best individual in the final population = ")
    print(repr(currentPopulation.bestIndividual()))
    return(currentPopulation.bestIndividual())


map = [ [ 0, 2, float("inf"), 12, 5 ],
        [ 2, 0, 4, 8, float("inf") ],
        [ float("inf"), 4, 0, 3, 3 ],
        [ 12, 8, 3, 0, 10 ],
        [ 5, float("inf"), 3, 10, 0 ] ]
geneticAlgorithm(mapp=map)