from GA import GA

def readGraph(file):
    f = open(file, "r")
    n = int(f.readline())
    graph = []
    for i in range(0, n):
        str = f.readline()
        values = str.split(",")
        edges = []
        for j in range(0, n):
            edges.append(int(values[j]))
        graph.append(edges)
    return graph

def readFromFile(fileName):
    f = open(fileName, "r")
    graph = []
    noNodes = int(f.readline())
    for line in f:
        costs = line.split(",")
        chromosome = []
        for cost in costs:
            chromosome.append(int(cost))
        graph.append(chromosome)
    problParam = {'noNodes':noNodes, 'graph':graph, 'function':fitness}
    return problParam


def fitness(chromosome):
    val = 0
    rep = chromosome.repres
    network = chromosome.problParam['graph']
    for i in range(0, len(rep) - 1):
        node = rep[i]
        nextNode = rep[i + 1]
        val = val + network[node - 1][nextNode - 1]
    val = val + network[rep[len(rep) - 1] - 1][rep[0] - 1]
    return val

def main():
    #graph = readGraph("inputFiles/easy_01_4.txt")
    #print(graph)
    #gaParam = {'popSize': 100, 'noGen': 100, 'pc': 0.8, 'pm': 0.1}
    #problParam = {'noNodes': len(graph),'graph':graph, 'function': fitness_func}

    data = readFromFile("inputFiles/hard_02_52.txt")
    gaParam = {'popSize':100, 'noGen':5000}

    ga = GA(gaParam, data)
    ga.initialisation()
    ga.evaluation()

    bestChromosomes = []
    bestFitness = 99999999
    bestChromosomeRepres = None

    for g in range(gaParam['noGen']):
        ga.oneGenerationElitism()
        bestChromo = ga.bestChromosome()
        if(bestChromo.fitness<bestFitness):
            bestChromosomeRepres = bestChromo.repres
            bestFitness = bestChromo.fitness
        bestChromosomes.append(bestChromo)
        print('Generation ' + str(g) + '/\n best chromosome: ' + str(bestChromo.repres) + '/\n  -> fitness: ' + str(bestChromo.fitness))

    print('\n ---------\nBest overall solution: ' + str(bestChromosomeRepres) + ' \n fitness = ' + str(bestFitness))



main()