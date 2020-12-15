from itertools import product


def _getmaskeddata(input_bits, bitmask):
	return "".join(i if o =='X' else o for i,o in zip(input_bits, bitmask))

def _getmaskedmemory(memory_value, bitmask, floating_bits):
	memory_bits = "{:036b}".format(int(memory_value))
	memory_masked_bits = []
	for i, ch in enumerate(memory_bits):
		if bitmask[i] == '0':
			memory_masked_bits.append(ch)
		elif bitmask[i] == '1':
			memory_masked_bits.append('1')
		else:
			memory_masked_bits.append('{}')

	masked_memory = "".join(memory_masked_bits)
	for floating_bit in floating_bits:
		yield masked_memory.format(*floating_bit)



def _generatefloatingbits(bitmask):
	float_len = bitmask.count('X')
	bits = "01"
	return list(product(bits, repeat=float_len))


def part1_bitmaskvalue(bitmask_instructions):
	memory = {}
	bitmask = None
	for instructions in bitmask_instructions:
		if instructions.startswith('mask'):
			_, bitmask = instructions.split(' = ')

		else:
			memlocation, value = instructions.split(' = ')
			memlocation = int(memlocation.strip('[]mem'))
			input_value_bits = "{:036b}".format(int(value))
			masked_data = _getmaskeddata(input_value_bits, bitmask)
			memory[memlocation] = int(masked_data, 2)


	return sum(memory.values())
	


def part2_bitmask_memory(bitmask_instructions):
	memory = {}
	bitmask = None
	for instructions in bitmask_instructions:
		if instructions.startswith('mask'):
			_, bitmask = instructions.split(' = ')
			floating_bits = _generatefloatingbits(bitmask)
		else:
			memlocation, value = instructions.split(' = ')
			memlocation = int(memlocation.strip('[]mem'))
			
			for masked_mem in _getmaskedmemory(memlocation, bitmask, floating_bits):
				memory_loc = int(masked_mem,2)
				memory[memory_loc] = int(value)


	return sum(memory.values())


def read_input(filename):
	with open(filename) as file:
		input_values = [x.strip() for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
				'mem[8] = 11',
				'mem[7] = 101',
				'mem[8] = 0']
	input_values = ['mask = 000000000000000000000000000000X1001X',
					'mem[42] = 100',
					'mask = 00000000000000000000000000000000X0XX',
					'mem[26] = 1']
	input_values = read_input("day14_input.txt")
	start_time = time.time()
	part1_ans = part1_bitmaskvalue(input_values)
	print("part1 answer", part1_ans)
		
	part2_ans = part2_bitmask_memory(input_values)
	print("part2 answer", part2_ans)
	

