# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        #in deg dic
        deg = {i: 0 for i in range(numCourses)}
        
        
        for a, b in prerequisites:
            graph[b].append(a)
            deg[a] += 1
        
        # courses with no preq
        dq = deque([course for course in deg if deg[course] == 0])
        answer = []
        
        while dq:
            course = dq.popleft()
            answer.append(course)
            
            
            for next_course in graph[course]:
                deg[next_course] -= 1
                
                if deg[next_course] == 0:
                    dq.append(next_course)
        
        
        if len(answer) == numCourses:
            return answer
        else:
            return []
