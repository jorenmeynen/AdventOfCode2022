with open('./input.txt') as f:
    input = f.read().rstrip()

groups = input.split('\n\n')
elves = [sum(map(int, elf.split('\n'))) for elf in groups]
elves.sort(reverse=True)

print("1:", elves[0])
print("2:", sum(elves[:3]))


# Original
# with open('./input.txt') as f:
#     input = f.read().splitlines()

# elves = []
# elf = 0
# for i in input:
#     if i == '':
#         elves.append(elf)
#         elf = 0
#     else:
#         elf += int(i)

# print("1:", elves[0])
# print("2:", sum(elves[:3]))