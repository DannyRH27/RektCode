'''
num line goes from -inf to inf
bunch of segs come in at random

seg = ---- 0-4

seg2 = -- 1-3

seg3 = --- 6-9

is there a way to ensure 4-6 doesn't come in
segs = [[0,4],[5,9],[6,9][8,13],[14,16]]
sort and then update boundaries as i process segs

this will work, but what can i change? Dissect the parts and see where we can optimize

noone cares if you get the optimal answer the first time

go through and test my edge cases and iterate

DO NOT wait for them to prompt you break your algorithm



----
 --
       -----
     ---
             --
             
123456789012345

each seg is a pair of ranges starting from seg[0] up to exclusive of seg[1]

returning how much space is taken up
'''

def spaceTaken(segs):
  segs.sort(key= lambda x: x[0])
  bounds = [segs[0][0],segs[0][1]]
  total = bounds[1] - bounds[0]
  

  for seg in segs:
    lower, upper = seg

    if lower < bounds[1]:
      if upper <= bounds[1]:
        continue
      else:
        total += upper - bounds[1]
        bounds[1] = upper
    else:
      total += upper - lower
      bounds[1] = upper

  return total

assert(spaceTaken([[0,4],[5,9],[2,5],[4,9],[12,15]]) == 12)
assert(spaceTaken([[0,4],[0,9],[1,7],[3,8],[1,1]]) == 9)
assert(spaceTaken([[0,4],[-3,8],[1,7],[3,8],[1,1]]) == 11)