def part1():
  valid_passwords = 0
  data = open('aoc2020/day2-input.txt').readlines()

  for line in data:
    fields = line.strip().split(' ')
    min, max = fields[0].split('-')
    min, max = int(min), int(max)
    letter = fields[1][0]
    pwd = fields[2]
    # print(line)
    # print(f"min={min}, max={max}, letter={letter}, pwd={pwd}")

    count = pwd.count(letter)
    if count >= min and count <= max:
      valid_passwords += 1

  print(f"Valid passwords: {valid_passwords}")

def part2():
  valid_passwords = 0
  data = open('aoc2020/day2-input.txt').readlines()
  
  for line in data:
    fields = line.strip().split(' ')
    p1, p2 = fields[0].split('-')
    p1, p2 = int(p1) - 1, int(p2) - 1 # input positions are 1-based
    letter = fields[1][0]
    pwd = fields[2]

    if pwd[p1] == letter and pwd[p2] != letter:
      valid_passwords += 1
    elif pwd[p1] != letter and pwd[p2] == letter:
      valid_passwords += 1

  print(f"Valid passwords: {valid_passwords}")
