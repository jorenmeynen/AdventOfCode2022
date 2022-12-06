with open('./input.txt') as f:
    input = f.read().rstrip()

for i in range(len(input)-4):
    test = input[i:i+4]
    package_marker = list(set(test))
    if len(package_marker) == 4:
        print("1:", i + 4)
        break

for i in range(len(input)-14):
    test = input[i:i+14]
    message_marker = list(set(test))
    if len(message_marker) == 14:
        print("2:", i+14)
        break
    
