with open("./input.txt") as f:
    jet_pattern = f.read().rstrip()

with open("./shapes.txt") as f:
    shapes = f.read().rstrip().split("\n\n")

def prepareShapes(shapes):
    prepared_shapes = []
    for shape in shapes:
        lines = shape.split("\n")
        prepared_shape = []
        for line in lines:
            prepared_line = []
            for char in line:
                prepared_line.append(char)
            prepared_shape.append(prepared_line)
        prepared_shapes.append(prepared_shape)
    return prepared_shapes

def isShapeTouchingGround(pos_in_grid, shape, grid):
    # Check if the shape is touching the ground
    # If the shape is touching the ground, return True
    # If the shape is not touching the ground, return False
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == "#":
                row = pos_in_grid[0] + i
                col = pos_in_grid[1] + j
                if row >= len(grid):
                    return True
                if grid[row][col] == "#":
                    return True
    return False

def addShapeToGrid(pos_in_grid, shape, grid):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == "#":
                row = pos_in_grid[0] + i
                col = pos_in_grid[1] + j
                grid[row][col] = "#"

def getFirstNonEmptyRow(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                return i
    return len(grid)

def insertOrRemoveRowsFromGrid(grid, shape):
    first_non_empty_row = getFirstNonEmptyRow(grid)

    # Insert or Remove a row to the grid until the new shape has 3 empty rows below it
    required_empty_rows = 3 + len(shape)
    new_rows = required_empty_rows - first_non_empty_row

    if new_rows > 0:
        for i in range(new_rows):
            grid.insert(0, ["."] * len(grid[0]))
    elif new_rows < 0:
        for i in range(abs(new_rows)):
            del grid[0]



def printGridWithShape(pos_in_grid, shape, grid):
    shape_height = len(shape)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i >= pos_in_grid[0] and i < pos_in_grid[0] + shape_height:
                if j >= pos_in_grid[1] and j < pos_in_grid[1] + len(shape[0]):
                    print(shape[i - pos_in_grid[0]][j - pos_in_grid[1]], end="")
                else:
                    print(grid[i][j], end="")
            else:
                print(grid[i][j], end="")
            
        print("")
    print("")


def getHeight(jet_pattern, shapes, total_rocks):
    grid = [["."] * 7 for i in range(4)]
    turn = 0
    shape_i = 0
    pos_in_grid = [-1, 2]
    rocks = 0

    # Drop the shape akin to tetris
    # Every turn, move the shape down,
    # then depending on the jet pattern, move the shape left or right.
    # Until the shape hits the bottom or another shape, then add it to the grid

    # Start the shape 2 units away from the left edge
    while rocks < total_rocks:
        shape = shapes[shape_i]

        # Move the shape down
        pos_in_grid[0] += 1

        # Check if the shape is touching the ground
        if isShapeTouchingGround(pos_in_grid, shape, grid):
            pos_in_grid[0] -= 1
            addShapeToGrid(pos_in_grid, shape, grid)

            shape_i += 1
            if shape_i >= len(shapes):
                shape_i = 0
            pos_in_grid = [-1, 2]
            insertOrRemoveRowsFromGrid(grid, shapes[shape_i])
            rocks += 1

        else:
            # printGridWithShape(pos_in_grid, shape, grid)
            # Move the shape left or right
            index = turn % len(jet_pattern)
            if jet_pattern[index] == "<" and pos_in_grid[1] > 0:
                pos_in_grid[1] -= 1
                if isShapeTouchingGround(pos_in_grid, shape, grid):
                    pos_in_grid[1] += 1
            elif jet_pattern[index] == ">" and pos_in_grid[1] < len(grid[0]) - len(shape[0]):
                pos_in_grid[1] += 1
                if isShapeTouchingGround(pos_in_grid, shape, grid):
                    pos_in_grid[1] -= 1
            turn += 1
            # printGridWithShape(pos_in_grid, shape, grid)

    return len(grid) - getFirstNonEmptyRow(grid)
    




shapes = prepareShapes(shapes)
part_1 = getHeight(jet_pattern, shapes, 2022)
print("1:", part_1)
# part_2 = getHeight(jet_pattern, shapes, 1_000_000_000_000)
# print("2:", part_2)