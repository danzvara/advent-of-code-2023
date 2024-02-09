def read_input1():
  with open('input6') as f:
    data = f.readlines()

  times = list(map(int, data[0].split(':')[1].split()))
  distances = list(map(int, data[1].split(':')[1].split()))

  return times, distances


def read_input2():
  with open('input6') as f:
    data = f.readlines()

  t = int(data[0].split(':')[1].replace(' ', ''))
  d = int(data[1].split(':')[1].replace(' ', ''))

  return t, d


def solve1(t, d):
  result = 1
  for i in range(len(t)):
    winning_distances = list(filter(lambda x: x > d[i], [j * (t[i] - j) for j in
                                                         range(1, t[i])]))
    result *= len(winning_distances)
  return result


def solve2(t, d):
  winning_distances = list(filter(lambda x: x > d, [j * (t - j) for j in range(1, t)]))
  return len(winning_distances)


if __name__ == '__main__':
  t, d = read_input1()
  print(solve1(t, d))

  t, d = read_input2()
  print(solve2(t, d))
