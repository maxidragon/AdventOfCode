cards_by_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4','3', '2']
types_by_strength = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card']
card_strength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
hands = []
def determine_hand_type(cards):
    count = {}
    for card in cards:
        if card[0] in count:
            count[card[0]] += 1
        else:
            count[card[0]] = 1        
    if 5 in count.values():
        return 'Five of a kind'
    elif 4 in count.values():
        return 'Four of a kind'
    elif 3 in count.values() and 2 in count.values():
        return 'Full house'
    elif 3 in count.values():
        return 'Three of a kind'
    elif list(count.values()).count(2) == 2:
        return 'Two pair'
    elif 2 in count.values():
        return 'One pair'
    else:
        return 'High card'
    
def determine_rank(cards1, cards2):
    for i in range(0, 5):
        if card_strength[cards1[i][0]] > card_strength[cards2[i][0]]:
            return 1
        elif card_strength[cards1[i][0]] < card_strength[cards2[i][0]]:
            return 2 
    

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        hands.append({
            'cards': line[0],
            'bid': int(line[1]),
            'type': determine_hand_type(line[0])
        })

hands = sorted(hands, key=lambda k: (types_by_strength.index(k['type']), card_strength[k['cards'][0]]), reverse=True)
rank = 1
for i in range(0, len(hands) - 1):
    try:
        key = hands[i]['rank']
    except KeyError:
        if hands[i]['type'] == hands[i + 1]['type']:
            rank_compare = determine_rank(hands[i]['cards'], hands[i + 1]['cards'])
            if rank_compare == 1:
                hands[i]['rank'] = rank + 1
                hands[i + 1]['rank'] = rank 
            else:
                hands[i]['rank'] = rank
                hands[i + 1]['rank'] = rank + 1
            rank += 2
        else:
            hands[i]['rank'] = rank
            rank += 1
    else:
        continue

try:
    key = hands[-1]['rank']
except:
    hands[-1]['rank'] = len(hands)
    
sum = 0
for hand in hands:
    sum += hand['rank'] * hand['bid']   

print(sum)