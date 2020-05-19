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
    return[individual(1, 9) for i in range(num)]


def calcularFitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
    return fitness


def selection_and_reproduction(population):
    puntuados = [(calcularFitness(i), i) for i in population]
    puntuados = [i[1] for i in sorted(puntuados)]
    population = puntuados

    selected = puntuados[(len(puntuados)-pressure):]

    for i in range(len(population)-pressure):
        punto = random.randint(1, largo-1)
        padre = random.sample(selected, 2)
        
        population[i][:punto] = padre[0][:punto]
        population[i][punto:] = padre[1][punto:]

    return population


def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:
            punto = random.randint(0, largo-1)
            nuevo_valor = random.randint(1, 9)

            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1, 9)

            population[i][punto] = nuevo_valor
    return population


population = createPopulation()
print("Población Inicial: \n%s"%(population))

for i in range(100):
    population = selection_and_reproduction(population)
    population = mutation(population)

print("\nPoblación Final: \n%s"%(population))
print("\n\n")
