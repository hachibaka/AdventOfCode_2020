from collections import Counter


def part1_countanswers(group_answers):
    num_of_anwers = sum(len(set("".join(group_answer))) for group_answer in group_answers)
    return num_of_anwers


def part2_countallanswers(group_answers):
    num_of_anwers = 0
    for group_answer in group_answers:
        ans_counter = Counter("".join(group_answer))
        num_of_anwers += sum(ans_counter[c] == len(group_answer) for c in ans_counter)

    return num_of_anwers


def read_input(filename):
    with open(filename) as file:
        group_answers = []
        person_answers = []
        for line in file:
            # print(line)
            if not line.strip():
                group_answers.append(person_answers)
                person_answers = []
            else:
                person_answers.append(line.strip())

        if person_answers:
            group_answers.append(person_answers)

    return group_answers


if __name__ == '__main__':
    group_answers = read_input('day6_sample_input.txt')
    # print(group_answers)
    group_answers = read_input("day6_input.txt")
    part1_ans = part1_countanswers(group_answers)
    print("part1 answer", part1_ans)
    part2_ans = part2_countallanswers(group_answers)
    print("part2 answer", part2_ans)
