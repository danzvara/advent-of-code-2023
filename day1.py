def read_input(input_name):
  with open(input_name, 'r') as f:
    return f.readlines()


def is_int(c):
  return abs(ord(c) - ord('0')) <= 9


def get_calibration_value(line):
  numbers_in_line = list(filter(lambda x: is_int(x), line))
  return int(numbers_in_line[0] + numbers_in_line[-1])


def get_calibration_value_with_words(line):
  words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

  numbers = ''
  for idx in range(len(line)):
    if is_int(line[idx]):
      numbers += line[idx]
    else:
      for w in words:
        if line[idx:].startswith(w):
          numbers += (str(words.index(w) + 1))
          break

  return int(numbers[0] + numbers[-1])



def solve1(input_lines):
  return sum(map(get_calibration_value, input_lines))


def solve2(input_lines):
  return sum(map(get_calibration_value_with_words, input_lines))


if __name__ == '__main__':
  input_lines = read_input('input1')

  print(solve1(input_lines))
  print(solve2(input_lines))
