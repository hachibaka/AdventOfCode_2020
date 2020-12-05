from collections import Counter

def part1_validpassword(input_passwords):
	valid_pass = 0
	for value in input_passwords:
		policy, password = value.split(':')
		policy_range, policy_char = policy.split()
		cmin, cmax = map(int,policy_range.split('-'))
		pass_counter = Counter(password.strip())
		if cmin <= pass_counter[policy_char] <= cmax:
			#print(password)
			valid_pass += 1

	return valid_pass


def part2_validbyposition(input_passwords):
	valid_pass = 0
	for value in input_passwords:
		policy, password = value.split(':')
		password = password.strip()
		policy_range, policy_char = policy.split()
		pos1, pos2 = map(int,policy_range.split('-'))
		
		if password[pos1-1] == policy_char and password[pos2-1] == policy_char:
			continue
		elif password[pos1-1] == policy_char or password[pos2-1] == policy_char:
			valid_pass += 1

	return valid_pass


def read_input(filename):
	with open(filename) as file:
		input_values = [x.strip() for x in file.readlines()]

	return input_values


if __name__ == '__main__':
	input_values = read_input("day2_input.txt")
	#input_values = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
	part1_ans = part1_validpassword(input_values)
	print("part1 answer", part1_ans)
	part2_ans = part2_validbyposition(input_values)
	print("part2 answer", part2_ans)

