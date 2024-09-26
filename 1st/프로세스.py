from collections import deque

def solution(priorities, location):
    priority = deque(priorities)
    result = 0
    
    while priority:
        front = priority.popleft()
        if not priority or front >= max(priority):
            result += 1
            if location == 0:
                break
            
        else:
            priority.append(front)
        
        location = (location-1 + len(priority)) % len(priority)
        
    return result