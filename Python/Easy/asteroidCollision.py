def asteroidCollision(asteroids):
  # create stack
  # for every asteroid in asteroids
  # append the stack
  # if there are at least two asteroids in the stack and the first one is headed left and the second one is headed right,
  # pop both out, find out which is bigger, and append it back to the stack.
  # if both are equal, don't append back to stack
  # return stack

  stack = []

  for asteroid in asteroids:
    stack.append(asteroid)
    
    while len(stack) >= 2:
      if stack[-1] < 0 and stack[-2] > 0:
        first = stack.pop()
        second = stack.pop()
        
        if abs(first) > abs(second):
          stack.append(first)
        elif abs(first) < abs(second):
          stack.append(second)
      else:
        break

  return stack





print(asteroidCollision([5,10,-5]))
print(asteroidCollision([8,-8]))
print(asteroidCollision([10,2,-5]))
print(asteroidCollision([-2,-1,1,2]))