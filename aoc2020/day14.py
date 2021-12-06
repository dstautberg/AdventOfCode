
def load_data():
  return [ d.strip() for d in open('aoc2020/day14-input.txt').readlines() ]

def bitfield(n, size):
    n = int(n)
    bits = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
    padding = size - len(bits)
    return [0] * padding + bits

def bits_to_int(bits):
  val = 0
  bits.reverse()
  for n, bit in enumerate(bits):
    if bit == 1: val += 2**n
  return val

def part1():
  data = load_data()
  print(data)

  memory = {}
  mask = ''

  for row in data[1:]:
    if row[0:4] == 'mask':
        s, mask = data[0].split(' = ')
        mask = list(mask)
        print(f"  mask={mask}\n")
    else:
      mem, val = row.split(' = ')
      addr = mem[4:-1]
      val = bitfield(val, len(mask))

      masked_val = val.copy()
      for n in range(len(mask)):
        if mask[n] == 'X': continue
        elif mask[n] == '1' and val[n] == 0:
          masked_val[n] = 1
          # print(f"converted bit {n} to 1")
        elif mask[n] == '0' and val[n] == 1:
          masked_val[n] = 0
          # print(f"converted bit {n} to 0")
      new_value = bits_to_int(masked_val)
      print(f"mask:       {mask}")
      print(f"masked_val: {masked_val}")
      print(f"Assigning address {addr} value {new_value}")
      memory[addr] = new_value

  total = 0
  for key in memory.keys():
    print(f"address {key} = {memory[key]} ")
    total += memory[key]
  print(f"Total: {total}")
