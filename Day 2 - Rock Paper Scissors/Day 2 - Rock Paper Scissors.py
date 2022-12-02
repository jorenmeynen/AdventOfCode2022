with open('./input.txt') as f:
    input = f.read().rstrip().split('\n')

def get_result_round_p1(hand1, hand2):
    result = (ord(hand1) - ord(hand2)) % 3
    if result == 0:
        return 'win'
    elif result == 1:
        return 'draw'
    else:
        return 'loss'

def get_hand_to_throw_p2(hand1, result):
    if result == 'win':
        offset_hand_to_throw = (ord(hand1) - 1) % 3
    elif result == 'draw':
        offset_hand_to_throw = (ord(hand1) - 2) % 3
    else:
        offset_hand_to_throw = (ord(hand1) - 3) % 3
    return chr(offset_hand_to_throw + ord('X'))

score_hand = {'X': 1, 'Y': 2, 'Z': 3}
score_round = {'win': 6, 'draw': 3, 'loss': 0}
action = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}

total_score_part_1 = []
total_score_part_2 = []
for line in input:
    i1, i2 = line.split(' ')

    round_result_p1 = get_result_round_p1(i1, i2)
    score_p1 = score_round[round_result_p1] + score_hand[i2]
    total_score_part_1.append(score_p1)

    hand_to_throw_p2 = get_hand_to_throw_p2(i1, action[i2])
    score_p2 = score_round[action[i2]] + score_hand[hand_to_throw_p2]
    total_score_part_2.append(score_p2)

print(sum(total_score_part_1))
print(sum(total_score_part_2))