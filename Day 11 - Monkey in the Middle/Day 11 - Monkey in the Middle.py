with open('./Day 11 - Monkey in the Middle/input.txt') as f:
    input = f.read().rstrip().split('\n\n')

import re
monkeys = []
for input_monkey in input:
    monkey_lines = input_monkey.split('\n')
    monkey = {}

    items = re.split(r' |,', monkey_lines[1])
    monkey['items'] = []
    for item in items:
        if item.isdigit():
            monkey['items'].append(int(item))

    monkey['operation'] = monkey_lines[2][13:]
    monkey['division_test'] = int(monkey_lines[3].split(' ')[-1])
    monkey['true'] = int(monkey_lines[4].split(' ')[-1])
    monkey['false'] = int(monkey_lines[5].split(' ')[-1])

    monkeys.append(monkey)

import math
def monkey_business(monkeys, rounds, decrease_worry_lvl):
    inspect_count = [0] * len(monkeys)

    LEAST_COMMON_MULTIPLE = math.prod(map(lambda x: x['division_test'], monkeys))

    for round in range(rounds):
        # print(f"Round {round + 1}:")
        for monkey_index in range(len(monkeys)):
            monkey = monkeys[monkey_index]
            for item in monkey['items']:
                inspect_count[monkey_index] += 1

                operation = monkey['operation'].split(' ')
                if operation[-1] == 'old':
                    item_worry_lvl = item ** 2
                elif operation[-2] == '+':
                    item_worry_lvl = item + int(operation[-1])
                elif operation[-2] == '*':
                    item_worry_lvl = item * int(operation[-1])
                
                if decrease_worry_lvl:
                    item_worry_lvl = math.floor(item_worry_lvl / 3)
                else:
                    item_worry_lvl = item_worry_lvl % LEAST_COMMON_MULTIPLE

                if item_worry_lvl % monkey['division_test'] == 0:
                    monkeys[monkey['true']]['items'].append(item_worry_lvl)
                else:
                    monkeys[monkey['false']]['items'].append(item_worry_lvl)
            
            monkey['items'].clear()

    return inspect_count


from copy import deepcopy 

insp_c_p1 = monkey_business(deepcopy(monkeys), 20, True)
insp_c_p1.sort(reverse=True)
print("1:", insp_c_p1[0] * insp_c_p1[1])


insp_c_p2 = monkey_business(deepcopy(monkeys), 10000, False)
insp_c_p2.sort(reverse=True)
print("2:", insp_c_p2[0] * insp_c_p2[1])