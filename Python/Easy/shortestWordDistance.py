def shortestDistance(words, word1, word2):
  i = None
  j = None
  res = len(words)

  for n in range(len(words)):
    word = words[n]
    if word == word1:
      i = n
    if word == word2:
      j = n

    if i != None and j!= None:
      res = min(abs(i-j),res)

  return res if i != None and j != None else 0


assert(shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice") == 3)
assert(shortestDistance(["a", "a", "b", "b"], "a", "b") == 1)
assert(shortestDistance(["a", "a", "c", "b", "a"], "a", "b") == 1)
assert(shortestDistance(["a", "a", "c", "b", "a"], "b", "a") == 1)
assert(shortestDistance(["a", "b", "c", "d", "d"], "a", "d") == 3)
assert(shortestDistance(["a", "c", "b", "b", "a"], "a", "b") == 1)
