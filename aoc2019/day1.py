import math

def run():
  input = open('day1-input.txt').readlines()
  sum = 0
  for line in input:
    n = math.floor(int(line.strip()) / 3) - 2
    sum += n
    print("sum: %d" % sum)
    more = math.floor(n / 3) - 2
    while more > 0:
      print("more: %d" % more)
      sum += more
      more = math.floor(more / 3) - 2

  print("sum: %d" % sum)
