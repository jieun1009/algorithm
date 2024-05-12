from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    comb_result = combinations(arr,3)
    result_list = list()
    for i in comb_result:
        result_sum = sum(i)
        if result_sum not in result_list:
            result_list.append(result_sum)

    result_list.sort()


    print("#{} {}".format(test_case, result_list[-5]))