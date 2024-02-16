from functools import cmp_to_key

def read_input():
  with open('input7') as f:
    lines = f.readlines()

  hands = []
  for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    hands.append((hand, bid))

  return hands


labels = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
labels_with_joker = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6',
                                   '5', '4', '3', '2', 'J']))

kinds = list(reversed(['5', '41', '32', '311', '221', '2111', '11111']))


def get_kind(hand):
  type_to_quantity = {}
  for card in hand:
    if card in type_to_quantity:
      type_to_quantity[card] += 1
    else:
      type_to_quantity[card] = 1

  if 'J' in type_to_quantity:
    joker_cnt = type_to_quantity['J']
    del type_to_quantity['J']
    if not type_to_quantity:
      type_to_quantity['A'] = 5
    else:
      max_label = max(type_to_quantity.items(), key=lambda i: i[1])
      type_to_quantity[max_label[0]] += joker_cnt

  counts = list(reversed(sorted(type_to_quantity.values())))
  quantified_hand = ''
  for count in counts:
    quantified_hand += str(count)

  kind = kinds.index(quantified_hand)
  return kind


def compare(labels, hand_bid_1, hand_bid_2):
  hand1 = hand_bid_1[0]
  hand2 = hand_bid_2[0]

  kind1 = get_kind(hand1)
  kind2 = get_kind(hand2)

  if kind1 > kind2:
    return 1
  elif kind1 < kind2:
    return -1
  else:
    for c1, c2 in zip(hand1, hand2):
      if labels.index(c1) > labels.index(c2):
        return 1
      elif labels.index(c1) < labels.index(c2):
        return -1

  raise Exception(f"Equal hands {hand1} {hand2}")



def solve1(hands):
  sorted_hands = sorted(hands, key=cmp_to_key(lambda a, b: compare(labels, a, b)))
  winnings = 0

  for idx in range(len(sorted_hands)):
    winnings += sorted_hands[idx][1] * (idx + 1)

  return winnings


def solve2(hands):
  sorted_hands = sorted(hands, key=cmp_to_key(lambda a, b: compare(labels_with_joker, a, b)))
  winnings = 0

  for idx in range(len(sorted_hands)):
    winnings += sorted_hands[idx][1] * (idx + 1)

  return winnings


if __name__ == '__main__':
  print(solve1(read_input()))
  print(solve2(read_input()))
