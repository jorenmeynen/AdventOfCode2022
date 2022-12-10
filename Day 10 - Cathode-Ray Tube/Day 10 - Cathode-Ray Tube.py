with open('./input.txt') as f:
    instructions = f.read().rstrip().split('\n')

to_add = None
value_x = 1
cycle = 0
cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = []
signal_strengths_str = []

# image = [''.join('.' for i in range(40)) for j in range(6)]
image = [['.' for i in range(40)] for j in range(6)]

instr_index = 0

def add_to_image(image, value_x, cycle):
    position = cycle - 1
    row = position // 40
    col = (position % 40)
    lit_up = [value_x - 1, value_x, value_x + 1]

    if col in lit_up:
        image[row][col] = '#'


for cycle in range(1, len(instructions)*2):

    if cycle in cycles:
        signal_strengths_str.append(f"{value_x} * {cycle} = {value_x*cycle}")
        signal_strengths.append(value_x*cycle)
    
    add_to_image(image, value_x, cycle)

    if to_add is not None:
        value_x += to_add
        to_add = None
    else:
        if instr_index == len(instructions):
            break
        operation = instructions[instr_index].split(' ')
        instr_index += 1
        if operation[0] == 'noop':
            pass
        elif operation[0] == 'addx':
            to_add = int(operation[1])


print("1:", sum(signal_strengths))
print("2:")
for row in image:
    print(''.join(row))