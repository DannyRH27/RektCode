def maxProfit(prices):
  i = 0
  j = 1
  profit = 0
  while j < len(prices):
    print(prices[i],prices[j])
    if prices[i] >= prices[j]:
      i+=1
      j+=1
      continue
    else:
      profit += (prices[j] - prices[i])
      i+=1
      j+=1
  return profit


assert(maxProfit([7, 6, 4, 3, 1]) == 0)
