maxims = { 'red': 12,
            'green': 13,
            'blue': 14 }


def read_input(input_name):
  with open(input_name, 'r') as f:
    return f.readlines()


def solve1(input_lines):
  id_sum = 0
  for line in input_lines:
    [name, game] = line.split(':')
    game_id = int(name.split()[1])
    turns = game.split(';')
    is_valid = True

    for turn in turns:
      colors = turn.split(',')
      for color_count in colors:
        [count, color] = color_count.strip().split()
        if int(count) > maxims[color]:
          is_valid = False
          break

      if not is_valid:
        break

    if is_valid:
      id_sum += game_id

  return id_sum


def solve2(input_lines):
  power_sum = 0
  for line in input_lines:
    minimums = { }
    [name, game] = line.split(':')
    game_id = int(name.split()[1])
    turns = game.split(';')
    print(line)
    for turn in turns:
      colors = turn.split(',')
      for color_count in colors:
        [count, color] = color_count.strip().split()
        if color not in minimums:
          minimums[color] = int(count)
        else:
          minimums[color] = max(minimums[color], int(count))

    print(minimums)
    power_sum += minimums['red'] * minimums['blue'] * minimums['green']

  return power_sum

if __name__ == '__main__':
  input_lines = read_input('input2')
  print(solve2(input_lines))
