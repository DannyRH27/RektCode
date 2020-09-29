# Write a method, reverse_string(str), that takes in a string.
# The method should return the string with it's characters in reverse order.
#
# Solve this recursively!
#
# Examples:
#
# reverse_string("")            # => ""
# reverse_string("c")           # => "c"
# reverse_string("internet")    # => "tenretni"
# reverse_string("friends")     # => "sdneirf"


def reverseString(s):
  if not s:
    return s
  else:
    return s[-1] + reverseString(s[:-1])



print(reverseString("Hello"))
print(reverseString("You can be an Engineer, Danny"))
