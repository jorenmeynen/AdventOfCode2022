with open('./input.txt') as f:
    forest = f.read().rstrip().split('\n')

def checkTreeHidden(x, y):
    global forest

    # Forest edges are always visible
    if x == 0 or y == 0:
        return True
    if x == len(forest[y]) - 1 or y == len(forest) - 1:
        return True
    
    # The forest is square grid of positive integers, representing the height of the trees
    # Check if there is are higher trees in every direction
    # If there is, the tree is not visible
    # If there is not, the tree is visible

    is_hidden_left = False
    is_hidden_right = False
    is_hidden_up = False
    is_hidden_down = False

    current_tree_height = forest[y][x]

    # Check if there is a higher tree to the left
    for i in range(x):
        height_of_tree = forest[y][i]
        if height_of_tree >= current_tree_height:
            is_hidden_left = True

    # Check if there is a higher tree to the right
    for i in range(x + 1, len(forest[y])):
        height_of_tree = forest[y][i]
        if height_of_tree >= current_tree_height:
            is_hidden_right = True
            
    # Check if there is a higher tree above
    for i in range(y):
        height_of_tree = forest[i][x]
        if height_of_tree >= current_tree_height:
            is_hidden_up = True

    # Check if there is a higher tree below
    for i in range(y + 1, len(forest)):
        height_of_tree = forest[i][x]
        if height_of_tree >= current_tree_height:
            is_hidden_down = True

    is_tree_visible = not (is_hidden_left and is_hidden_right and is_hidden_up and is_hidden_down)
    return is_tree_visible


def findScenicScoreTree(x, y):
    global forest
    
    if x == 0 or y == 0:
        return 0
    if x == len(forest[y]) - 1 or y == len(forest) - 1:
        return 0

    # The forest is square grid of positive integers, representing the height of the trees
    # The scenic score of a tree is the multiplication of the distance to the nearest tree that is of the same height or higher in every direction

    scenic_score_directions = []
    current_tree_height = forest[y][x]

    # Find the distance to the nearest tree to the left
    distance = 0
    for i in range(1, x+1):
        height_of_tree = forest[y][x-i]
        distance += 1
        if height_of_tree >= current_tree_height:
            break
    scenic_score_directions.append(distance)
    
    # Find the distance to the nearest tree to the right
    distance = 0
    for i in range(x + 1, len(forest[y])):
        height_of_tree = forest[y][i]
        distance += 1
        if height_of_tree >= current_tree_height:
            break
    scenic_score_directions.append(distance)

    # Find the distance to the nearest tree above
    distance = 0
    for i in range(1, y+1):
        height_of_tree = forest[y-i][x]
        distance += 1
        if height_of_tree >= current_tree_height:
            break
    scenic_score_directions.append(distance)

    # Find the distance to the nearest tree below
    distance = 0
    for i in range(y + 1, len(forest)):
        height_of_tree = forest[i][x]
        distance += 1
        if height_of_tree >= current_tree_height:
            break
    scenic_score_directions.append(distance)

    scenic_score = 1
    for score in scenic_score_directions:
        scenic_score *= score
    
    return scenic_score


trees_not_hidden = 0
scenic_scores = []
for y in range(len(forest)):
    for x in range(len(forest[y])):
        trees_not_hidden += checkTreeHidden(x, y)
        scenic_scores.append(findScenicScoreTree(x, y))

print("1:", trees_not_hidden)
print("2:", max(scenic_scores))
