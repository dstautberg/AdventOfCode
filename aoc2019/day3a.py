import sys

def run():
  input = open('day3-input.txt').readlines()
  print("input: %s" % input)

  path1 = expand_path(input[0])
  path2 = expand_path(input[1])

  # print("path1:%s\n\n" % path1)
  # print("path2:%s\n\n" % path2)
  # display(path1, path2)

  closest = 1000000000
  for pos1 in path1:
    print(pos1)
    if contains(pos1[0], pos1[1], path2):
      print("Found intersection at %s" % pos1)
      d = abs(pos1[0]) + abs(pos1[1])
      if d < closest: closest = d
    
  print("Closest intersection is %d" % closest)

def display(path1, path2):
  x1, x2 = 0, 0
  y1, y2 = 0, 0
  for pos in path1:
    if pos[0] < x1: x1 = pos[0]
    if pos[0] > x2: x2 = pos[0]
    if pos[1] < y1: y1 = pos[1]
    if pos[1] > y2: y2 = pos[1]
  print ("x1=%d, x2=%d, y1=%d, y2=%d" % (x1, x2, y1, y2))
  for y in range(y2, y1-1, -1):
    for x in range(x1, x2+1):
      if contains(x, y, path1): print('1', end='')
      elif contains(x, y, path2): print('2', end='')
      else: print('.', end='')
    print('')

def contains(x, y, path):
  for pos in path:
    if pos[0] == x and pos[1] == y: return True

def expand_path(path):
  path = path.split(',')
  #print("Input path: %s" % path)
  result = []
  x, y = 0, 0
  for move in path:
    dir = move[0]
    len = int(move[1:])
    for n in range(len):
      if dir == 'R': x += 1
      elif dir == 'L': x -= 1
      elif dir == 'U': y += 1
      elif dir == 'D': y -= 1
      result.append([x,y])
    #print("Move was %s:%d, x,y=%d,%d result is now: %s" % (dir, len, x, y, result))
  return result
