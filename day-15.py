from collections import defaultdict, deque
from functools import partial

def part1_2020recitation(starting_numbers, max_turn):
	turn_positions = defaultdict(partial(deque, maxlen=2))
	for i, val in enumerate(starting_numbers):
		turn_positions[val].append(i)

	current_turn = len(turn_positions)
	last_spoken = starting_numbers[-1]
	while current_turn <max_turn:
		#print(last_spoken, turn_positions)
		if last_spoken in turn_positions:
			if len(turn_positions[last_spoken]) > 1:
				recite = turn_positions[last_spoken][1]  - turn_positions[last_spoken][0]
				turn_positions[recite].append(current_turn)
				last_spoken = recite
			else:
				turn_positions[0].append(current_turn)
				last_spoken = 0

		current_turn += 1

	return last_spoken

if __name__ == '__main__':
	input_values = [1,3,2]
	#input_values = [0, 3, 6]
	#input_values = [3,1,2]
	#input_values = [3,2,1]
	input_values = [7,12,1,0,16,2]
	#input_values = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
	part1_ans = part1_2020recitation(input_values, 2020)
	print("part1 answer", part1_ans)
	part2_ans = part1_2020recitation(input_values, 30000000)
	print("part2 answer", part2_ans)

