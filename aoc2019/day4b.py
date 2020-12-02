def run():
  input_start, input_end = 145852, 616942

  # Two adjacent digits are the same (like 22 in 122345).
  # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
  
  # Part 2:
  # 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
  # 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
  # 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
  
  count = 0
  for n in range(input_start, input_end+1):
    if is_match(n):
      print(n)
      count += 1
  
  print(count)    
      
def is_match(n):
  s = str(n)
  # print(s)
  adjacent, decreasing = False, False
  repeated_digit_count = 0
  repeated_digit_counts = []
  prev = 0

  for c in s:
    d = int(c)
    if d < prev: decreasing = True
    # print("d=%d, prev=%d" % (d, prev))
    if d == prev:
      repeated_digit_count = 2 if repeated_digit_count == 0 else repeated_digit_count + 1
      # print("repeated_digit_count: %d" % repeated_digit_count)
    else:
      if repeated_digit_count > 0:
        repeated_digit_counts.append(repeated_digit_count)
        repeated_digit_count = 0
      # print("repeated_digit_counts: %s" % repeated_digit_counts)
    prev = d

  if repeated_digit_count > 0:
    repeated_digit_counts.append(repeated_digit_count)
  for n in repeated_digit_counts:
    if n == 2: adjacent = True
  # print("repeated_digit_counts: %s" % repeated_digit_counts)
  return adjacent and not decreasing
