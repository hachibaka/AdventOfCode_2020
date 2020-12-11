from collections import defaultdict

def part1_joltdiff(adapters):
	differences = defaultdict(int)
	_sortandadd(adapters)
	
	for i in range(len(adapters)-1):
		if (adapters[i+1] - adapters[i]) <= 3:
			diff = adapters[i+1] - adapters[i]
			differences[diff] += 1

	return differences.get(1,0) * differences.get(3,0)


def _adaptercommbinations(combinations, start, seen={}):
	if not combinations[start]:
		return 1
	if start in seen:
		return seen[start]
	totalcombinations = sum(_adaptercommbinations(combinations, i) for i in combinations[start])
	seen[start] = totalcombinations
	return totalcombinations	
	

def part2_adaptercombinations(adapters):
	combinations = defaultdict(list)

	for i in range(len(adapters) - 1):
		for j in (1,2,3):
			if i+j < len(adapters) and (adapters[i+j] - adapters[i]) <= 3:
				combinations[adapters[i]].append(adapters[i+j])

	totalcombinations =_adaptercommbinations(combinations, 0)
	return totalcombinations


def _sortandadd(adapters):
	adapters.sort()
	adapters.append(adapters[-1]+3)
	adapters.insert(0,0)



def read_input(filename):
	with open(filename) as file:
		input_values = [int(x.strip()) for x in file.readlines()]
	
	return input_values


if __name__ == '__main__':
	input_values = read_input("day10_input.txt")
	#input_values = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,79,4,2,34,10,3]
	#input_values = [16,10,15,5,1,11,7,19,6,12,4]
	part1_ans = part1_joltdiff(input_values)
	print("part1 answer", part1_ans)
	part2_ans = part2_adaptercombinations(input_values)
	print("part2 answer", part2_ans)


