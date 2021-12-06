data = open('aoc2020/day6-input.txt').readlines()
data = [ d.strip() for d in data ]

def part1():
  group_yes = {}
  total_yes_count = 0
  for row in data:
    if len(row) == 0: # end of group
      # print(f"group_yes.keys() = {group_yes.keys()}")
      total_yes_count += len(group_yes.keys())
      group_yes = {}
      next
    for c in row:
      group_yes[c] = 1

  # Last group doesn't have a trailing blank line
  # print(f"group_yes.keys() = {group_yes.keys()}")
  total_yes_count += len(group_yes.keys())

  print(f"Total: {total_yes_count}")

class Counter(dict):
  def __missing__(self, key):
    return 0

def part2():
  group_size = 0
  group_yes_counts = Counter()
  total_yes_count = 0
  for row in data:
    if len(row) == 0: # end of group
      for key in group_yes_counts.keys():
        if group_yes_counts[key] == group_size:
          total_yes_count += 1
        # print(f"group_yes_counts[{key}] = {group_yes_counts[key]}, group_size = {group_size}, total_yes_count = {total_yes_count}")
      group_yes_counts.clear()
      group_size = 0
      print()
    else:
      for c in row:
        group_yes_counts[c] += 1
      group_size += 1
      # print(f"group_size = {group_size}, row was {row}")

  for key in group_yes_counts.keys():
    if group_yes_counts[key] == group_size:
      total_yes_count += 1
    # print(f"group_yes_counts[{key}] = {group_yes_counts[key]}, group_size = {group_size}, total_yes_count = {total_yes_count}")

  print(f"Total: {total_yes_count}")
