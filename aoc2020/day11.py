import copy

def load_data():
  return [ list(line.strip()) for line in open('aoc2020/day11-input.txt').readlines() ]
  
def append_seat(seats, data, row, col):
  if row >= 0 and col >= 0 and row < len(data) and col < len(data[0]):
    seats.append(data[row][col])

def adjacent_seats(data, row, col):
  seats = []
  append_seat(seats, data, row-1, col-1) # upper left
  append_seat(seats, data, row-1, col)   # upper middle
  append_seat(seats, data, row-1, col+1) # upper right
  append_seat(seats, data, row, col-1)   # left
  append_seat(seats, data, row, col+1)   # right
  append_seat(seats, data, row+1, col-1) # lower left
  append_seat(seats, data, row+1, col)   # lower middle
  append_seat(seats, data, row+1, col+1) # lower right
  return seats

def part1():
  data = load_data()
  # print(f"part1, data: {data}")
  round = 0
  did_seats_change = True
  while did_seats_change:
    did_seats_change = False
    prev_data = copy.deepcopy(data)

    for row in range(len(prev_data)):
      for col in range(len(prev_data[row])):
        seat = prev_data[row][col]
        if seat == '.': # floor
          pass
        elif seat == 'L': # empty
          # print(f"empty seat at {row}, {col}, adjacent seats: {adjacent_seats(prev_data, row, col)}")
          if '#' not in adjacent_seats(prev_data, row, col):
            # print(f"Seating someone at {row}, {col}")
            data[row][col] = '#'
            did_seats_change = True
        elif seat == '#': # occupied
          # print(f"occupied seat at {row}, {col}, adjacent seats: {adjacent_seats(prev_data, row, col)}")
          if adjacent_seats(prev_data, row, col).count('#') >= 4:
            # print(f"Leaving seat at {row}, {col}")
            data[row][col] = 'L'
            did_seats_change = True

    print(f"FINISHED ROUND {round}\n")
    round += 1

  occupied_seats = 0
  for row in data:
    occupied_seats += row.count('#')
  print(f"occupied seats: {occupied_seats}")

def first_visible_seat(data, row, col, row_direction, col_direction):
  r, c = row + row_direction, col + col_direction
  while r >= 0 and c >= 0 and r < len(data) and c < len(data[0]):
    if data[r][c] != '.':
      return data[r][c]
    else:
      r += row_direction
      c += col_direction

def visible_seats(data, row, col):
  return [
    first_visible_seat(data, row, col, -1, -1),
    first_visible_seat(data, row, col, -1, 0),
    first_visible_seat(data, row, col, -1, 1),
    first_visible_seat(data, row, col, 0, -1),
    first_visible_seat(data, row, col, 0, 1),
    first_visible_seat(data, row, col, 1, -1),
    first_visible_seat(data, row, col, 1, 0),
    first_visible_seat(data, row, col, 1, 1),
  ]

def part2():
  data = load_data()
  round = 0
  did_seats_change = True
  while did_seats_change:
    did_seats_change = False
    prev_data = copy.deepcopy(data)

    for row in range(len(prev_data)):
      for col in range(len(prev_data[row])):
        seat = prev_data[row][col]
        if seat == '.': # floor
          pass
        elif seat == 'L': # empty
          # print(f"empty seat at {row}, {col}, adjacent seats: {adjacent_seats(prev_data, row, col)}")
          if '#' not in visible_seats(prev_data, row, col):
            # print(f"Seating someone at {row}, {col}")
            data[row][col] = '#'
            did_seats_change = True
        elif seat == '#': # occupied
          # print(f"occupied seat at {row}, {col}, adjacent seats: {adjacent_seats(prev_data, row, col)}")
          if visible_seats(prev_data, row, col).count('#') >= 5:
            # print(f"Leaving seat at {row}, {col}")
            data[row][col] = 'L'
            did_seats_change = True

    print(f"FINISHED ROUND {round}\n")
    round += 1

  occupied_seats = 0
  for row in data:
    occupied_seats += row.count('#')
  print(f"occupied seats: {occupied_seats}")
