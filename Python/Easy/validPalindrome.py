'''
two pointer method,
until pointers meet
if pointer points to a non alphanumeric, then next
if pointers are not equal, then return False
return True if we have iterated through the whole string
'''
def isPalindrome(s):
  lower = s.lower()

  clean = [x for x in lower if x.isalnum()]
  ans = "".join(clean)
  return ans == ans[::-1]


    

assert(isPalindrome("A man, a plan, a canal: Panama") == True)
assert(isPalindrome("race a car") == False)
assert(isPalindrome("0p") == False)
