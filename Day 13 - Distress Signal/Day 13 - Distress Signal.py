
with open('./input.txt') as f:
    input = f.read().rstrip().split('\n\n')


def compareLists(list1, list2):
    # If list1 is smaller, or same length or shorter, return True
    # If list2 is smaller, or shorter, return False

    for i in range(len(list1)):
        sub1 = list1[i]
        sub2 = list2[i] if i < len(list2) else None
        if sub2 == None:
            return False # list2 is shorter

        if type(sub1) == list and type(sub2) == list:
            return compareLists(sub1, sub2)
        elif type(sub1) == list and type(sub2) != list:
            return compareLists(sub1, [sub2])
        elif type(sub1) != list and type(sub2) == list:
            return compareLists([sub1], sub2)

        if sub1 < sub2:
            return True  # el in list1 is smaller
        elif sub1 > sub2:
            return False # el in list2 is smaller

    return True # list1 is shorter or equal


def comparePair(pair):
    e_1, e_2 = pair
    return compareLists(e_1, e_2)

correctly_ordered = []
import json
for i in range(len(input)):
    e_1, e_2 = [json.loads(x) for x in input[i].split('\n')]
    correctly_ordered.append(compareLists(e_1, e_2))

solution_p1 = 0
for i in range(len(correctly_ordered)):
    if correctly_ordered[i]:
        solution_p1 += i+1


print("1:", solution_p1)



