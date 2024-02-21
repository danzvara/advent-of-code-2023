def read_input():
  with open('input11', 'r') as f:
    lines = f.readlines()

  return list(map(lambda l: l.strip(), lines))


def solve(n = 2):
  grid = read_input()

  empty_cols = []
  for j in range(len(grid[0])):
    empty = True
    for i in range(len(grid)):
      empty = empty and grid[i][j] == '.'
    if empty:
      empty_cols.append(j)

  empty_rows = []
  for idx, line in enumerate(grid):
    if all(map(lambda c: c == '.', line)):
      empty_rows.append(idx)

  galaxies = []
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '#':
        galaxies.append((i, j))

  path_sum = 0

  for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
      g1, g2 = galaxies[i], galaxies[j]
      dist = (max(g1[1], g2[1]) - min(g1[1], g2[1])) + (max(g1[0], g2[0]) - min(g1[0], g2[0]))

      for c in empty_cols:
        if min(g1[1], g2[1]) < c < max(g1[1], g2[1]):
          dist += n - 1

      for r in empty_rows:
        if min(g1[0], g2[0]) < r < max(g1[0], g2[0]):
          dist += n - 1

      path_sum += dist

  return path_sum


if __name__ == '__main__':
  print(solve(2))
  print(solve(1000000))
