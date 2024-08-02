from itertools import permutations

arr = ["A","A","A","A","A","A","A","A","B","B"]
result = permutations(arr,10)
# result = sorted(list(result))

print(list(result)[22])
