import sys, math

def load_data():
  return [ row.strip() for row in open('day13-input.txt').readlines() ]

def part1():
  data = load_data()
  arrival = int(data[0])
  busses = data[1].split(',')
  # print(f"busses: {busses}")
  earliest_bus = sys.maxsize
  earliest_bus_arrival = sys.maxsize

  for bus in busses:
    # print(f"bus: {bus}")
    if bus == 'x': continue
    t, bus = int(bus), int(bus)
    while t < arrival:
      t += bus
      # print(t)
    if t < earliest_bus_arrival:
      print(f"earlier bus: {bus}, t: {t}")
      earliest_bus = bus
      earliest_bus_arrival = t

  wait = earliest_bus_arrival - arrival
  print(f"result: {wait * earliest_bus}")

def part2():
  data = load_data()
  busses = data[1].split(',')
  times = []
  time = 0
  for bus in busses:
    if bus == 'x': times.append(None)
    else: times.append(int(bus))

#   print(times)
#   range_len_times = range(len(times))
#   for n in range(len(times)):
#     if times[n] is not None: print(f"{n}, ", end='')
#   print("")
  range_len_times = [0, 13, 23, 36, 37, 52, 54, 60, 73]
  largest = 509

  time = 100000000000000
  for n in range_len_times:
    multiple = math.floor(time / times[n])
    times[n] *= multiple  

  while True:
    # check if we're done
    done = True
    for n in range_len_times:
    #   if times[n] is None:
    #     continue
      if times[n] != time + n:
        done = False

    if done:
      print(f"Time: {time}")
      break

    # bump up all the times
    time += largest
    changes = False
    while not changes:
      changes = False
      for n in range_len_times:
        if times[n] <= time + n:
            times[n] += int(busses[n])
            changes = True

    if time % 100000 == 0: print(time, end='\r')
    # if time > 100: break
