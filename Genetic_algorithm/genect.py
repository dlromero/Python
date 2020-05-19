import random

modelo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
largo = 10
num = 10
pressure = 3
mutation_chance = 0.2

print("\n\Modelo: %s\n" % (modelo))


def individual(min, max):
    return [random.randint(min, max) for i in range(largo)]


def createPopulation():
    return[individual(1, 9) for i in range(largo)]


def calcularFitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
    return fitness
