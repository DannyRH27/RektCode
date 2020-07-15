def numJewelsInStones(J, S):
  jewels = 0
  for stone in S:
    if stone in J:
      jewels +=1
  return jewels


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))