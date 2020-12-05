
def part1_counttrees(toboggan_grid):
	numoftrees = 0
	width_of_grid = len(toboggan_grid[0])
	len_of_grid = len(toboggan_grid)
	i = j = 0

	while j < len_of_grid:
		if toboggan_grid[j][i] == '#':
			numoftrees += 1
		j += 1
		i = (i+3)%width_of_grid	

	return numoftrees


def part2_multipleslopes(toboggan_grid):
	productoftrees = 1
	width_of_grid = len(toboggan_grid[0])
	len_of_grid = len(toboggan_grid)
	
	for right, down in ((1,1), (3, 1), (5, 1), (7, 1), (1, 2)):
		i = j = 0
		numoftrees = 0
		while j < len_of_grid:
			if toboggan_grid[j][i] == '#':
				numoftrees += 1
			j += down
			i = (i+right)%width_of_grid

		productoftrees *= numoftrees

	return productoftrees


def read_input(filename):
	with open(filename) as file:
		input_values = [x.strip() for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values = ['..##.......',
				'#...#...#..',
				'.#....#..#.',
				'..#.#...#.#',
				'.#...##..#.',
				'..#.##.....',
				'.#.#.#....#',
				'.#........#',
				'#.##...#...',
				'#...##....#',
				'.#..#...#.#']
	#input_values = read_input("day3_input.txt")

	#input_values = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
	part1_ans = part1_counttrees(input_values)
	print("part1 answer", part1_ans)
	part2_ans = part2_multipleslopes(input_values)
	print("part2 answer", part2_ans)

