from itertools import combinations

def part1_notsumofpreabmle(xmas_data, preamble_size):
	i = 0
	for number in xmas_data[preamble_size:]:
		if not targetsum_value_product(xmas_data[i:i+preamble_size], number, 2):
			return number
		i += 1


def part2_contiguousset(input_values, target):
	i = 0
	while i < len(input_values):
		totalsum = 0
		j = i
		contiguos_sum = []
		while totalsum <= target and j < len(input_values):
			totalsum += input_values[j]
			contiguos_sum.append(input_values[j])
			if totalsum == target and len(contiguos_sum) >= 2:
				return min(contiguos_sum) + max(contiguos_sum)
			j += 1
		i += 1


def targetsum_value_product(input_values, target, numofelements):
	numofParsed = 0
	for combi in combinations(input_values, numofelements):
		numofParsed += 1
		if sum(combi) == target:
			return True

	return False

def read_input(filename):
	with open(filename) as file:
		input_values = [int(x.strip()) for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values = read_input("day9_input.txt")
	#input_values = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
	part1_ans = part1_notsumofpreabmle(input_values, 25)
	print(part1_ans)
	part2_ans = part2_contiguousset(input_values, part1_ans)
	print(part2_ans)

