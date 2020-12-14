'''
Finding valid routes
Dasher will first pick up order, then drop off
Can also do batch deliveries
Multiple pickups, multiple dropoffs
dropoff must happen after pickup

Examples: P1, D1 -> valid P1, P2, D1, D2 -> valid P1, D1, P2, D2 -> valid 
P2, D2, P1, D2 -> invalid P1, D2, P2, D1 -> invalid 
P1, D2 -> invalid P1, P2, D2 -> invalid 
P1, D1, P1, D1 -> invalid P1, P2, D2, D1 -> valid 

['P1','P2']


Write a function to determine if route is valid

All pickups are valid
Deliveries are the orders i really care about.
i can have a set to keep track of the pickups that i have 
and when i encounter a delivery, i'll check my set to see if i have the package and if i do,
and it isn't in my delivered set, then add it to delivered and continue
return false if encountered same delivery

Have a second set of already delivered items

Call out assumptions more

Are the input strings uniform or do i need to clean the data?

Name things correctly and make your code readable.



'''

def validDelivery(route):
  if not len(route):
    return False
  
  pickup = set()
  delivered = set()
  for pkg in route:
    if pkg[0] is "p":
      if pkg[1] in pickup:
        return False
      pickup.add(pkg[1])
    else:
      if pkg[1] in pickup:
        if pkg[1] in delivered:
          return False
        else:
          delivered.add(pkg[1])
      else:
        return False

  return len(pickup) == len(delivered)



# assert(validDelivery(["P1","D1"]) == True)
# assert(validDelivery(["P1","D1","P2","D2"]) == True)
# assert(validDelivery(["P2","D2","P1","D2"]) == False)
# assert(validDelivery(["P1","P2","D1","D2"]) == True)
# assert(validDelivery(["P1","P2","P1","D2"]) == False)
# assert(validDelivery(["P1","D2","P2","D1"]) == False)
# assert(validDelivery(["P1","P2","D2"]) == False)
# assert(validDelivery(["P1","D1","P1","D1"]) == False)
# assert(validDelivery(["P1","P2","D2","D1"]) == True)


'''
N + 2N! 
'''
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

  pickups = ['p' + str(i) for i in range(1, N+1)]
  deliveries = ['d' + str(i) for i in range(1, N+1)]
  events = pickups + deliveries

  recursive_helper([], events)
  valid_routes = []
  for route in routes:
    if validDelivery(route):
      valid_routes.append(route)

  return valid_routes

print(possibleRoutes(2))
# assert(possibleRoutes(2) == set([['p1', 'd1', 'p2', 'd2'], ['p1', 'p2', 'd1', 'd2'], ['p1', 'p2', 'd2', 'd1'], ['p2', 'd2', 'p1', 'd1'], ['p2', 'p1', 'd1', 'd2'], ['p2', 'p1', 'd2', 'd1']]))
