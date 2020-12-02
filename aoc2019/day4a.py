def run():
  input_start, input_end = 145852, 616942

  # Two adjacent digits are the same (like 22 in 122345).
  # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
  
  count = 0
  for n in range(input_start, input_end+1):
    s = str(n)
    # print(s)
    adjacent, decreasing = False, False
    prev = 0
    for c in s:
      d = int(c)
      if d == prev: adjacent = True
      if d < prev: decreasing = True
      prev = d
    if adjacent and not decreasing:
      print(s)
      count += 1

  print("Total: %d" % count)    
      