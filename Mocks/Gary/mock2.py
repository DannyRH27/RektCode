'''
Part 2: Given N deliveries, print out all the possible routes

Examples: N = 1 -> [p1, d1] 
N = 2 -> [p1, d1, p2, d2], [p1, p2, d1, d2], [p1, p2, d2, d1], [p2, d2, p1, d1], [p2, p1, d1, d2], [p2, p1, d2, d1]

at any given moment, i need to know what i can possibly put there
i can try this recursively and see what's available to be added and continue adding until len(list is N8 2)

I could get all the permutations of possible routes,

i know i have N amount of pickups and N amount of deliveries that need to be made
so i'd just do a permutation on these two lists
run them through my validRoute function and then if it's true, then append to list of valid routes
return the valid routes

'''
from .mock1 import validDelivery
def possibleRoutes(N):
  if not N:
    return False

  routes = []

  
  def recursive_helper(route, events):
    if len(route) == N * 2:
      routes.append(route)
      return

    for i in range(len(events)):
      event_copy = events[:i] + events[i+1:]
      recursive_helper(route + [events[i]], event_copy)

  pickups = ['P' + str(i) for i in range(1,N+1)]
  deliveries = ['D' + str(i) for i in range(1,N+1)]
  events = pickups + deliveries

  recursive_helper([], events)
  valid_routes = []
  for route in routes:
    if validDelivery(route):
      valid_routes.append(route)

  return valid_routes


possibleRoutes(2)

