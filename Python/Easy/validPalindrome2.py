def validPalindrome(s):
  if s == s[::-1]:
    return True

  left, right = 0, len(s)-1

  while left < right:
    letter1 = s[left]
    letter2 = s[right]

    if letter1 != letter2:
      p = s[0:left] + s[left+1:]
      q = s[0:right] + s[right+1:]
      break
    else:
      left +=1
      right -=1

  if p == p[::-1] or q == q[::-1]:
    return True
  return False

assert(validPalindrome("aba") == True)
assert(validPalindrome("abca") == True)
assert(validPalindrome("abcbba") == True)
assert(validPalindrome("cbbcc") == True)
