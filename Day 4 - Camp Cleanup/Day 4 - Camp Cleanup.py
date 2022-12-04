with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

overlap_counter_p1 = 0
overlap_counter_p2 = 0
for pair in input:
    elf1, elf2 = pair.split(',')
    elf1 = [int(x) for x in elf1.split('-')]
    elf2 = [int(x) for x in elf2.split('-')]

    if (
        elf1[0] <= elf2[0] and elf1[1] >= elf2[1]
    ) or (
        elf1[0] >= elf2[0] and elf1[1] <= elf2[1]
    ):
        overlap_counter_p1 += 1
        overlap_counter_p2 += 1
        continue

    if (
        elf1[0] <= elf2[0] and elf1[1] >= elf2[0]
    ) or (
        elf1[0] <= elf2[1] and elf1[1] >= elf2[1]
    ):
        overlap_counter_p2 += 1

print("1:", overlap_counter_p1)
print("2:", overlap_counter_p2)
