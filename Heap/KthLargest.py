class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we are going to use built in heapq ds
        # eliminate minimum len(nums)-k elements from min heap and the kth largest wlement will be the min element in the heap
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        # heapify TC will be O(n)
        # pop n-k min elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# TC - O(n-k)logn - remove elements in O(logn) TC
