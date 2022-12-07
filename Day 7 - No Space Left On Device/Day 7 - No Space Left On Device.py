with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

file_system = current_directory = {}
directory = []

for line in input:
    line = line.split()

    # Command
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                directory.pop()
            elif line[2] == '/':
                directory = []
            else:
                directory.append(line[2])

    # Folder
    elif line[0] == 'dir':
        for i in directory:
            current_directory = current_directory[i]
        if current_directory.get(line[1]) is None:
            current_directory[line[1]] = {}
        current_directory = file_system

    # File
    else:
        for i in directory:
            current_directory = current_directory[i]
        current_directory[line[1]] = int(line[0])
        current_directory = file_system



# Part 1
sum_of_files_less_than_100000 = 0
def sum_directory_sizes(directory):
    global sum_of_files_less_than_100000
    current_directory_size = 0

    for key, value in directory.items():
        if type(value) is int:
            current_directory_size += value
        else:
            current_directory_size += sum_directory_sizes(value)

    if current_directory_size < 100_000:
        sum_of_files_less_than_100000 += current_directory_size

    return current_directory_size

root_directory_size = sum_directory_sizes(file_system)
print("1:", sum_of_files_less_than_100000)

# Part 2
directory_max = 70_000_000
update_size = 30_000_000
extra_space_required = root_directory_size - (directory_max - update_size)

smallest_directory = None
def find_smallest_directory(directory):
    global smallest_directory
    current_directory_size = 0

    for key, value in directory.items():
        if type(value) is int:
            current_directory_size += value
        else:
            current_directory_size += find_smallest_directory(value)

    if current_directory_size > extra_space_required:
        if smallest_directory is None:
            smallest_directory = current_directory_size
        else:
            smallest_directory = min(current_directory_size, smallest_directory)

    return current_directory_size


find_smallest_directory(file_system)
print("2:", smallest_directory)

