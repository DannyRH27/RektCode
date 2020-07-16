def calculateTime(keyboard, word):
  new_dict = {char: idx for idx, char in enumerate(keyboard)}
  i = 1
  time = new_dict[word[0]]
  while i < len(word):
   
    time += abs(new_dict[word[i-1]] - new_dict[word[i]])
    i+=1
  
  return time

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
print(calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))
