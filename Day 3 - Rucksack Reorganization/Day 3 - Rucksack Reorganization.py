with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

def find_priority(letter):
    if letter.islower():
        return ord(letter) - 96  # 1 to 26
    else:
        return ord(letter) - 38  # 27 to 52

# Part 1
found_letters_p1 = []
for i, text in enumerate(input):

    length = int(len(text)/2)
    half1 = text[:length]
    half2 = text[length:]

    common_item = [x for x in half1 if x in half2][0]
    found_letters_p1.append(common_item)


# Part 2
found_letters_p2 = []
group_size = int(len(input)/3)
for i in range(group_size):
    index = i*3
    text1 = input[index]
    text2 = input[index+1]
    text3 = input[index+2]
    for letter in text1:
        if letter in text2 and letter in text3:
            found_letters_p2.append(letter)
            break


print("1:", sum([find_priority(x) for x in found_letters_p1]))
print("2:", sum([find_priority(x) for x in found_letters_p2]))