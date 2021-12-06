def load_data():
  data = open('aoc2020/day10-input-simple2.txt').readlines()
  data = [ int(d.strip()) for d in data ]
  return data

def part1():
  data = load_data()
  max_joltage = max(data)
  joltage = 0
  adapters = []
  one_jolt_differences, three_jolt_differences = 0, 0
  while joltage < max_joltage:
    matches = [ j for j in data if j > joltage and j <= joltage + 3 ]
    matches.sort()
    print(f"joltage: {joltage}, matches: {matches}")
    for m in matches:
      if m - joltage == 1: one_jolt_differences += 1
      if m - joltage == 3: three_jolt_differences += 1
      adapters.append(m)
      joltage = m
  
  three_jolt_differences += 1 # last adapter to phone is a 3 jolt increase 
  print(f"adapters: {adapters}")
  print(f"one_jolt_differences: {one_jolt_differences}, three_jolt_differences: {three_jolt_differences}, result: {one_jolt_differences * three_jolt_differences}")

def recurse(data, adapters, max_joltage, joltage, permutations):
  print(f"recurse, permutations: {permutations}, joltage: {joltage}, adapters: {adapters}")
  while joltage < max_joltage:
    matches = [ j for j in data if j > joltage and j <= joltage + 3 ]
    matches.sort()
    if len(matches) == 1:
      adapters.append(matches[0])
      joltage = matches[0]
      print(f"one match, adapters: {adapters}")
    elif len(matches) == 2:
      a1 = adapters.copy()
      a1.append(matches[0])
      a1.append(matches[1])
      recurse(data, a1, max_joltage, matches[1], permutations)
      a2 = adapters.copy()
      a2.append(matches[1])
      recurse(data, a2, max_joltage, matches[1], permutations)
      joltage = matches[1]
      permutations += 2
    elif len(matches) == 3:
      a1 = adapters.copy()
      a1.append(matches[0])
      a1.append(matches[1])
      a1.append(matches[2])
      recurse(data, a1, max_joltage, matches[2], permutations)
      a2 = adapters.copy()
      a2.append(matches[0])
      a2.append(matches[2])
      recurse(data, a2, max_joltage, matches[2], permutations)
      a3 = adapters.copy()
      a3.append(matches[1])
      a3.append(matches[2])
      recurse(data, a3, max_joltage, matches[2], permutations)
      a4 = adapters.copy()
      a4.append(matches[2])
      recurse(data, a4, max_joltage, matches[2], permutations)
      joltage = matches[2]
      permutations += 4

      # for m in matches:
      #   a = adapters.copy()
      #   a.append(m)
      #   print(f"recursing: permutations: {permutations+1}, adapters: {a}")
      #   permutations = recurse(data, a, max_joltage, m, permutations + 1)
      #   adapters.append(m)
      #   joltage = m

  return permutations 

def part2():
  print("part2")
  data = load_data()
  max_joltage = max(data)
  joltage = 0
  adapters = []
  permutations = 1

  permutations = recurse(data, adapters, max_joltage, joltage, permutations)

  print(f"permutations: {permutations}")
  # Getting 263538, answer should be 19208
  # Trying to figure out how to debug this
