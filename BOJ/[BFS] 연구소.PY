# 0 빈칸 1 벽 2 바이러스
from collections import deque

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    
bx = [0,1,0,-1]
by = [1,0,-1,0]

q = deque()

def bfs(start):
    q = deque([start])
    