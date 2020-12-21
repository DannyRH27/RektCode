'''
There is a new alien language that uses the English alphabet. 
However, the order among letters are unknown to you.

You are given a list of strings words from the dictionary, 
where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language, and return it. 
If the given input is invalid, return "". 
If there are multiple valid solutions, return any of them.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

how do i compare two words?
zip words, compare letters, if not equal l1 is before l2.
hash[l1] = set(l2)

a => b
b => c
c => d
d => b

b => 1
c => 1
d => 1

t => f
w => e
r => t
e => r



t => 1
e => 1
f => 1
r => 1
w => 0

a => b
a => c

"nothing points to it, therefore this starts"
visited set that has w

topological sort
graph must be DAG
sorts based on direction of graph

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

ab, ac

abc, bca, bac all work

Insights/Questions:
Compare two words to begin understanding the rules
How do i traverse through these words or letters?

I could have a function that takes in two words, and my current ordering
hash where key is the letter, value is the ordering

'''

def alienOrder(words):
  order = {}

  letters = set()

  for word in words:
    for letter in word:
      letters.add(letter)

  i = 0

  while i + 1 < len(words):
    word1 = words[i]
    word2 = words[i+1]

    j = 0

    while j < len(word1) or j < len(word2):
      if j == len(word2) or j == len(word1):
        if len(word1) > len(word2):
            return ""
        else:
            break
      l1 = word1[j]
      l2 = word2[j]

      if l1 == l2:
        j += 1
        continue

      if l1 not in order:
        order[l1] = set()

      order[l1].add(l2)
      break
    i += 1

  values = order.values()

  counter = {}
  for value in values:
    for letter in value:
      if letter not in counter:
        counter[letter] = 0

      counter[letter] += 1

  ans = ""
  starters = set()
  # identify the starters
  for letter in letters:
    if letter not in counter:
      starters.add(letter)

  if not len(starters):
    return ""

  while len(starters):
    temp = starters.pop()
    ans += temp
    if temp not in order:
        continue
    for letter in order[temp]:
      counter[letter] -= 1
      if counter[letter] == 0:
        starters.add(letter)
        del counter[letter]

    del order[temp]

  if len(ans) != len(letters):
    ans = ""
  return ans
      

# print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(alienOrder(["abc", "ab"]))
print(alienOrder(["wrt", "wrtkj"]))
