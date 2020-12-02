def part1():
  data = open('aoc2020/day1-input.txt').readlines()
  # print(data)

  for n1 in data:
    n1 = int(n1.strip())
    for n2 in data:
      n2 = int(n2.strip())
      if n1 + n2 == 2020:
        print(f"{n1} + {n2} = 2020")
        print(n1 * n2)

def part2():
  data = open('aoc2020/day1-input.txt').readlines()

  for n1 in data:
    n1 = int(n1.strip())
    for n2 in data:
      n2 = int(n2.strip())
      for n3 in data:
        n3 = int(n3.strip())
        if n1 + n2 + n3 == 2020:
          print(f"{n1} + {n2} + {n3} = 2020")
          print(n1 * n2 * n3)
