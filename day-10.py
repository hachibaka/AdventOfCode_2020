#from itertools import combinations
from collections import defaultdict

def part1_joltdiff(adapters):
	differences = defaultdict(int)
	adapters.sort()
	adapters.append(adapters[-1]+3)
	adapters = [0] + adapters
	for i in range(len(adapters)-1):
		if (adapters[i+1] - adapters[i]) in (1,2,3):
			diff = adapters[i+1] - adapters[i]
			differences[diff] += 1

	return differences.get(1,0) * differences.get(3,0)

def _adaptercommbinations(combinations, start):
	if len(combinations[start]) == 1:
		return 1
	return sum(_adaptercommbinations(combinations, i) for i in combinations[start])

def part2_adaptercombinations(adapters):
	combinations = defaultdict(list)
	adapters.sort()
	adapters.append(adapters[-1] + 3)
	adapters = [0] + adapters
	for i in range(len(adapters) - 1):
		for j in (1,2,3):
			if i+j < len(adapters) and (adapters[i+j] - adapters[i]) in (1,2,3):
				combinations[adapters[i]].append(adapters[i+j])

	print(combinations)







def read_input(filename):
	with open(filename) as file:
		input_values = [int(x.strip()) for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	#input_values = read_input("day10_input.txt")
	#input_values = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,79,4,2,34,10,3]
	input_values = [16,10,15,5,1,11,7,19,6,12,4]
	part1_ans = part1_joltdiff(input_values)
	print(part1_ans)
	part2_ans = part2_adaptercombinations(input_values)
	#print(part2_ans)

