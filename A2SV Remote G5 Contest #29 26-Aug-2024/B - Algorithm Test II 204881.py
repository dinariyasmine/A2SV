# Problem: B - Algorithm Test II - https://codeforces.com/gym/544347/problem/B

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DblLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, val):
        new_node = Node(val)
        # if the list is empty the only node whould be the head and the tail
        if self.tail is None:  
            self.head = new_node
            self.tail = new_node
        # else we make it the tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    
    def insert_after(self, node, val):
        new_node = Node(val)
        new_node.prev = node
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node
        return new_node
    
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

class Solution:
    def __init__(self):
        self.dll = DblLL()
        self.positions = {}  # {val: deque of nodes the top should be the first one added}
    
    def insert(self, x, y):
        if y in self.positions and self.positions[y]:
            # insert x after the first occurrence of y
            target_node = self.positions[y][0]
            new_node = self.dll.insert_after(target_node, x)
        else:
            # add x at the end 
            new_node = self.dll.append(x)
        
        # update the dic with the new x
        if x not in self.positions:
            self.positions[x] = deque()
        # we append x anyway in 
        self.positions[x].append(new_node)
    
    def remove(self, w):
        if w in self.positions and self.positions[w]:
            # Remove the first of  the ws
            target_node = self.positions[w].popleft()
            self.dll.remove(target_node)
    
    # turns linked list to a normal python list 
    def convert_to_array(self):
        result = []
        curr = self.dll.head
        
        while curr:
            result.append(curr.val)
            curr = curr.next
            
        return result

def helper(queries):
    
    sol = Solution()
    
    for q in queries:
        input = q.split()
        if input[0] == "insert":
            x = int(input[1])
            y = int(input[2])
            sol.insert(x, y)
            
        elif input[0] == "remove":
            w = int(input[1])
            sol.remove(w)
    
    return sol.convert_to_array()

t = int(input())
queries = []
for _ in range(t):
    queries.append(input())
result = helper(queries)

print(' '.join(map(str, result)))
