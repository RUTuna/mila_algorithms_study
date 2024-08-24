import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline().strip() + ' '
    stack = []
    result = []
    
    for char in string:
        if char == ' ':
            while stack:
                result.append(stack.pop())
            result.append(' ')
        else :
            stack.append(char)
            
    print(''.join(result))