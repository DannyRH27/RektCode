def kidsWithCandies(candies, extraCandies):
  max_candies = max(candies)
  for idx, n in enumerate(candies):
    if n + extraCandies >= max_candies:
      candies[idx] = True
    else:
      candies[idx] = False

  return candies