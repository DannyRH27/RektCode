# Write a method, pow(base, exponent), that takes in two numbers.
# The method should calculate the base raised to the exponent power.
# You can assume the exponent is always positive.


def pow(base, exp):
  if exp == 0: 
    return 1
  else:
    return base * pow(base,exp - 1)


print(pow(2,0))
print(pow(3,8))