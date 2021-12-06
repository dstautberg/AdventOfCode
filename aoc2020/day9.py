def load_file():
  data = open('aoc2020/day9-input.txt').readlines()
  data = [ int(d.strip()) for d in data ]
  return data

def part1():
  data = load_file()

  preamble_length = 25
  previous_count = 25

  preamble = data[0:preamble_length]
  print(f"Preamble: {preamble}")

  for n in range(preamble_length, len(data)):
    match = False

    for n1 in range(n-previous_count, n):
      for n2 in range(n-previous_count, n):
        if n1 == n2:
          pass
          # print("Skip: same number")
        else:
          # print(f"{data[n]} == {data[n1]} + {data[n2]}")
          if data[n1] + data[n2] == data[n]:
            match = True
        
    if not match:
      print(f"Bad number: {data[n]}")
      break

def part2():
  invalid_number = 542529149 # answer from part 1
  data = load_file()

  for n1 in range(len(data)):
    for n2 in range(n1+1, len(data)):
      sum = 0
      for n in range(n1, n2+1): sum += data[n]
      if sum == invalid_number:
        list = data[n1:n2+1]
        m1, m2 = min(list), max(list)
        print(f"{m1} + {m2} = {m1+m2}")
        return
      elif sum > invalid_number:
        break
