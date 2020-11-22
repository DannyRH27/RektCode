def minFlips(target):
  
  count = int(target[0])
  print(target,target[1:])
  for bulb1, bulb2 in zip(target,target[1:]):
    if bulb1 != bulb2:
      count += 1
  return count



print(minFlips("10111"))
print(minFlips("101"))
print(minFlips("00000"))
print(minFlips("001011101"))
