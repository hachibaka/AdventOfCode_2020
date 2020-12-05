import re

def part1_countvalidpassports(passports):
	numofvalidpassports = 0
	
	valid_fields =  {'ecl', 'pid', 'eyr', 'byr', 'iyr', 'hgt', 'hcl', 'cid'}
	
	for passport in passports:
		fields_difference = valid_fields.difference(set(passport.keys()))
		if not fields_difference  or fields_difference == {'cid'}:
			numofvalidpassports += 1
	return numofvalidpassports


def part2_countvaliddatapassports(passports):
	numofvalidpassports = 0

	def validate_data(string, regex=r'.*', number_range=None, hgt=False):
		valid = False
		if regex:
			data = re.findall(regex, string)
			if data:
				valid = True
				if number_range:
					valid = False
					if hgt:
						number_range = number_range[data[0][1]]
						data = data[0][0]
					else:
						data = data[0]
					min_range, max_range = number_range
					if min_range <= int(data) <= max_range:
						valid= True

		return valid
	
	valid_fields =  {
					'ecl': {'regex': r'^amb|blu|brn|gry|grn|hzl|oth$'}, 
					'pid' : {'regex': r'^\d{9}$'},
				    'eyr': {'regex': r'^\d{4}$', 'number_range': (2020, 2030)}, 
				    'byr':{'regex': r'^\d{4}$', 'number_range': (1920, 2002)}, 
				    'iyr':{'regex': r'^\d{4}$','number_range': (2010, 2020)},
				     'hgt':{'regex': r'^(\d+)(in|cm)$','number_range': {'in':(59, 76), 'cm': (150, 193)}, 'hgt':True},
				     'hcl':{'regex':r'^#[0-9a-f]{6}$'}, 	
				     'cid':{}
				     }
	
	for passport in passports:
		fields_difference = set(valid_fields.keys()).difference(set(passport.keys()))
		if not fields_difference  or fields_difference == {'cid'}:
			if all(validate_data(value, **valid_fields[key]) for key, value in passport.items()):
				numofvalidpassports += 1
				
	return numofvalidpassports


def read_input(filename):
	with open(filename) as file:
		passports = []
		passport= {}
		for line in file.readlines():
			#print(line)
			if not line.strip():
				passports.append(passport)
				passport = {}
			else:
				passport.update({entity.split(':')[0]:entity.split(':')[1] for entity in line.split()})

		if passport:
			passports.append(passport)
		

	return passports


if __name__ == '__main__':
	passports = read_input('day4_sample_input2.txt')
	#print(passports)
	passports = read_input("day4_input.txt")

	#input_values = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
	part1_ans = part1_countvalidpassports(passports)
	print("part1 answer", part1_ans)
	part2_ans = part2_countvaliddatapassports(passports)
	print("part2 answer", part2_ans)


