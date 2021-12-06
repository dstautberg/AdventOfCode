def load_data():
  data, n = [{}], 0
  valid_count = 0
  rows = open('aoc2020/day4-input.txt').readlines()
  # byr (Birth Year)
  # iyr (Issue Year)
  # eyr (Expiration Year)
  # hgt (Height)
  # hcl (Hair Color)
  # ecl (Eye Color)
  # pid (Passport ID) (optional)
  # cid (Country ID)

  for row in rows:
    row = row.strip()
    print(n, row)
    if row == '':
      n += 1
      data.append({})
    else:
      entries = row.split(' ')
      for entry in entries:
        key, value = entry.split(':')
        # print(f"data[{n}]['{key}'] = '{value}'")
        data[n][key] = value
  # print(data[n])
  return data

def part1():
  data = load_data()
  valid_count = 0
  for row in data:
    print(row)
    if ('byr' in row) and ('iyr' in row) and ('eyr' in row) and ('hgt' in row) and ('hcl' in row) and ('ecl' in row) and ('pid' in row):
      valid_count += 1
    print(valid_count)
  print(f"Valid passports: {valid_count}")

def part2():
  data = load_data()
  valid_count = 0
  for row in data:
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    valid = True
    print(row)

    if ('byr' not in row) or ('iyr' not in row) or ('eyr' not in row) or ('hgt' not in row) or ('hcl' not in row) or ('ecl' not in row) or ('pid' not in row):
      print("missing required field")
      valid = False

    if valid:
      byr = int(row['byr'])
      if byr < 1920 or byr > 2002:
        print('byr not between 1920 and 2002')
        valid = False
    
    if valid:
      iyr = int(row['iyr'])
      if iyr < 2010 or iyr > 2020:
        print("iyr not between 2010 and 2020")
        valid = False
    
    if valid:
      eyr = int(row['eyr'])
      if eyr < 2020 or eyr > 2030:
        print("eyr not between 2020 and 2030")
        valid = False

    if valid:
      hgt_units = row['hgt'][-2:]
      if hgt_units != 'cm'and hgt_units != 'in':
        print("hgt not followed by cm or in")
        valid = False
      else:
        hgt_num = int(row['hgt'][0:-2])
        if hgt_units == 'cm':
          if hgt_num < 150 or hgt_num > 193:
            print("hgt not between 150 and 193")
            valid = False
        if hgt_units == 'in':
          if hgt_num < 59 or hgt_num > 176:
            print("hgt not between 59 and 176")
            valid = False

    if valid:
      if row['hcl'][0] != '#':
        print("hcl must start with #")
        valid = False

    if valid:
      if len(row['hcl']) != 7:
        print("hcl must be 7 characters long")
        valid = False

    if valid:
      for c in row['hcl'][1:]:
        if c not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
          print("hcl can only contain digits and a-f")
          valid = False

    if valid:
      if row['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        print("ecl not valid")
        valid = False

    if valid:
      pid = row['pid']
      if len(pid) != 9: valid = False
      for c in pid:
        if c not in ['0','1','2','3','4','5','6','7','8','9']:
          print("pid can only contains digits")
          valid = False

    if valid: valid_count += 1

  print(f"Valid passports: {valid_count}")
