from functools import cache

def read_input():
  with open('input12', 'r') as f:
    lines = f.readlines()

  rows = []
  for line in lines:
    record, groups = line.strip().split()
    groups = list(map(int, groups.split(',')))
    rows.append((record, groups))

  return rows


def compute_arrangements(row):
  record, groups = row
  print(record)

  @cache
  def next(idx, gid, gcnt, curr, prev):
    #b = b + curr
    if curr == '.':
      if prev == '#':
        if gcnt == groups[gid]:
          return aux(idx + 1, gid + 1, 0, curr)
        else:
          #print(b + ' FAIL')
          return 0
      return aux(idx + 1, gid, 0, curr)

    if curr == '#':
      if gid == len(groups) or gcnt == groups[gid]:
        #print(b + ' FAIL')
        return 0
      return aux(idx + 1, gid, gcnt + 1, curr)

  @cache
  def aux(idx, gid, gcnt, prev):
    if idx == len(record):
      if gid == len(groups) or (gid == len(groups) - 1 and gcnt == groups[gid]):
        #print(buffer)
        return 1
      else:
        #print(buffer + ' FAIL')
        return 0

    curr = record[idx]
    if curr != '?':
      return next(idx, gid, gcnt, curr, prev)
    else:
      if gid < len(groups):
        return next(idx, gid, gcnt, '#', prev) + next(idx, gid, gcnt, '.', prev)
      else:
        return next(idx, gid, gcnt, '.', prev)

  return aux(0, 0, 0, None)


def compute_arrangements_dp(row):
  record, group = row
  return 0


def solve1():
  rows = read_input()
  #return compute_arrangements(unroll(('?###????????', [3,2,1])))

  return sum(map(compute_arrangements, map(unroll, rows)))


def unroll(row):
  record, group = row
  return ('?'.join([record] * 5), group * 5)


def solve2():
  rows = list(map(unroll, read_input()))
  return sum(map(compute_arrangements_dp, rows))


if __name__ == '__main__':
  print(solve1())

