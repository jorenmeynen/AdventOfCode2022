with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

stacks_input = []
instructions = []

for line in input:
    if not line.startswith('move'):
        if line == '':
            continue
        stacks_input.append(line)
    else:
        instructions.append(line)

stacks_input.reverse()
stacks_p1 = []
for i, stack_number in enumerate(stacks_input[0]):
    if stack_number == ' ':
        continue
    stack = []
    for crate in stacks_input[1:]:
        if crate[i] == ' ':
            continue
        stack.append(crate[i])
    stacks_p1.append(stack)

import copy

stacks_p2 = copy.deepcopy(stacks_p1)

for instruction in instructions:
    instruction = instruction.split(' ')
    amount = int(instruction[1])
    crate_from = int(instruction[3])
    crate_to = int(instruction[5])

    crates_to_move = stacks_p1[crate_from-1][-amount:]
    stacks_p1[crate_from-1] = stacks_p1[crate_from-1][:-amount]
    crates_to_move.reverse()
    stacks_p1[crate_to-1] += crates_to_move

    crates_to_move_p2 = stacks_p2[crate_from-1][-amount:]
    stacks_p2[crate_from-1] = stacks_p2[crate_from-1][:-amount]
    stacks_p2[crate_to-1] += crates_to_move_p2



crates_on_top_p1 = "".join([stack[-1] for stack in stacks_p1])
crates_on_top_p2 = "".join([stack[-1] for stack in stacks_p2])

print("1:", crates_on_top_p1)
print("2:", crates_on_top_p2)

    

