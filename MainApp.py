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


def func(chromosome):
    repres = chromosome.repres
    g = chromosome.problParam['graph']
    fitness = 0.0

    for i in range(len(repres) - 1):
        fitness = fitness + g[repres[i]][repres[i+1]]

    return fitness

def main():
    graph = readGraph("input.txt")
    print(graph)
    gaParam = {'popSize': 100, 'noGen': 500, 'pc': 0.8, 'pm': 0.1}
    problParam = {'noNodes': len(graph),'graph':graph, 'function': func}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestChromosomes = []

    for g in range(gaParam['noGen']):
        ga.oneGenerationElitism()

        bestChromo = ga.bestChromosome()
        bestChromosomes.append(bestChromo)
        print('Generation ' + str(g) + '/ best chromosome: ' + str(bestChromo.repres) + '/ fitness: ' + str(bestChromo.fitness))



main()