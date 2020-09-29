# ## Task A
# You were given a natural number number.
# Return a string with all numbers from 1 to 'number' using recursion.
# You can divide each digit by spaces or new lines.

def task_a(num):
  if num == 1:
    return str(1)
  else:
    return str(task_a(num-1)) + " " + str(num)


print(task_a(10)) # "1 2 3 4 5 6 7 8 9 10"
print(task_a(5)) # "1 2 3 4 5"


### Task B
# You were given two numbers 'number1' and 'number2'.
# If 'number1' < 'number2', return a string with all numbers
# from 'number1' to 'number2' including them.
# Otherwise, return a string with all numbers from number1 to number2 in descending order.

# def task_b(num1, num2):


# end

# p task_b(1, 10) # "1 2 3 4 5 6 7 8 9 10"
# p task_b(9, 2) # "9 8 7 6 5 4 3 2"


### Task C
# You were given two integers 'number1' and 'number2'.
# Implement Ackermann function A(number1,number2) using recursion.
# https://wikimedia.org/api/rest_v1/media/math/render/svg/1a15ea2fcf1977e497bccdf1916ae23edc412fff

# def task_c(num1, num2):


# end

# p task_c(3, 2) # 29

### Task D
# You were given a natural number 'number'.
# Write a function that returns true if 'number' is a power of two.
# You should not use the exponentiation operator!


# def task_d(num):


# end

# p task_d(64) # true
# p task_d(128) # true
# p task_d(17) # false


# ### Task E
# You were given a natural 'number'. Calculate the sum of its digits.
# You should not use string, array or loops.

# def task_e(num):


# end

# p task_e(1459) # 19
# p task_e(367) # 16
# p task_e(39) # 12


# ### Task F
# You were given a natural number 'number'. Return all its digits one by one in reverse order separating them by spaces or new lines
# You should not use string, array or loops. Use only recursion and arithmetic operators.

# def task_f(num):


# end

# p task_f(1459) # "9 5 4 1"
# p task_f(367) # "7 6 3"
# p task_f(39) # "9 3"


# ### Task G
# You were given a natural number 'number'.
# Return all its digits one by one in initial order separating them by spaces or new lines
# You should not use string, array or loops.
# Use only recursion and arithmetic operators.

# def task_g(num):


# end

# p task_g(1459) # "1 4 5 9"
# p task_g(367) # "3 6 7"
# p task_g(39) # "3 9"


# ### Task H
# You were given a natural number 'number' (number > 1).
# Check if 'number' is a prime number or not.
# The function should return true, if 'number' is  prime, and return false, if 'number' is not prime.
# The algorithm should have time complexity O(log n).
# Hint: you should add one argument to the function as a divisor.

# def task_h(num):


# end

# p task_h(7, 6) # true
# p task_h(10, 9) # false
# p task_h(13, 12) # true


# ### Task I
# You were given a word consisting only of lowercase latin letters.
# Check if the word is a palindrome.
# The function should return true or false.
# You should not use loops.

# def task_i(word):


# end

# p task_i('racecar') # true
# p task_i('banana') # false


# ### Task J
# You were given a sequence of natural numbers (that should look like one number in a string).
# Return all odd numbers from this sequence keeping their initial order.
# You should not use global variables.

# def task_j(seq):


# end

# p task_j('4567') # "57"
# p task_j('24680') # ""
# p task_j('7777') "7777"


# ### Task K
# You were given a sequence of numbers.
# Return the first, third, fifth etc. numbers from the sequence.
# You should not use global variables.

# def task_k(seq):


# end

# p task_k([1,2,3,4,5,6,7,8]) # [1,3,5,7]
# p task_k([1,2,3,4,5,6,7,8,9]) # [1,3,5,7,9]


# ### Task L
# You were given a sequence of - natural numbers.
# Return the biggest number from the sequence.

# def task_l(seq):


# end

# p task_l([1,2,3,4,5,6]) # 6
# p task_l([20, 29, 4]) # 29
# p task_l([100, 25, 6, 89]) # 100
