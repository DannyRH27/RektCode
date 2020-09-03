def plusOne(digits):
  count = len(digits)


  for i in range(count):
    idx = count - 1 - i
    if digits[idx] == 9:
      digits[idx] = 0
    else:
      digits[idx] += 1
      return digits

  return [1] + digits



print(plusOne([4,3,2,1]))
print(plusOne([0]))
print(plusOne([9]))
print(plusOne([1,2,3]))