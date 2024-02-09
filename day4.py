def read_input():
  with open('input4') as f:
    return f.readlines()


def get_card_matches(card):
  [w, c] = card.split(':')[1].split('|')
  winning = w.split()
  numbers = c.split()

  w_cnt = 0
  for n in numbers:
    if n in winning:
      w_cnt += 1 

  return w_cnt


def solve1(pile):
  value = 0
  for card in pile:
    w_cnt = get_card_matches(card)
    value += 2 ** (w_cnt - 1) if w_cnt > 0 else 0

  return value


def solve2(pile):
  hand = {}
  matches = {}
  count = len(pile)
  for i in range(len(pile)):
    hand[i] = 1

  for i in range(len(pile)):
    while hand[i] > 0:
      n_matches = get_card_matches(pile[i]) if i not in matches else matches[i]
      matches[i] = n_matches

      for j in range(n_matches):
        hand[i + j + 1] += 1
      count += n_matches

      hand[i] -= 1

  return count


if __name__ == '__main__':
  pile = read_input()

  print(solve1(pile))
  print(solve2(pile))
