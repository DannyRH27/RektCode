'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
'''

def canAttendMeetings(intervals):
  intervals.sort()
  lower, upper = intervals[0]
  for i in range(1,len(intervals)):
    curr_low, curr_up = intervals[i]
    print(curr_low, lower, curr_up, upper)
    if curr_low >= lower and curr_low < upper:
      return False
    if curr_up >= lower and curr_up <= upper:
      return False
    
    lower, upper = curr_low, curr_up
  
  return True
  # print(intervals)

# assert(canAttendMeetings([[0,30],[5,10],[15,20]]) == False)
# assert(canAttendMeetings([[7,10],[2,4]]) == True)
# assert(canAttendMeetings([[8, 11], [17, 20], [17, 20]]) == False)
assert(canAttendMeetings([[13, 15], [1, 13]]) == True)
