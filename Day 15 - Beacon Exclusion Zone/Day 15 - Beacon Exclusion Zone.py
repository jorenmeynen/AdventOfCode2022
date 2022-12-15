with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

def prepareInput(input):
    coords = []
    for i in range(len(input)):
        line = input[i].split(' ')
        sensor_x = int(line[2].split('=')[1].rstrip(','))
        sensor_y = int(line[3].split('=')[1].rstrip(':'))
        beacon_x = int(line[8].split('=')[1].rstrip(','))
        beacon_y = int(line[9].split('=')[1])
        coords.append({
            'sensor': (sensor_x, sensor_y),
            'beacon': (beacon_x, beacon_y),
            'distance': abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y),
        })
    return coords

def get_occupied_coords(coords, given_y):
    occupied_coords = set()
    for coord in coords:
        if coord['sensor'][1] == given_y:
            occupied_coords.add((coord['sensor'][0], coord['sensor'][1]))
        if coord['beacon'][1] == given_y:
            occupied_coords.add((coord['beacon'][0], coord['beacon'][1]))
    return occupied_coords

def filter_sensors(coord, given_y):
    if coord['sensor'][1] >= given_y:
        return coord['sensor'][1] - coord['distance'] <= given_y
    else:
        return coord['sensor'][1] + coord['distance'] >= given_y

def get_min_max_x(coords, given_y, min_x1=None, max_x1=None):
    list_min_x = []
    list_max_x = []
    for coord in coords:
        distance_to_y = abs(coord['sensor'][1] - given_y)
        x_distance = coord['distance'] - distance_to_y
        min_x = coord['sensor'][0] - x_distance if min_x1 is None else max(min_x1, coord['sensor'][0] - x_distance)
        max_x = coord['sensor'][0] + x_distance if max_x1 is None else min(max_x1, coord['sensor'][0] + x_distance)
        list_min_x.append(min_x)
        list_max_x.append(max_x)
    return list_min_x, list_max_x

def get_min_max_x2(coords, given_y, min_x_=None, max_x_=None):
    list_min_max_x = []
    for coord in coords:
        distance_to_y = abs(coord['sensor'][1] - given_y)
        x_distance = coord['distance'] - distance_to_y
        min_x = coord['sensor'][0] - x_distance if min_x_ is None else max(min_x_, coord['sensor'][0] - x_distance)
        max_x = coord['sensor'][0] + x_distance if max_x_ is None else min(max_x_, coord['sensor'][0] + x_distance)
        list_min_max_x.append([min_x, max_x])
    return list_min_max_x


def part1():
    global coords
    global given_y

    occupied_coords = get_occupied_coords(coords, given_y)
    coords_filtered = list(filter(lambda x: filter_sensors(x, given_y), coords))
    list_min_max_x = get_min_max_x2(coords_filtered, given_y)

    # Get all numbers in range of min_x and max_x
    min_x = sorted(list_min_max_x, key=lambda x: x[0])[0][0]
    max_x = sorted(list_min_max_x, key=lambda x: x[1])[-1][1]
    all_covered_coords = (max_x - min_x + 1) - len(occupied_coords)
    return all_covered_coords
    

def part2(given_y):
    global coords

    coords_filtered = list(filter(lambda x: filter_sensors(x, given_y), coords))
    list_min_max_x = get_min_max_x2(coords_filtered, given_y, min_x_=0, max_x_=4_000_000)
    list_min_max_x.sort(key=lambda x: x[0])

    covered_cords = list_min_max_x[0]
    x = None
    for i in range(1,len(list_min_max_x)):
        if covered_cords[1] + 2 == list_min_max_x[i][0]:
            # the missing beacon
            x = covered_cords[1] + 1
            return x
        if covered_cords[1] < list_min_max_x[i][0]:
            # separate
            covered_cords = list_min_max_x[i]
        else:
            # overlap
            new_max = max(covered_cords[1], list_min_max_x[i][1])
            covered_cords = [covered_cords[0], new_max]
    return None



# given_y = 10
given_y = 2_000_000
coords = prepareInput(input)

all_covered_coords = part1()
print("1:", all_covered_coords)

for i in range(0, 4_000_000):
    given_y = i
    x = part2(i)
    if x is not None:
        print(f'x: {x}, y: {i}')
        print(f'2: {4_000_000 * x + i}')
        break

