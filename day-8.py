import copy
def part1_accumulator(instructions):
	accumulator = 0
	seen = set()
	i = 0
	validrun = False
	while True:
		if i == len(instructions) -1:  #checking last instructions has been run
			validrun = True

		if i >= len(instructions) or i < 0:
			return None, True
		if i in seen:
			return accumulator, True
		else:
			seen.add(i)
			op, arg = instructions[i].split()
			arg = int(arg)
			if op == 'acc':
				accumulator += arg
				i += 1
			elif op == 'jmp':
				i += arg
			else:
				i += 1
		if 	validrun:
			return accumulator, False

	return accumulator, False


def part2_breakloop(instructions):
	accumulator = 0
	i = 0
	for i in range(1, len(instructions)):
		op, _ = instructions[i].split()
		if op == 'jmp':
			new_instructions = copy.copy(instructions)
			new_instructions[i] = new_instructions[i].replace('jmp','nop')
			new_acc, invalid = part1_accumulator(new_instructions)
			if not invalid:
				return new_acc
		elif op == 'nop':
			new_instructions = copy.copy(instructions)
			new_instructions[i] = new_instructions[i].replace('nop','jmp')
			new_acc, loop = part1_accumulator(new_instructions)
			if not loop:
				return new_acc

def read_input(filename):
	with open(filename) as file:
		input_values = [x.strip() for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values = ['nop +0',
'acc +1',
'jmp +4',
'acc +3',
'jmp -3',
'acc -99',
'acc +1',
'jmp -4',
'acc +6']
	input_values = read_input("day8_input.txt")
	part1_ans = part1_accumulator(input_values)
	print("part1 answer", part1_ans)
	part2_ans = part2_breakloop(input_values)
	print("part2 answer", part2_ans)

