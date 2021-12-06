import pprint
pp = pprint.PrettyPrinter()

def load_data():
  data = open('aoc2020/day7-input.txt').readlines()
  data = [ d.strip() for d in data ]

  bags = {}
  for row in data:
    # light red bags contain 1 bright white bag, 2 muted yellow bags.
    # dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    # bright white bags contain 1 shiny gold bag.
    # muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    # shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    # dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    # vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    # faded blue bags contain no other bags.
    # dotted black bags contain no other bags.
    container, contents = row.split(' bags contain ')
    for content in contents.split(', '):
      # print(f"content: '{content}'")
      if content == 'no other bags.':
        bags[container] = []
      else:
        count, adjective, color, bag = content.split(' ')
        color = f"{adjective} {color}"
        if container not in bags: bags[container] = []
        bags[container].append((int(count), color))

  # pp.pprint(bags)
  return bags

def check_contents(bags, bag, my_bag):
  for content in bags[bag]:
    if content[1] == my_bag:
      return True
    else:
      # recursively check this contents of this bag
      if check_contents(bags, content[1], my_bag):
        return True

def part1():
  bags = load_data()

  my_bag = 'shiny gold'
  count = 0
  for color in bags.keys():
    if check_contents(bags, color, my_bag):
      count += 1

  print(count)

def count_bags(bags, bag):
  print(f"bag: {bag}, {bags[bag]}")
  count = 0
  for content in bags[bag]:
    # print(f"content: {content}")
    sub_count = count_bags(bags, content[1])
    count += content[0] + sub_count * content[0]
    print(f"{content[1]} contains {sub_count} bags, times {content[0]}, total count is {count}")
  return count

def part2():
  bags = load_data()

  my_bag = 'shiny gold'
  count = count_bags(bags, my_bag)

  print(count)  
