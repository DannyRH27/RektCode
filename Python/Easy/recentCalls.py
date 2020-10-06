class RecentCounter:

  def __init__(self):
    self.arr = deque()

  def ping(self, t: int) -> int:
    self.arr.append(t)
    while self.arr[0] < t-3000:
      self.arr.popleft()
    return len(self.arr)


