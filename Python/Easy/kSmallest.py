def findKSmallest(lst, k):
    # Write your code here
    minHeap = MinHeap()
    minHeap.buildHeap(lst)
    ans = []
    i = 0
    while i < k:
        ans.append(minHeap.removeMin())
        i += 1
    return ans
