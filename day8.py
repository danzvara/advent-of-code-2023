import re
import math

def read_input():
  with open('input8', 'r') as f:
    lines = f.readlines()

  instructions = lines[0].strip()
  network_lines = lines[2:]

  network = {}
  for line in network_lines:
    source, dest = line.strip().replace(' ', '').split('=')
    dest = re.sub(r'[\(\)\s]', '', dest).split(',')

    network[source] = dest

  return instructions, network


def solve1():
  instructions, network = read_input()

  steps = 0

  loc = 'AAA'

  while loc != 'ZZZ':
    i = instructions[steps % len(instructions)]
    loc = network[loc][1 if i == 'R' else 0]
    steps += 1

  return steps


def done(locs, first_z):
  return all(map(lambda l: l.endswith('Z'), locs))


def done2(first_z):
  return all(map(lambda n: n > 0, first_z))


def solve2():
  instructions, network = read_input()

  steps = 0

  locs = []

  for loc in network.keys():
    if loc.endswith('A'):
      locs.append(loc)

  first_z = [-1 for _ in range(len(locs))]

  while not done2(first_z):
    i = instructions[steps % len(instructions)]
    new_locs = []

    steps += 1

    for idx in range(len(locs)):
      new_loc = network[locs[idx]][1 if i == 'R' else 0]
      new_locs.append(new_loc)

      if new_loc.endswith('Z') and steps % len(instructions) == 0 and first_z[idx] < 0:
        first_z[idx] = steps

    locs = new_locs


  return math.lcm(*first_z)


if __name__ == '__main__':
  print(solve1())
  print(solve2())

