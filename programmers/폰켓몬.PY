def solution(nums):
    # len(nums)//2 # 배열 절반 가져옴 (중복 포함 가능)
    # set(nums) # 배열 중복 추림
    return min(len(nums)/2, len(set(nums)))