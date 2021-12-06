def part1():
  data = open('aoc2020/day3-input.txt').readlines()
  data = [ row.strip() for row in data ]
  # print(data[0])
  # print(len(data[0]), len(data))
  x, y = 3, 1
  trees = 0

  while y < len(data):
    x = x % len(data[y])
    if data[y][x] == '#':
      trees += 1
    x += 3
    y += 1

  print(f"Trees: {trees}")

def count_trees(data, slope_x, slope_y):
  trees = 0
  x, y = slope_x, slope_y
  while y < len(data):
    x = x % len(data[y])
    if data[y][x] == '#':
      trees += 1
    x += slope_x
    y += slope_y
  return trees

def part2():
  data = open('aoc2020/day3-input.txt').readlines()
  data = [ row.strip() for row in data ]

  c1 = count_trees(data, 1, 1)
  print(c1)
  c2 = count_trees(data, 3, 1)
  print(c2)
  c3 = count_trees(data, 5, 1)
  print(c3)
  c4 = count_trees(data, 7, 1)
  print(c4)
  c5 = count_trees(data, 1, 2)
  print(c5)

  print(c1*c2*c3*c4*c5)
  