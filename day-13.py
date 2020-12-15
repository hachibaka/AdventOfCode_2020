

def part1_earliestbus(bus_inputs):
	mytime, busids = bus_inputs
	
	reminders = [busid - mytime%busid if busid != 'x' else 9999999999   for busid in busids]
	min_reminder = min(reminders)
	return min_reminder * busids[reminders.index(min_reminder)]


def part2_earliestoffset(busids):
	earliest_offfset, step = 0, 1

	#Learned from reddit, this can solved using Chinese reminder theorem .
	#Otherwise naive way of checking takes forever.
	#Basically find the offsert which works for k+1 busid and increment the steps accordingly.
	for pos, val in enumerate(busids):
		if val != 'x':
			while (earliest_offfset+pos)%val !=0:
				earliest_offfset += step

			step *=val

	return earliest_offfset



def read_input(filename):
	with open(filename) as file:
		passports = []
		passport= {}
		mytime = int(file.readline().strip())
		busids = [int(x) if x != 'x' else x for x in file.readline().strip().split(',') ]
		
	return (mytime, busids)


if __name__ == '__main__':
	bus_inputs = (939,[7, 13, 'x', 'x', 59,'x', 31, 19])
	bus_inputs = read_input("day13_input.txt")
	part1_ans = part1_earliestbus(bus_inputs)
	print("part1 answer", part1_ans)
	part2_ans = part2_earliestoffset(bus_inputs[1])
	print("part2 answer", part2_ans)


