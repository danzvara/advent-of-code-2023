def read_input():
  with open('input5') as f:
    data = f.readlines()

  seeds = list(map(int, data[0].split(':')[1].split()))

  maps = {}
  current_map_name = ''
  for line in data[1:]:
    if line and line != '\n' and 'map' in line:
      current_map_name = line.split()[0]
      maps[current_map_name] = []
    elif line and line != '\n':
      map_line = list(map(int, line.split()))
      maps[current_map_name].append(map_line)

  return seeds, maps


def src_to_dest(x, maps):
  for map_range in maps:
    dest, src, length = map_range

    dist = x - src
    if dist >= 0 and dist < length:
      return dest + dist

  return x


def solve1(seeds, maps):
  locs = seeds
  for current_map in maps.values():
    locs = list(map(lambda x: src_to_dest(x, current_map), locs))

  return min(locs)


def get_new_range(rng, maps):
  for map_range in maps:
    t, s, l = map_range
    r, rl = rng
    d = r - s

    is_overlap = r + rl > s and r < s + l
    if is_overlap:
      overlap_start = max(r, s)
      overlap_end = min(r + rl, s + l)
      overlap_len = overlap_end - overlap_start

      leftovers = []
      if r < s:
        leftovers.append((r, s - r))
      if r + rl > s + l:
        leftovers.append((s + l, r + rl - s - l))
      return (t + (overlap_start - s), overlap_len), leftovers

  return rng, []


def solve2(seeds, maps):
  ranges = []
  for i in range(0, len(seeds), 2):
    ranges.append((seeds[i], seeds[i + 1]))

  for current_map in maps.values():
    new_ranges = []
    while len(ranges) > 0:
      r = ranges[0]
      new_r, leftovers = get_new_range(r, current_map)
      new_ranges.append(new_r)
      ranges = ranges[1:] + leftovers

    ranges = new_ranges

  return min(ranges)[0]

if __name__ == '__main__':
  seeds, maps = read_input()
  print(solve1(seeds, maps))
  print(solve2(seeds, maps))

