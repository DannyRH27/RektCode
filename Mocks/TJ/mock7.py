'''
Constraints:
There will be at most 20000 operations.
1 <= id, t <= 10^6
All strings consist of uppercase, lowercase English letters and digits.
1 <= stationName.length <= 10
Answers within 10^-5 of the actual value will be accepted as correct.




customer with id card == to id gets in at stationName at time t and can only be checked in at one time


third is where we return the avg time to travel from start staion to end station
point A to point B

assumptions:
any call to getAverageTime is valid 

Average time is computed from all the previous trips

All calls to checkin/checkout is consistent

need a data structure to determine that we checked in at start 
and after when i check out, i need to look up the start and then it will point to a check in time

two hashes

just need to know that we started here and ended here and then i can take those times


in getAverageTime i would need to check that the trip is complete, otherwise don't count it.

  id => stationName => arrival time

  id => stationName => set arrival time to None

  start => end => list of travel times

  get average time, i just look it up and take the average.

checkIn(self,1,A,3)
checkOut(self,1,B,9)
checkIn(self,1,A,12)
checkOut(self,1,B,15)

runtime is O(trips) at worst
space is O(stations^2 * trips + customers)
'''

from statistics import mean
class UndergroundSystem:
    def __init__(self):
      self.arrivals = {}
      self.travel_times = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
      self.arrivals[id] = [stationName, t]
      if stationName not in self.travel_times:
        self.travel_times[stationName] = {}
    def checkOut(self, id: int, stationName: str, t: int) -> None:
      arrival = self.arrivals[id]
      if stationName not in self.travel_times[arrival[0]]:
        self.travel_times[arrival[0]][stationName] = [1, t - arrival[1]]
      else:
        num_trips = self.travel_times[arrival[0]][stationName][0] + 1
        total = self.travel_times[arrival[0]][stationName][1]
        duration = t - [arrival][1]
        updated_total = total + duration

        self.travel_times[arrival[0]][stationName] = [num_trips, updated_total]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
      return self.travel_times[startStation][endStation][1] / self.travel_times[startStation][endStation][0]
        # Your UndergroundSystem object will be instantiated and called as such:
        # obj = UndergroundSystem()
        # obj.checkIn(id,stationName,t)
        # obj.checkOut(id,stationName,t)
        # param_3 = obj.getAverageTime(startStation,endStation)


