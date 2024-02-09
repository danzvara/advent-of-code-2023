def read_input():
  with open('input3') as f:
    return f.readlines()


def is_digit(c):
  return 9 >= ord(c) - ord('0') >= 0


def is_symbol(c):
  #return not is_digit(c) and c != '.'
  return c == '*'


def solve1(input_lines):
  partno_sum = 0
  i, j = 0, 0

  while i < len(input_lines):
    while j < len(input_lines[0]):
      if not is_digit(input_lines[i][j]):
        j += 1
        continue

      k = j + 1
      while k < len(input_lines[0]) and is_digit(input_lines[i][k]):
        k += 1

      window = input_lines[i][max(0, j - 1) : min(len(input_lines[0]), k + 1)].strip()
      if i > 0:
        window += input_lines[i - 1][max(0, j - 1) : min(len(input_lines[0]), k + 1)].strip()
      if i < len(input_lines) - 1:
        window += input_lines[i + 1][max(0, j - 1) : min(len(input_lines[0]), k + 1)].strip()

      window_has_character = False
      for c in window:
        if is_symbol(c):
          window_has_character = True
          break

      if window_has_character:
        partno_sum += int(input_lines[i][j:k])

      j = k

    j = 0
    i += 1

  return partno_sum


def solve2(input_lines):
  def is_inbounds(i, j):
    return i >= 0 and i < len(input_lines) and j >= 0 and j < len(input_lines[0])


  def expand_number(i, j):
    a, b = j - 1, j + 1
    number = input_lines[i][j]

    while a >= 0 and is_digit(input_lines[i][a]):
      number = input_lines[i][a] + number
      a -= 1

    while b < len(input_lines[0]) and is_digit(input_lines[i][b]):
      number = number + input_lines[i][b]
      b += 1

    return int(number)


  gear_sum = 0
  i, j = 0, 0

  while is_inbounds(i, 0):
    while is_inbounds(0, j):
      c = input_lines[i][j]
      if not is_symbol(c):
        j += 1
        continue


      numbers_around = []
      m = max(0, i - 1)
      n = max(0, j - 1)
      while is_inbounds(m, n) and m < i + 2:
        while is_inbounds(m, n) and n < j + 2:
          if is_digit(input_lines[m][n]):
            number = expand_number(m, n)
            numbers_around.append(number)

            if n == j - 1 and not is_digit(input_lines[m][n + 1]):
              n += 1
            else:
              break
          else:
            n += 1
        m += 1
        n = j - 1

      if len(numbers_around) == 2:
        gear_sum += numbers_around[0] * numbers_around[1]
        window = input_lines[i][max(0, j - 1) : min(len(input_lines[0]), j + 2)].strip()
        #if i > 0:
        #  window = input_lines[i - 1][max(0, j - 1) : min(len(input_lines[0]), j+ 2)].strip() + '\n' + window
        #if i < len(input_lines) - 1:
        #  window += '\n' + input_lines[i + 1][max(0, j - 1) : min(len(input_lines[0]), j + 2)].strip()

        print(window)
        print(numbers_around)

      j += 1
    i += 1
    j = 0

  return gear_sum

if __name__ == '__main__':
  test_input = '''467..114..
...*......
....2.633.
......#...
617*......
.....+.58.
..592.....
......755.
...$......
.664.598..'''.split()
  print(solve1(read_input()))
  print(solve2(read_input()))

