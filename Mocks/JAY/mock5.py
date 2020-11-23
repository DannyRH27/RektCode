'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()()"]

with a set to keep track of combos and duplicates,
recursive call with the 
'''

def generateParenthesis(n):
  lst = []
  def recurse(num_opens, combo):
    if len(combo) == n*2:
      lst.append(combo)
      return

    if num_opens > 0:
      recurse(num_opens - 1, combo + ")", lst)

    if (n*2) - len(combo) - num_opens >= 2:
      recurse(num_opens + 1, combo + "(", lst)
  
  recurse(0, "")

  return lst
