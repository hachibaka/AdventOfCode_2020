from collections import defaultdict

def part1_calc_manhattan_dist(instructions):
    mahattan_distance = 0
    current_facing = current_direction = 'E'
    directions = ['E', 'S', 'W', 'N']
    ship_distance = defaultdict(int)

    current_pos = 0
    for inst in instructions:
        instruction, arg = inst[0], int(inst[1:])
        if instruction == 'R' or instruction == 'L':
            turn_position = arg//90 if instruction == 'R' else -1 * (arg//90)
            current_pos = (current_pos+turn_position)%4
            current_facing = directions[current_pos]
        elif instruction == 'F':
            ship_distance[current_facing] += arg
        else:
            ship_distance[instruction] += arg

    mahattan_distance = abs(ship_distance['E'] - ship_distance['W'])  + abs(ship_distance['N'] - ship_distance['S'])

    return mahattan_distance


def part2_calc_manhattan_dist_waypoint(instructions):
    sx, sy = 0, 0
    wx, wy = 10, 1
    DELTAS = {
    "E": (1, 0),
    "N": (0, 1),
    "W": (-1, 0),
    "S": (0, -1)
}
    def move(x, y, n, direction):
        dx, dy = DELTAS[direction]
        return x + n * dx, y + n * dy


    for inst in instructions:
        instr, arg = inst[0], int(inst[1:])
        if (instr, arg) in {('L', 90), ('R', 270)}:
            wx, wy = -wy, wx
        elif (instr, arg) in {('L', 180), ('R', 180)}:
            wx, wy = -wx, -wy
        elif (instr, arg) in {('L', 270), ('R', 90)}:
            wx, wy = wy, -wx
        elif instr == "F":
            sx += wx * arg
            sy += wy * arg
        else:
            wx, wy =  move(wx, wy, arg, instr)
    return abs(sx) + abs(sy)


    mahattan_distance = abs(ship_distance['E'] - ship_distance['W'])  + abs(ship_distance['N'] - ship_distance['S'])

    return mahattan_distance


def read_input(filename):
    with open(filename) as file:
        input_values = [x.strip() for x in file.readlines()]

    return input_values


if __name__ == '__main__':
    input_values = read_input("day12_input.txt")
    #input_values = ['F10', 'N3','F7','R90','F11']
    part1_ans = part1_calc_manhattan_dist(input_values)
    print("part1 answer", part1_ans)
    part2_ans = part2_calc_manhattan_dist_waypoint(input_values)
    print("part2 answer", part2_ans)

