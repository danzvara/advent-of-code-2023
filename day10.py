import math

def read_input():
  with open('input10', 'r') as f:
    grid = f.readlines()

  return list(map(lambda l: l.strip(), grid))


dirs = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
    }
pipes = {
    '|': ('N', 'S'),
    '-': ('W', 'E'),
    'J': ('N', 'W'),
    '7': ('W', 'S'),
    'F': ('E', 'S'),
    'L': ('N', 'E')
    }


def pipe_neighboars(pos, grid, pipe = None):
  if not pipe:
    pipe = grid[pos[0]][pos[1]]
  pipe_dir = pipes[pipe]

  dir0 = dirs[pipe_dir[0]]
  dir1 = dirs[pipe_dir[1]]

  pos0 = (pos[0] + dir0[0], pos[1] + dir0[1])
  pos1 = (pos[0] + dir1[0], pos[1] + dir1[1])

  return [pos0, pos1]


def fits(grid, pos2, pos1, pipe1 = None):
  return pos1 in pipe_neighboars(pos2, grid) and pos2 in pipe_neighboars(pos1, grid, pipe1)


def get_options(pos, grid):
  options = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  options = map(lambda o: (pos[0] + o[0], pos[1] + o[1]), options)
  options = filter(lambda o: (0 <= o[0] < len(grid)) and (0 <= o[1] < len(grid[1])), options)

  options = filter(lambda o: grid[o[0]][o[1]] != '.', options)

  return options

def move(grid, pos, prev_pos):
  options = get_options(pos, grid)

  for option in options:
    if option == prev_pos:
      continue
    if grid[option[0]][option[1]] == 'S':
      return option
    if fits(grid, option, pos):
      return option


def deduce_s_pipe(grid, pos):
  options = get_options(pos, grid)

  for pipe in pipes.keys():
    fitting_neighbours = list(filter(lambda o: fits(grid, o, pos, pipe), options))

    if len(fitting_neighbours) == 2:
      return pipe, fitting_neighbours


def solve1():
  grid = read_input()
  h, w = len(grid), len(grid[0])
  pos = None

  for i in range(h):
    for j in range(w):
      if grid[i][j] == 'S':
        pos = (i, j)
        break
    if pos:
      break

  s_pipe, neighbours = deduce_s_pipe(grid, pos)

  prev_pos = pos
  pos = neighbours[0]
  loop = [prev_pos, pos]

  while grid[pos[0]][pos[1]] != 'S':
    next_pos = move(grid, pos, prev_pos)

    prev_pos = pos
    pos = next_pos

    loop.append(pos)

  area = 0
  for i in range(1, len(loop)):
    area += (loop[i][1] - loop[i - 1][1]) * (loop[i][0] + loop[i - 1][0])
  area = area / 2

  i = math.floor(area - len(loop) / 2)

  return math.ceil(len(loop) / 2), i


if __name__ == '__main__':
  print(solve1())
