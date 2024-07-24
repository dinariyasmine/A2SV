# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.h = list(range(1, 1001))
        self.infSet = set(range(1, 1001))
        

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.h)
        self.infSet.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.infSet:
            heapq.heappush(self.h,num)
            self.infSet.add(num)
        

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)