
with open('./input.txt') as f:
    input = f.read().rstrip().split('\n\n')


def compareLists(list1, list2):
    # If list1 is smaller, or same length or shorter, return True
    # If list2 is smaller, or shorter, return False
    val = None

    for i in range(len(list1)):
        sub1 = list1[i]
        sub2 = list2[i] if i < len(list2) else None
        if sub2 == None:
            return False # list2 is shorter

        if type(sub1) == list and type(sub2) == list:
            val = compareLists(sub1, sub2)
        elif type(sub1) == list and type(sub2) != list:
            val = compareLists(sub1, [sub2])
        elif type(sub1) != list and type(sub2) == list:
            val = compareLists([sub1], sub2)
        elif sub1 < sub2:
            return True  # el in list1 is smaller
        elif sub1 > sub2:
            return False # el in list2 is smaller

        if val != None:
            return val

    if len(list1) < len(list2):
        return True # list1 is shorter or equal


correctly_ordered_p1 = []
import json
for i in range(len(input)):
    pair = input[i]
    e_1, e_2 = [json.loads(x) for x in pair.split('\n')]
    correctly_ordered_p1.append(compareLists(e_1, e_2))
solution_p1 = 0
for i in range(len(correctly_ordered_p1)):
    if correctly_ordered_p1[i]:
        solution_p1 += i+1
print("1:", solution_p1)

def compareListSort(list1, list2):
    result = compareLists(list1, list2)
    if result:
        return -1
    else:
        return 1

from functools import cmp_to_key
input_p2 = []
for i in range(len(input)):
    pair = input[i]
    e_1, e_2 = [json.loads(x) for x in pair.split('\n')]
    input_p2.append(e_1)
    input_p2.append(e_2)

divider_1 = [[2]]
divider_2 = [[6]]

input_p2.append(divider_1)
input_p2.append(divider_2)

input_p2.sort(key=cmp_to_key(compareListSort))
solution_p2 = 1
solution_p2 *= input_p2.index(divider_1) + 1
solution_p2 *= input_p2.index(divider_2) + 1
print("2:", solution_p2)




