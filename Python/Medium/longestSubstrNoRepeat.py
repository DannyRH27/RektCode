'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = ""
Output: 0

maintain a set to see which chars we've seen.
keep track of longest
if not in set,
increment count and add char to set
if in set,
reset set with just that char
count is now 1

two pointers,
keep track of the latest index of letter


'''

def lengthOfLongestSubstring(s):
  if not s:
    return 0

  



assert(lengthOfLongestSubstring("abcabcbb") == 3)
assert(lengthOfLongestSubstring("bbbbbb") == 1)
assert(lengthOfLongestSubstring("") == 0)
assert(lengthOfLongestSubstring("dvdf") == 3)
assert(lengthOfLongestSubstring("dvoqdldf") == 3)

'''
i see the d
move left until not same as right
make count = j - i
continue counting
can't do iteration, need to keep track of the index
'''
