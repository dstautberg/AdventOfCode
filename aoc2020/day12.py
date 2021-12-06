import math

def load_data():
  return [ line.strip() for line in open('aoc2020/day12-input.txt').readlines() ]

def part1():
  data = load_data()
  
  x, y = 0, 0
  dirs = ['E','S','W','N']
  dir = 0
  for row in data:
    action, count = row[0], int(row[1:])
    if action == 'N':
      y -= count
    elif action == 'S':
      y += count
    elif action == 'E':
      x += count
    elif action == 'W':
      x -= count
    elif action == 'L':
      if (count % 90) != 0: raise Exception(f"Weird turning angle: {count}")  
      dir = (dir - (count / 90)) % 4
    elif action == 'R':
      if (count % 90) != 0: raise Exception(f"Weird turning angle: {count}")  
      dir = (dir + (count / 90)) % 4
    elif action == 'F':
      if dir == 0: x += count
      elif dir == 1: y += count
      elif dir == 2: x -= count
      elif dir == 3: y -= count
      else: raise Exception(f"Bad direction: {dir}")
    else:
      raise Exception(f"Bad action: {action}")
    print(f"x, y = {x}, {y}")

  print(f"x, y = {x}, {y}: {math.fabs(x) + math.fabs(y)}")

def rotate_left(x, y):
  # 10, 4 -> -4,10 -> -10,-4 ->  4,-10
  return (y, -x)

def rotate_right(x, y):
  #  10,-4 -> 4,10 -> -10,4 -> -4,-10
  return (-y, x)

def part2():
  data = load_data()
  x, y = 0, 0 # ship location: +x = east, +y = south
  wx, wy = 10, -1 # waypoint location relative to the ship
  for row in data:
    action, count = row[0], int(row[1:])
    
    if action == 'N': # move waypoint north
      wy -= count
    elif action == 'S': # move waypoint south
      wy += count
    elif action == 'E': # move waypoint east
      wx += count
    elif action == 'W': # move waypoint west
      wx -= count
    elif action == 'L': # rotate waypoint around the ship to the left
      for n in range(int(count / 90)):
        wx, wy = rotate_left(wx, wy)
    elif action == 'R': # rotate waypoint around the ship to the right
      for n in range(int(count / 90)):
        wx, wy = rotate_right(wx, wy)
    elif action == 'F':
      for n in range(count):
        x += wx
        y += wy
    else:
      raise Exception(f"Bad action: {action}")
    print(f"action: {action} - x, y = {x}, {y} - wx, wy = {wx}, {wy}")

  print(f"x, y = {x}, {y}: {math.fabs(x) + math.fabs(y)}")
