'''
swap for longest repeated character substring
sounds disgusting

given string text

can swap 2 chars in str
find length of longest substring with repeated characters

need to find current longest substring of repeated

if i knew where each substr started and ended,
one pass
a hashmap of letters and ranges for substrings
what can value be to make it easier for me to swap intelligently
set of indices?
'aaababba'
'aaabbaaa'
'aaabaaa'

a => [(0,2),[4,6]]
b => [3,3]

(3,4)
(3,5)
a => 3
b => 1


Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. 
Then, the longest repeated character substring is "aaa", which its length is 3.

Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), 
and we get longest repeated character substring "aaaaaa", which its length is 6.

Example 3:
Input: text = "aaabbaaa"
Output: 4

Example 4:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
if len(set) == 1, return len(text)

Example 5:
Input: text = "abcdef"
Output: 1
if len(set) == len(text) return 1
Constraints:
1 <= text.length <= 20000
text consist of lowercase English characters only.

runtime: O(n)
space: O(m) x O(o) where m is the number of unique letters and o is the amount of ranges

need to also keep track of which one is the longest

figure out the gap,
iterate through my ranges, two at a time and if difference -1 is 1, i can use this gap, 

only one range, just return length of that range
Only have two ranges, so take the lengths and add them together
More than two, then i take the lengths and add them together and then + 1

len(hash[a])

and save current biggest count
is it bigger than my current biggest, if so replace, if not cool

this would give me all of my gaps
figure out what to swap with

'aaabaaabccdefa'
'''


def maxRepOpt1(text):
  start = 0
  end = 0
  curr_letter = text[start]

  my_dict= {}

  while end < len(text):
    check = text[end]
    if check != curr_letter:
      if curr_letter not in my_dict:
        my_dict[curr_letter] = []

      my_dict[curr_letter].append([start, end-1])
      curr_letter = text[end]
      start = end
    
    end += 1
  
  my_dict[curr_letter].append([start, end-1])

  count = 0
  letters = set(text)

  for letter in letters:
    ranges = my_dict[letter]

    if len(ranges) == 1:
      first, second = ranges[0]

      count = max(count, second - first)
    elif len(ranges) == 2:
      first, second = ranges[0], ranges[1]

      check1 = first[1] - first[0] + 1
      check2 = second[1] - second[0] + 1
      if second[0] - first[1] == 2:
        count = max(count, check1 + check2)
      else:
        count = max(check1+1, check2+1, count)
    else:
      first, second = 0, 1
      while second < len(ranges):
        range1 = ranges[first]
        range2 = ranges[second]

        check1 = range1[1] - range1[0] + 1
        check2 = range2[1] - range2[0] + 1
        if range2[0] - range1[1] == 2:
          count = max(count, check1 + check2 + 1)
        else:
          count = max(check1+1, check2+1, count)
        
        first += 1
        second += 1


    return count

  
assert(maxRepOpt1("ababa") == 3)
# assert(maxRepOpt1('aaababba') == 5)
# assert(maxRepOpt1('aaabbaaa') == 4)
# assert(maxRepOpt1('aaabaaa') == 6)
