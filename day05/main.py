def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read().split('\n')
    return values


def first_section(values):  # get info about first section of input
    i = 0
    while values[i][1] != '1':  # go through lines until reach 1 2 3 etc line
        i += 1
    stack_count = int(values[i][-1])  # get last character from 1 2 3 etc line
    return values[:i], i, stack_count


def make_stacks_list(stacks, stacks_count):
    line = len(stacks) - 1  # to start at bottom of stacks
    stacks_list = [[] for _ in range(stacks_count)]  # initialise list of stacks with empty lists
    while line >= 0:  # until and including line 0
        for i in range(0, stacks_count):  # go through each stack's item at this level
            if i * 4 + 1 > len(stacks[line]):  # if the line ends early because later stacks don't go this high, break
                break
            char = stacks[line][i * 4 + 1]  # get character for stack i. There are 4 characters per stack eg '[A] '
            if char != ' ':  # if the stack doesn't go this high, there will be a space instead of an item
                stacks_list[i].append(char)  # to the list of items in this stack, add the item
        line -= 1  # go up a row
    return stacks_list


def read_moves(moves_lines):  # turn the strings into tuples of 3 eg (5, 1, 3)
    moves = []
    for move_line in moves_lines:
        split_space = move_line.split(' ')
        moves.append((int(split_space[1]), int(split_space[3]) - 1, int(split_space[5]) - 1))  # put numbers into tuple
    return moves


def do_moves_p1(stacks, moves):
    for move in moves:
        for i in range(move[0]):  # so the move repeats the right number of times
            stacks[move[2]].append(stacks[move[1]].pop())  # remove from one stack, add to other
    return stacks


def do_moves_p2(stacks, moves):
    for move in moves:
        split_at = move[0]  # how far down the stack to remove
        leave_stack = stacks[move[1]]  # stack to remove from
        to_move, to_keep = leave_stack[-split_at:], leave_stack[:-split_at]  # split stack into two parts
        stacks[move[1]] = to_keep  # keep the keeping part
        stacks[move[2]] += to_move  # add the moving part to other stack
    return stacks


def output_for(stacks):  # get the top item of each stack
    out = ''
    for stack in stacks:
        out += stack[-1]
    return out


def p1(values):
    stacks, section_end, stacks_count = first_section(values)
    stacks_list = make_stacks_list(stacks, stacks_count)
    moves = read_moves(values[section_end + 2:])
    stacks_list_after_1 = do_moves_p1(stacks_list, moves)
    return output_for(stacks_list_after_1)


def p2(values):
    stacks, section_end, stack_count = first_section(values)
    stacks_list = make_stacks_list(stacks, stack_count)
    moves = read_moves(values[section_end + 2:])
    stacks_list_after_2 = do_moves_p2(stacks_list, moves)
    return output_for(stacks_list_after_2)


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
