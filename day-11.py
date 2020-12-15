import copy 
import  time

adjacent_nodes = [(-1,-1),   #Top Diagonal left
				 (-1,0),    #Right above
				 (-1,1),    #Top Diagonal Right
				 (0,1),     #to the right
				 (1,1),     #Bottom Diagonal right
			     (1,0),     #Right below
				 (1,-1),    #Bottom Diagonal left
				 (0,-1)]    #to the left



def _simulateseatoccupation1(seatlayout):
	occupiedseat = copy.deepcopy(seatlayout)
	i = j = 0
	seatwidth = len(seatlayout[0])

	def _checkadjacentseatsempty(i,j):
		for y, x in adjacent_nodes:
			if 0 <= i+y < len(seatlayout) and 0 <= j+x < len(seatlayout[0]):
				if seatlayout[i+y][j+x] == '#':
					return False
		return True
		
	for i in range(len(seatlayout)):
		for j in range(seatwidth):
			if occupiedseat[i][j] == 'L' and _checkadjacentseatsempty(i,j):
				occupiedseat[i][j] = '#'

	return occupiedseat

def _simulateseatadjustment1(seatlayout):
	occupiedseat = copy.deepcopy(seatlayout)
	seatwidth = len(seatlayout[0])

	def _checkadjacentseatsoccupied(i,j):
		numoccupied = 0 
		for y, x in adjacent_nodes:
			if 0 <= i+y < len(seatlayout) and 0 <= j+x < len(seatlayout[0]):
				if seatlayout[i+y][j+x] == '#':
					numoccupied += 1
		return True if numoccupied>=4 else False

	for i in range(len(seatlayout)):
		for j in range(seatwidth):
			if occupiedseat[i][j] == '#' and _checkadjacentseatsoccupied(i,j):
				occupiedseat[i][j] = 'L'

	return occupiedseat

def _simulateseatoccupation2(seatlayout):
	occupiedseat = copy.deepcopy(seatlayout)
	i = j = 0
	seatwidth = len(seatlayout[0])
	seatlength  = len(seatlayout)

	def _checkadjacentseatsempty(i,j):
		for y, x in adjacent_nodes:
			k, l = y, x 
			while 0 <= i+k < seatlength and 0 <= j+l < seatwidth:
				if seatlayout[i+k][j+l] == '#':
					return False
				elif seatlayout[i+k][j+l] == 'L':
					break
				k += y
				l += x
		return True
		
	for i in range(seatlength):
		for j in range(seatwidth):
			if occupiedseat[i][j] == 'L' and _checkadjacentseatsempty(i,j):
				occupiedseat[i][j] = '#'

	return occupiedseat

def _simulateseatadjustment2(seatlayout):
	occupiedseat = copy.deepcopy(seatlayout)
	seatwidth = len(seatlayout[0])
	#print("Seat layout before applying second rule ", _getformattedlayout(seatlayout))
	def _checkadjacentseatsoccupied(i,j):
		numoccupied = 0 
		for y, x in adjacent_nodes:
			k, l = y, x 
			while 0 <= i+k < len(seatlayout) and 0 <= j+l < len(seatlayout[0]):
				if seatlayout[i+k][j+l] == '#':
					numoccupied += 1
					break
				elif seatlayout[i+k][j+l] == 'L':
					break
				k += y
				l += x
		return True if numoccupied>=5 else False

	for i in range(len(seatlayout)):
		for j in range(seatwidth):
			if occupiedseat[i][j] == '#' and _checkadjacentseatsoccupied(i,j):
				occupiedseat[i][j] = 'L'

	return occupiedseat


def _getformattedlayout(seatlayout):
	return "|".join("".join(x) for x in seatlayout)


def part1_cacl_occupied_seats(seatlayout):
	totaloccupiedseats = 0
	previouslayout = _getformattedlayout(seatlayout)
	
	while True:
		seatlayout = _simulateseatoccupation1(seatlayout)
		seatlayout = _simulateseatadjustment1(seatlayout)
		current_layout =  _getformattedlayout(seatlayout)
		#print(f"Previous Layout = {previouslayout} \n After simulation layout = {current_layout}\n\n")
		if previouslayout == current_layout:
			break
		else:
			previouslayout = current_layout


	totaloccupiedseats = sum(1 for sublayout in seatlayout for seat in sublayout if seat == '#')

	return totaloccupiedseats
	


def part2_cacl_occupied_seat(seatlayout):
	totaloccupiedseats = 0
	previouslayout = _getformattedlayout(seatlayout)
	i =  0 
	while True:
		seatlayout = _simulateseatoccupation2(seatlayout)
		seatlayout = _simulateseatadjustment2(seatlayout)
		current_layout =  _getformattedlayout(seatlayout)
		#print(f"Previous Layout = {previouslayout} \n After simulation layout = {current_layout}\n\n")
		if previouslayout == current_layout:
			break
		else:
			previouslayout = current_layout

		i += 1

	totaloccupiedseats = sum(1 for sublayout in seatlayout for seat in sublayout if seat == '#')

	return totaloccupiedseats


def read_input(filename):
	with open(filename) as file:
		input_values = [list(x.strip()) for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values_sample = ['L.LL.LL.LL',
				'LLLLLLL.LL',
				'L.L.L..L..',
				'LLLL.LL.LL',
				'L.LL.LL.LL',
				'L.LLLLL.LL',
				'..L.L.....',
				'LLLLLLLLLL',
				'L.LLLLLL.L',
				'L.LLLLL.LL']
	input_values = [list(x) for x in input_values_sample]
	input_values = read_input("day11_input.txt")
	start_time = time.time()
	part1_ans = part1_cacl_occupied_seats(input_values)
	print("part1 answer", part1_ans)
	print(f"total time taken is {time.time() - start_time}")
	start_time = time.time()
	part2_ans = part2_cacl_occupied_seat(input_values)
	print("part2 answer", part2_ans)
	print(f"total time taken is {time.time() - start_time}")

