def kthLargest(arr):
  maxHeap = MaxHeap()
  maxHeap.build(arr)
  kthLargest = [maxHeap.removeMax() for i in range(k)]
  return kthLarges