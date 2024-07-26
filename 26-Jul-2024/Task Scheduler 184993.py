# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        max_heap = []
        
        for task, freq in count.items():
            heappush(max_heap, (-freq, task))
        
        time = 0
        
        while max_heap:
            temp = []
            i = 0
            while i <= n:
                if max_heap:
                    freq, task = heappop(max_heap)
                    if -freq > 1:
                        temp.append((freq + 1, task))
                time += 1
                if not max_heap and not temp:
                    break
                i += 1
            
            for item in temp:
                heappush(max_heap, item)
        
        return time
