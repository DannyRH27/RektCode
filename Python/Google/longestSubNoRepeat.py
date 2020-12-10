def lengthOfLongestSubstring(s):
  if len(s) == 0:
    return 0
  check = set()
  curr_max = 0
  count = 0
  for i in range(len(s)):
    letter = s[i]
    print(letter, check, count, curr_max)
    if letter in check:
      count = 0
      check.remove(letter)
    count += 1
    check.add(letter)
    if count > curr_max:
      curr_max = count

  return curr_max


assert(lengthOfLongestSubstring("abcabcbb")==3)
assert(lengthOfLongestSubstring("bbbbb") == 1)
assert(lengthOfLongestSubstring("pwwkew") == 3)
assert(lengthOfLongestSubstring("") == 0)
assert(lengthOfLongestSubstring("dvdf") == 3)
