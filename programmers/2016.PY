def solution(a, b):
    # 1/31 - 2/29 - 3/31 -4/30 -5/31 -6/30 -7/31 - 8/31
    # 9/30 - 10/31 - 11/30 - 12/31
    # 1/1 금요일

    month = [31,29,31,30,31,30,31,31,30,31,30,31]

    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    answer = (((sum(month[:a-1]) % 7) + b ) % 7 -1)
    
    return day[answer]