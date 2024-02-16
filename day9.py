def read_input():
  with open('input9', 'r') as f:
    lines = f.readlines()

  sequences = list(map(lambda l: list(map(int, l.split())), lines))
  return sequences


def expand_sequence(sequence):
  result = []
  for i in range(1, len(sequence)):
    result.append(sequence[i] - sequence[i - 1])

  return result


def predict_last(sequence):
  if all(map(lambda n: n == 0, sequence)):
    return 0

  return sequence[-1] + predict_last(expand_sequence(sequence))


def predict_first(sequence):
  if all(map(lambda n: n == 0, sequence)):
    return 0

  return sequence[0] - predict_first(expand_sequence(sequence))



def solve():
  sequences = read_input()

  last = sum(map(predict_last, sequences))
  first = sum(map(predict_first, sequences))

  return last, first


if __name__ == '__main__':
  print(solve())
