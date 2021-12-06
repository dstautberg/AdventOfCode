def part1():
  seats = open('aoc2020/day5-input.txt').readlines()
  seats = [ s.strip() for s in seats ]
  highest_seat_id = 0
  seat_ids = []

  for seat in seats:
    min_row, max_row = 0, 127
    min_col, max_col = 0, 7
    for c in seat:
      if c == 'F': max_row = (min_row + max_row + 1) / 2 - 1
      if c == 'B': min_row = (min_row + max_row + 1) / 2
      if c == 'L': max_col = (min_col + max_col + 1) / 2 - 1
      if c == 'R': min_col = (min_col + max_col + 1) / 2
      # print(f"c: {c}, min_row: {min_row}, max_row: {max_row}, min_col: {min_col}, max_col: {max_col}")

    seat_id = min_row * 8 + min_col
    seat_ids.append(seat_id)
    # print(f"Seat: {seat}, Seat ID: {seat_id}")
    # print(seat_ids)
    if seat_id > highest_seat_id: highest_seat_id = seat_id

  print(f"\nHighest Seat ID: {highest_seat_id}")
  seat_ids.sort()
  return seat_ids, highest_seat_id

def part2():
  seat_ids, highest_seat_id = part1()
  # print(seat_ids)
  for seat_id in range(0, int(highest_seat_id) + 1):
    if seat_id not in seat_ids: print(f"Missing Seat ID {seat_id}")  
