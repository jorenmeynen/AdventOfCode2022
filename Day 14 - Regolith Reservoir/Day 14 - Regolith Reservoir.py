
grid_x = { 'min': None, 'max': None }
grid_y = { 'min': None, 'max': None }

def prepareInput():
    global grid_x
    global grid_y

    with open('./input.txt') as f:
        input = f.read().rstrip().split('\n')

    # Input contains a list of x,y elements like:
    # 495,144 -> 499,144
    # 492,40 -> 492,43 -> 484,43 -> 484,50 -> 499,50 -> 499,43 -> 496,43 -> 496,40
    # 499,13 -> 499,17 -> 497,17 -> 497,25 -> 505,25 -> 505,17 -> 502,17 -> 502,13

    # Create a list of all the lines from the points in the input
    line_groups = []
    for i in range(len(input)):
        points = input[i].split(' -> ')
        lines = []
        for point in points:
            x_val, y_val = [int(x) for x in point.split(',')]
            if grid_x['min'] == None or x_val < grid_x['min']:
                grid_x['min'] = x_val
            if grid_x['max'] == None or x_val > grid_x['max']:
                grid_x['max'] = x_val
            if grid_y['min'] == None or y_val < grid_y['min']:
                grid_y['min'] = y_val
            if grid_y['max'] == None or y_val > grid_y['max']:
                grid_y['max'] = y_val
            lines.append([x_val, y_val])
        line_groups.append(lines)

    # Add empty edges to the grid
    grid_x['min'] -= 200
    grid_x['max'] += 200
    grid_y['min'] = 0
    grid_y['max'] += 1

    # Draw the lines on a grid
    # # = line
    # . = empty

    grid = []
    for i in range(grid_y['min'], grid_y['max']+1):
        grid.append(['.'] * (grid_x['max']-grid_x['min']+1))

    for line_group in line_groups:
        for i in range(len(line_group)-1):
            x1, y1 = line_group[i]
            x2, y2 = line_group[i+1]
            # point 1 can be above or below point 2
            if y1 < y2:
                y_min = y1
                y_max = y2
            else:
                y_min = y2
                y_max = y1
            # point 1 can be left or right of point 2
            if x1 < x2:
                x_min = x1
                x_max = x2
            else:
                x_min = x2
                x_max = x1
            # Draw the line
            for y in range(y_min, y_max+1):
                for x in range(x_min, x_max+1):
                    grid[y-grid_y['min']][x-grid_x['min']] = '#'
                    # printGrid(grid)

    return grid

# Simulate sand falling
# If sand were to hit something other than air, it will try to spread down to the left, then down the right
# o = sand
def simulateSandDropped(grid, sand_start):
    x, y = sand_start
    if grid[y][x] == 'o':
        return (x, y)
    while y < len(grid):
        if grid[y][x] == '.':
            y += 1
        else:
            # Try to spread down to the left
            if grid[y][x-1] == '.':
                x -= 1
            # Try to spread down to the right
            elif grid[y][x+1] == '.':
                x += 1
            # If we can't spread down, we're done
            else:
                y -= 1
                break
        # printGridFraction(grid, (x, y))
    return (x, y)

def printGrid(grid):
    print()
    for row in grid:
        print(''.join(row))

def printGridFraction(grid, current_sand):
    print()
    x_min = max([current_sand[0] - 5, 0])
    x_max = min([current_sand[0] + 5, len(grid[0])-1])
    y_min = max([current_sand[1] - 5, 0])
    y_max = min([current_sand[1] + 5, len(grid)-1])


    for y in range(y_min, y_max+1):
        row = ''
        for x in range(x_min, x_max+1):
            if x == current_sand[0] and y == current_sand[1]:
                row += 'o'
            else:
                row += grid[y][x]
        print(row)


def prepareGridForPart2(grid):
    # grid.append(['.'] * len(grid[0]))
    grid.append(['#'] * len(grid[0]))
    return grid






from copy import deepcopy
grid_p1 = prepareInput()
grid_p2 = prepareGridForPart2(deepcopy(grid_p1))


sand_start = (500-grid_x['min'], 0)
voided = False
sand_count_p1 = 0
while not voided:
    x, y = simulateSandDropped(grid_p1, sand_start)
    if y >= len(grid_p1):
        voided = True
    else:
        grid_p1[y][x] = 'o'
        sand_count_p1 += 1

printGrid(grid_p1)
print("1:", sand_count_p1)

filled = False
sand_count_p2 = 0
while not filled:
    x, y = simulateSandDropped(grid_p2, sand_start)
    if y == 0:
        grid_p2[y][x] = 'o'
        sand_count_p2 += 1
        filled = True
    else:
        grid_p2[y][x] = 'o'
        sand_count_p2 += 1

printGrid(grid_p2)
print("2:", sand_count_p2)