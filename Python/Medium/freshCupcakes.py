'''
You are the owner of a cupcake shop which makes only one kind of cupcake. 
The cupcakes are baked in batches of K and every batch has to be served completely before another one can be made.

Customers walk into your shop in groups and each group has to be served cupcakes before you move onto serving the next group.

How many groups only get fresh cupcakes?

we can mod every group to see how many cupcakes would be leftover and store the result in a hash with the mod remaining as the key and a deque as the value,
then we would first start a list starting with all the groups with 

if the mods add together to equal K, then we can pop and pair these so that the next batch gets fresh cupcakes.
once we pop, we should check the length of the queue and if it is 0 then delete the key.
once the dictionary only has one key, we can just add the rest of these to the order and call it a day.

store mods that appear in a list, iterate from biggest mod to lowest (this is (0-9) so it would be constant time)
how would we order the pairs so that i go through all of the ones with potential pairs first??
'''
from collections import deque
def freshCupcakes(input):
  K = input[0]
  my_dict = {}
  for n in input[1:]: 
    mod = n % K
    if mod in my_dict:
      my_dict[mod].append(n)
    else:
      my_dict[mod] = deque([n])

  ans = list(my_dict[0])
  print(ans)



assert(freshCupcakes([3,4,3]) == 1)
assert(freshCupcakes([3,3,4]) == 2)
assert(freshCupcakes([3,6,3,4]) == 2)
assert(freshCupcakes([3,4,6]) == 1)