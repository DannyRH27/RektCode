def reverseStringF(s):
  def helper(left, right):
    if left < right:
      s[left], s[right] = s[right], s[left]
      helper(left+1, right-1)
  
  helper(0, len(s)-1)




reverseStringF("Hello")
reverseStringF("You can be an Engineer, Danny")