def load_data():
  data = open('aoc2021/day1-input.txt').readlines()
  data = [ int(d.strip()) for d in data ]
  return data

def part1():
  data = load_data()

  prev_depth = data[0]
  count = 0
  for depth in data[1:]:
    if depth > prev_depth:
      count += 1
    prev_depth = depth

  print(f"Number of increases: {count}")

def part2():
  data = load_data
  
  count = 0
  prev_window = data[0:3]
  prev_total = sum(prev_window)
  for depth in data[3:]:
    window = prev_window[1:3] + [depth]
    total = sum(window)
    if total > prev_total:
      count += 1
    prev_total = total

