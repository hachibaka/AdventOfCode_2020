
def getpos(rowmap, direction1, direction2, start, end):
	for row_pos in rowmap:
		if row_pos == direction1:
			end = start + (end-start)//2
		elif row_pos == direction2:
			start = (end-start)//2 + start + 1

	if row_pos == direction1:
		return start
	else:
		return end


def part1_maxseatid(seats):
	maxseatid = 0
	seatids = []
	for seat in seats:
		rowpos = getpos(seat[:7], 'F', 'B', 0, 127)
		colpos = getpos(seat[-3:], 'L', 'R', 0, 7)
		#print(seat, rowpos, colpos)
		seatid = rowpos * 8 + colpos
		seatid_binary = "".join('1' if char == 'R' or char == 'B' else '0' for char in seat)
		print(seatid, int(seatid_binary,2))

		seatids.append(seatid)
		if seatid > maxseatid:
			maxseatid = seatid

	return maxseatid, seatids


def part2_findseatid(seatids):
	seatids.sort()

	for i in range(len(seatids)-1):
		if seatids[i] + 2 == seatids[i+1]:
			return seatids[i]+1


def read_input(filename):
	with open(filename) as file:
		seats = [seat.strip() for seat in file.readlines()]
		
	return seats


if __name__ == '__main__':
	seats = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
	#seats = read_input("day5_input.txt")
	part1_ans, seatids = part1_maxseatid(seats)
	print("part1 answer", part1_ans)
	part2_ans = part2_findseatid(seatids)
	print("part2 answer", part2_ans)


