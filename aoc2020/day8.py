def load_data():
  data = open('aoc2020/day8-input.txt').readlines()
  data = [ d.strip() for d in data ]

  # nop +0
  # acc +1
  # jmp +4
  # acc +3
  # jmp -3
  # acc -99
  # acc +1
  # jmp -4
  # acc +6

  program = []
  for row in data:
    op, arg = row.split(' ')
    program.append((op, arg))

  return program

def part1():
  program = load_data()

  executed_lines = []
  current_line = 0
  acc = 0
  while True:
    if current_line in executed_lines:
      print(f"ACC: {acc}")
      break 
    op, arg = program[current_line]
    executed_lines.append(current_line)
    if op == 'nop':
      current_line += 1
    elif op == 'acc':
      acc += int(arg)
      current_line += 1
    elif op == 'jmp':
      current_line += int(arg)
    else:
      raise f"Bad operation: {op}"

count = 0

def run_program(program):
  executed_lines = []
  current_line = 0
  acc = 0
  
  while True:
    if current_line in executed_lines:
      return False
    if current_line >= len(program):
      print(f"Program completed. ACC: {acc}")
      return True

    op, arg = program[current_line]
    next_line = current_line + 1
    if op == 'acc':
      acc += int(arg)
    elif op == 'jmp':
      next_line = current_line + int(arg)

    executed_lines.append(current_line)
    current_line = next_line

def part2():
  program = load_data()

  for n in range(len(program)):
    p = program
    if program[n][0] == 'nop':
      p = program.copy()
      p[n] = ('jmp', p[n][1])
    elif program[n][0] == 'jmp':
      p = program.copy()
      p[n] = ('nop', p[n][1])
    run_program(p)
