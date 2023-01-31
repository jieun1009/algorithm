import sys

n = int(sys.stdin.readline())



card = (list(map(int, sys.stdin.readline().split())))
card.sort()

m = int(sys.stdin.readline())

arr = (list(map(int, sys.stdin.readline().split())))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) //2
        
        if arr[mid] == target:
            print("1", end =' ')
            return 1
            
        elif arr[mid] < target:
            start = mid +1
        else:
            end = mid -1
    print("0", end=" ")
    return 0
    
for i in range(m):
    binary_search(card, arr[i], 0, n-1)
