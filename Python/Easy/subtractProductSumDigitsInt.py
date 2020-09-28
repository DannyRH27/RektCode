def subtractProductAndSum(n):
  n_product = 1
  n_sum = 0
  n_list = list(str(n))

  for n in n_list:
    n_product *= int(n)
    n_sum += int(n)
  return n_product - n_sum


print(subtractProductAndSum(234))
print(subtractProductAndSum(888))
