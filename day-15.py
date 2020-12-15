from collections import defaultdict
from functools import  wraps
import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:{} args:[{}, {}] took: {:2.4f} sec'.format(f.__name__, args, kw, te-ts))
        return result
    return wrap

@timing    
def part1_2020recitation(starting_numbers, max_turn):
	
	turn_positions = defaultdict(tuple)
	
	for i, val in enumerate(starting_numbers):
		turn_positions[val] = (None,i)

	current_turn = len(turn_positions)
	last_spoken = starting_numbers[-1]
	while current_turn <max_turn:
		if last_spoken in turn_positions:
			if turn_positions[last_spoken][0] is not None:
				recite = turn_positions[last_spoken][1]  - turn_positions[last_spoken][0]
				if not turn_positions[recite]:
					turn_positions[recite] = (None, current_turn)
				else:
					turn_positions[recite] = (turn_positions[recite][1], current_turn)

				last_spoken = recite
			else:
				turn_positions[0] = (turn_positions[0][1], current_turn)
				last_spoken = 0

		current_turn += 1

	return last_spoken


if __name__ == '__main__':
	input_values = [1,3,2]
	#input_values = [0, 3, 6]
	#input_values = [3,1,2]
	#input_values = [3,2,1]
	input_values = [7,12,1,0,16,2]
	part1_ans = part1_2020recitation(input_values, 2020)
	print("part1 answer", part1_ans)

	part2_ans = part1_2020recitation(input_values, 30000000)
	print("part2 answer", part2_ans)
	

