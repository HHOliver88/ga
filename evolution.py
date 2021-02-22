import random
import string

POPULATION_SIZE = 10000
DESIRED_ORGANISM = 'Eerie nights so cold \n Tranquility in sad hearts \n It lays forgotten'
MUTATION_RATE = 0.1

class Organism:
	def __init__(self):

		self.genetic_code = ""

		self.number_of_conflicts = 0

		self.fitness = -1

		self.is_fitness_changed = True

	def get_number_of_conflicts(self):

		return self.number_of_conflicts

	def get_fitness(self):

		if self.is_fitness_changed == True:

			self.fitness = self.calculate_fitness()

			self.is_fitness_changed = False

		return self.fitness

	def calculate_fitness(self):

		self.number_of_conflicts = 0

		genetic_code = self.get_genetic_code()

		for i in range(0, len(genetic_code)):
			# we compare the genetic code of the random species with the desired species
			# desired being the "smartest"
			if genetic_code[i] != DESIRED_ORGANISM[i]:

				self.number_of_conflicts += 1

		power = self.number_of_conflicts

		if self.number_of_conflicts == 0:

			return 1
		if self.number_of_conflicts <= 4:

			return 1 / pow(((1.0*self.number_of_conflicts + 1)), 4)

		else:

			return 1 / pow(((1.0*self.number_of_conflicts + 1)), 4)

	def initialize(self):

		self.genetic_code = random.choices(string.printable, k=len(DESIRED_ORGANISM))

		return self

	def get_genetic_code(self):

		self.is_fitness_changed = True

		return self.genetic_code

	def update_genetic_code(self, genetic_code):

		self.genetic_code = genetic_code


class Population:

	def __init__(self, size):

		self.size = size

		self.organisms = []
		# this will loop 10,000 times
		for i in range(0, self.size):
			# creating 10,000 new organisms
			self.organisms.append(Organism().initialize())

	def get_organisms(self):

		return self.organisms

	def set_organisms(self, organisms):

		self.organisms = organisms

	def append_organism(self, organism):

		self.organisms.append(organism)

	def replace_organism(self, key, organism):

		self.organisms[key] = organism

	def get_size(self):

		return self.size


class Evolution:

	def __init__(self, population):

		self.population = population

	def list_to_string(self, s):  
	    
	    str1 = "" 
	    
	    return (str1.join(s))

	def evolve(self):
		generation = 0

		while(self.get_population().get_organisms()[0].get_fitness() != 1.0):

			selected_population = self.selection(self.population)

			selected_crossedover_population = self.crossover(selected_population)

			selected_crossedover_mutated_population = self.mutation(selected_crossedover_population)

			selected_crossedover_mutated_population.get_organisms().sort(key=lambda x: x.get_fitness(), reverse=True)

			self.update_population(selected_crossedover_mutated_population)

			genetic_code = population.get_organisms()[0].get_genetic_code()

			print('Generation #'+ str(generation) + ': ' + self.list_to_string(genetic_code), end='\r', flush=True)

			generation += 1

		fittest_genetic_code = population.get_organisms()[0].get_genetic_code()

		print('Generation #'+ str(generation) + ': ' + self.list_to_string(fittest_genetic_code), end='\r', flush=True)

		print('')

	def update_population(self, population):

		self.population = population

	def get_population(self):

		return self.population

	def selection(self, population):

		total = 0

		index = 0

		organisms = []
		# this code will reduce the population
		# and kill off the unfit species
		for i in range(0, len(population.get_organisms())):

			total += population.get_organisms()[i].get_fitness()

		r = random.uniform(0, total)

		while r > 0:

			r = r - population.get_organisms()[index].get_fitness()

			organisms.append(population.get_organisms()[index])

			index += 1

		population.set_organisms(organisms)

		return population

	def mutation(self, population):

		for i in range(self.len_of_population_before_crossover, POPULATION_SIZE):
			# there's a 10% chance that our organism will mutate
			self.mutate_organism(population.get_organisms()[i])

		return population

	def mutate_organism(self, organism):

		new_organism = Organism().initialize()

		for i in range(0, len(new_organism.get_genetic_code())):

			if(MUTATION_RATE > random.random()):
				# it will randomly select a letter from the organism
				# and change it with a random letter or character
				organism.get_genetic_code()[i] = new_organism.get_genetic_code()[i]

		return organism

	def crossover(self, population):

		organisms = population.get_organisms()

		self.len_of_population_before_crossover = len(organisms)

		for _ in range(POPULATION_SIZE - len(organisms)):
			# this is where we pass our genetic code
			# from parent, to offspring.
			parents = random.choices(organisms, k=2)

			parent1 = parents[0]

			parent2 = parents[1]

			child = Organism().initialize()

			split = random.randint(0, len(parent1.get_genetic_code()))

			child.update_genetic_code(parent1.get_genetic_code()[0:split] + parent2.get_genetic_code()[split:len(parent1.get_genetic_code())])

			population.append_organism(child)

		return population

population = Population(POPULATION_SIZE)
evolution = Evolution(population)
evolution.evolve()


