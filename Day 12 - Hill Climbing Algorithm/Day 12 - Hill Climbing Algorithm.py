
with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

# Check if two nodes are traversable
def is_traversable(current, next):
    elevation_difference = 0
    if current == 'S':
        elevation_difference = ord(next) - ord('a') + 1
    elif current == 'E':
        elevation_difference = ord('z') - ord(next) + 1
    elif next == 'S':
        elevation_difference = ord(current) - ord('a')
    elif next == 'E':
        elevation_difference = ord('z') - ord(current)
    else:
        elevation_difference = ord(next) - ord(current)

    return elevation_difference <= 1

# Get the neighbors of a node
def get_neighbors(grid, x, y):
    neighbors = []
    if x > 0 and is_traversable(grid[y][x], grid[y][x - 1]):
        neighbors.append((x - 1, y))
    if x < len(grid[y]) - 1 and is_traversable(grid[y][x], grid[y][x + 1]):
        neighbors.append((x + 1, y))
    if y > 0 and is_traversable(grid[y][x], grid[y - 1][x]):
        neighbors.append((x, y - 1))
    if y < len(grid) - 1 and is_traversable(grid[y][x], grid[y + 1][x]):
        neighbors.append((x, y + 1))

    return neighbors

# Collect the distance from every node to the start
def get_distances(grid, start, end):
    distances = {start: 0}
    to_visit = [start]

    while to_visit:
        current = to_visit.pop(0)
        if current == end:
            break

        neighbors = get_neighbors(grid, *current)
        for neighbor in neighbors:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                to_visit.append(neighbor)
                continue
            if distances[neighbor] > distances[current] + 1:
                distances[neighbor] = distances[current] + 1
                to_visit.append(neighbor)
                continue
            dis_to_neighbor = distances[neighbor]
            dis_to_current = distances[current]
            next_el = grid[neighbor[1]][neighbor[0]]
            current_el = grid[current[1]][current[0]]
            if dis_to_neighbor < dis_to_current + 1 and abs(ord(next_el) - ord(current_el)) < 1:
                distances[current] = distances[neighbor] + 1

    return distances

def get_start_end(grid):
    start = None
    end = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start = (x, y)
            elif grid[y][x] == 'E':
                end = (x, y)
    return start, end

def locate_all_a(grid):
    a_locations = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'a':
                a_locations.append((x, y))
    return a_locations

def get_closest_a(grid):
    a_locations = locate_all_a(grid)
    closest_a = None
    closest_a_distance = None
    for a in a_locations:
        distances = get_distances(grid, a, end)
        distance_a_to_end = distances[end] if end in distances else 4000
        if closest_a is None:
            closest_a = a
            closest_a_distance = distance_a_to_end
        elif distance_a_to_end < closest_a_distance:
            closest_a = a
            closest_a_distance = distance_a_to_end
    return closest_a, closest_a_distance



start, end = get_start_end(input)
distances = get_distances(input, start, end)
distance_to_end = distances[end]
print("1:", distance_to_end)

closest_a, distance_to_a = get_closest_a(input)
print("2:", distance_to_a)



# Visualize the grid with colors
def visualize_colors(grid, distances):
    print('closest_a:', closest_a)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) == start:
                print('\033[1;32m', end='')
            elif (x, y) == end:
                print('\033[1;31m', end='')
            elif (x, y) == closest_a:
                print('\033[1;33m', end='')
            elif (x, y) in distances:
                print('\033[1;34m', end='')
            else:
                print('\033[1;37m', end='')
            print(grid[y][x], end='')
        print('\033[0m')
visualize_colors(input, distances)