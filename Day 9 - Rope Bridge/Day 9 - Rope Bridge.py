with open('./input.txt') as f:
    movement_instructions = f.read().rstrip().split('\n')

# movement_instructions contains a list of actions
# Each action is a string of a direction (U, D, L, R) followed by a distance (integer)
# These actions are performed by the head
# The tail lags behind the head, and only moves if the distance between the head and the tail is greater than 1 unit each direction and diagonal
# Record the unique coordinates that the tail has visited


def move(direction, enitity):

    if direction == 'R':
        enitity = (enitity[0] + 1, enitity[1])
    elif direction == 'L':
        enitity = (enitity[0] - 1, enitity[1])
    elif direction == 'U':
        enitity = (enitity[0], enitity[1] + 1)
    elif direction == 'D':
        enitity = (enitity[0], enitity[1] - 1)

    elif direction == 'RU':
        enitity = (enitity[0] + 1, enitity[1] + 1)
    elif direction == 'RD':
        enitity = (enitity[0] + 1, enitity[1] - 1)
    elif direction == 'LU':
        enitity = (enitity[0] - 1, enitity[1] + 1)
    elif direction == 'LD':
        enitity = (enitity[0] - 1, enitity[1] - 1)

    return enitity

def get_tail_direction(head, tail):
    dir_tail = ''
    # Check if the tail is lagging behind the head
    if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) > 1:
        # The tail is lagging behind the head in both the x and y directions
        dir_tail = 'R' if head[0] > tail[0] else 'L'
        dir_tail += 'U' if head[1] > tail[1] else 'D'
    elif abs(head[0] - tail[0]) > 1:
        # The tail is lagging behind the head in the x direction
        dir_tail = 'R' if head[0] > tail[0] else 'L'
        dir_tail += 'U' if head[1] > tail[1] else 'D' if head[1] < tail[1] else ''
    elif abs(head[1] - tail[1]) > 1:
        # The tail is lagging behind the head in the y direction
        dir_tail = 'R' if head[0] > tail[0] else 'L' if head[0] < tail[0] else ''
        dir_tail += 'U' if head[1] > tail[1] else 'D'
    return dir_tail




# Part 1
# head = (0, 0)
# tail = (0, 0)
# tail_visited_p1 = set()
# tail_visited_p1.add(tail)
# for instruction in movement_instructions:
#     direction, distance = instruction.split(' ')
#     distance = int(distance)

#     for i in range(distance):
#         head = move(direction, head)

#         dir_tail = get_tail_direction()
#         tail = move(dir_tail, tail)
#         tail_visited_p1.add(tail)

# print("1:", len(tail_visited_p1))



# Part 2
head = (0, 0)
tail = [(0, 0) for i in range(1, 10)]
tail_visited_p2 = set()
tail_visited_p2.add(tail[-1])

for instruction in movement_instructions:
    direction, distance = instruction.split(' ')
    distance = int(distance)

    for i in range(distance):
        head = move(direction, head)

        dir_tail = get_tail_direction(head, tail[0])
        tail[0] = move(dir_tail, tail[0])

        for j in range(len(tail)-1):
            head_2 = tail[j]
            tail_2 = tail[j+1]

            dir_tail = get_tail_direction(head_2, tail_2)
            tail[j+1] = move(dir_tail, tail_2)
        tail_visited_p2.add(tail[-1])

print("2:", len(tail_visited_p2))