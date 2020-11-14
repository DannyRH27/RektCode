import heapq
def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    output = heapq.nlargest(k, nums)
    return output[k-1]
