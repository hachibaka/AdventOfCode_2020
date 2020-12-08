from collections import defaultdict
import re


def part1_countbags(bag_rules):
    inverted_bag_rules = defaultdict(list)

    for outer_bag, inner_bags in bag_rules.items():
        for count, bag in inner_bags:
            inverted_bag_rules[bag].append(outer_bag)

    def _countouterbags(bag, seen={}):
        print(bag, inverted_bag_rules[bag])
        if bag in seen:
            return seen[bag]
        if seen and bag == 'shiny gold':
            return 0
        if not inverted_bag_rules[bag]:
            seen[bag] = 1
            return 1
        seen[bag] =  sum(_countouterbags(obag) for obag in inverted_bag_rules[bag])
        return seen[bag]

    print(_countouterbags('shiny gold'))





def part2_countallanswers(bag_rules):
    num_of_anwers = 0
    for group_answer in group_answers:
        ans_counter = Counter("".join(group_answer))
        num_of_anwers += sum(ans_counter[c] == len(group_answer) for c in ans_counter)

    return num_of_anwers


def read_input(filename):
    with open(filename) as file:
        bag_rules = {}
        for line in file:
            # print(line)
            outer_bag, inner_bags = line.split(" bags contain")
            bag_rules[outer_bag] = re.findall(r'([0-9]+) ([a-z ]+) bag[s]?', inner_bags.strip())

    return bag_rules


if __name__ == '__main__':
    bag_rules = read_input('day7_sample_input.txt')
    #print(bag_rules)
    #bag_rules = read_input("day7_input.txt")
    #print(bag_rules)
    part1_ans = part1_countbags(bag_rules)
    print("part1 answer", part1_ans)
    #part2_ans = part2_countallanswers(bag_rules)
    #print("part2 answer", part2_ans)
