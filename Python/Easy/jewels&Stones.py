def numJewelsInStones(J, S):

  new_set = set(J)
  jewels = 0
  for stone in S:
    if stone in new_set:
      jewels +=1
  return jewels


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))