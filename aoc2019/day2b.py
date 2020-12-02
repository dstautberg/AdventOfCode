import copy

# Bailed on this one, it never matched on the right result
def run():
  input = open('day2-input.txt').read()
  print("input: %s" % input)
  numbers = [ int(n) for n in input.split(',') ]
  for noun in range(0,100):
    for verb in range(0,100):
      result = process(copy.copy(numbers))
      if result == 19690720: print("%d%d" % (noun, verb))

def process(numbers):
  pos = 0
  while True:
    opcode = numbers[pos]
    #print("opcode: %d" % opcode)
    if opcode == 1:
      p1, p2, p3 = numbers[pos+1:pos+4]
      ##print("Adding positions %d and %d, storing at position %d" %(p1, p2, p3))
      n1 = numbers[p1]
      n2 = numbers[p2]
      numbers[p3] = n1 + n2
      #print("New list: %s" % numbers) 
    elif opcode == 2:
      p1, p2, p3 = numbers[pos+1:pos+4]
      #print("Multiplying positions %d and %d, storing at position %d" %(p1, p2, p3))
      n1 = numbers[p1]
      n2 = numbers[p2]
      numbers[p3] = n1 * n2
      #print("New list: %s" % numbers) 
    elif opcode == 99:
      #print("Quitting")
      break
    pos += 4
  return numbers[0]