def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    count = Counter(nums)
    ans = [n for n, occ in count.most_common(k)]
    return ans
