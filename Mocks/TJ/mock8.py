'''

list of airline tickets (from, to)
Reconstruct the itinerary in order

All tickets belong to a man who first departs from JFK

Must begin with JFK
if there are multiple valid itineraries, return the itinerary that has the samllest lexical order when read as a single str


JFK LGB SJC
JFK SJC LGB

Use all tix once and only once

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
  But it is larger in lexical order.

The checks i have to do are not only which one returns to the other city, but also, sort them lexical order

build a dictionary,

and then recursively traverse my dict starting with JFK, and add all valid itineraries
then i could sort the itineraries and return the first.

Greedy approach,

while adding to dict, if just one destination, i can just compare and then add to front or end
if it's multiple, i can just sort bc it's not a huge operation


SFO => SDC UEU


'''
from collections import deque
def reconstructItinerary(trips):
  trip_dict = {}

  for (start,end) in trips:
    if start not in trip_dict:
      trip_dict[start] = {}
    
    trip_dict[start][end] += 1

  valid = []

  def recurse(itinerary, depart, trip_dict):
    if len(itinerary) == len(trips) + 1:
      valid.append(" ".join(itinerary))
      return
    
    if not trip_dict[depart]:
      return
    cities = trip_dict[depart].items()
    for (city, count) in cities:
      if count is 0:
        continue
      
      trip_dict[depart][city] -= 1
      if trip_dict[depart][city] == 0:
        del trip_dict[depart][city]
      itinerary.append(city)
      recurse(itinerary, city, trip_dict)
      if city not in trip_dict[depart]:
        trip_dict[depart][city] = 0
      trip_dict[depart][city] += 1
      itinerary.pop()
      
    recurse(["JFK"], "JFK")

    valid.sort()
    ans = valid[0]
    return ans.split()


    
