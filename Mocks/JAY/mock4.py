phone = {2: "abc",
3: "def",
4: "ghi",
5: "jkl",
6: "mno",
7: "pqrs",
8: "tuv",
9: "wxyz"}

'''
digits will be as long as needed, numbers will be anywhere from 2-9
return a list of all possible letter combinations
at the very least i have to hit every number and every letter in the number and then every combination
order of combos doesn't matter, but letter order does
i'll have a set to keep track of possible combinations
i will have a loop for each digit, and everytime i get a possible combination, i check the set and add if it isn't in the set.

recursion plan:
make a call, initially with empty string
in this call, i will make another call with an additional digit, 
i want to explore all possible combinations
digits = "223"

recursive(digits, "")
recursive(digits, "a")
recursive(digits, "b")
'''

def letterCombinations(digits):
  combos = set()

  if len(digits) == 0:
    return []
  
  def recursive_helper(digits, combos, current_combo):
    if len(current_combo) ==  len(digits):
      combos.add(current_combo)
      return
    
    for c in phone[digits[len(current_combo)]]:
      current_combo += c
      recursive_helper(digits, combos, current_combo)
      current_combo = current_combo[:-1]

  recursive_helper(digits, combos, "")
  
  return list(combos)



