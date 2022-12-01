# %%
with open('./input.txt') as f:
    input = f.read().splitlines()

# %%
elves = []
elf = 0
for i in input:
    if i == '':
        elves.append(elf)
        elf = 0
    else:
        elf += int(i)

# %%
elves.sort(reverse=True)
print("1:", elves[0])
print("2:", sum(elves[:3]))