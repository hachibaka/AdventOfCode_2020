from itertools import combinations
from functools import reduce
import operator

def part1_sumoftwo(input_values, target):
	reminder = {}
	for value in input_values:
		if value in reminder:
			return value * reminder[value]
		else:
			reminder[target-value] = value


def part2_sumofthree_naive(input_values, target):
	for i in range(len(input_values)):
		for j in range(1, len(input_values)):
			for k in range(2, len(input_values)):
				if input_values[i] + input_values[j] + input_values[k] == target:
					return input_values[i] * input_values[j] * input_values[k] 

def part2_sumofthree(input_values, target):
	for combi in combinations(input_values, 3):
		if sum(combi) == target:
			return reduce(operator.mul, combi)

def targetsum_value_product(input_values, target, numofelements):
	numofParsed = 0
	for combi in combinations(input_values, numofelements):
		numofParsed += 1
		if sum(combi) == target:
			print("total number of parsed combinations", numofParsed)
			return reduce(operator.mul, combi)

	return 0

def read_input(filename):
	with open(filename) as file:
		input_values = [int(x.strip()) for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values = read_input("day1_input.txt")
	#input_values = [1721, 979, 366, 299, 675, 1456]
	#part1_ans = part1_sumoftwo(input_values, 2020)
	part1_ans = targetsum_value_product(input_values, 2020, 2)
	print(part1_ans)
	#part2_ans = part2_sumofthree(input_values, 2020)
	part2_ans = targetsum_value_product(input_values, 2020, 3)
	print(part2_ans)

