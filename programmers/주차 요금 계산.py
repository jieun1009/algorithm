import math
def time_calc(endtime, starttime):
    endhour = int(endtime.split(":")[0])
    endmin = int(endtime.split(":")[1])
    starthour = int(starttime.split(":")[0])
    startmin = int(starttime.split(":")[1])
    return (60*endhour+endmin) - (60*starthour+startmin)
    
def solution(fees, records):
    answer = []

    default_time = fees[0]
    default_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    
    recorddict = {} # 차량 출입 정보 기록
    time_record = {} # 자동차별 주차시간 기록
    # 각 자동차별로 시간 계산
    for i in records:
        rec = i.split(" ")
        if rec[1] in recorddict.keys(): # 이미 dict에 있다면 시간 계산 and 출차
            time = time_calc(rec[0], recorddict[rec[1]])
            if rec[1] in time_record.keys():
                time_record[rec[1]] += time
            else:
                time_record[rec[1]] = time
            # dict에서 삭제
            del recorddict[rec[1]]
        else:# 입차
            recorddict[rec[1]] = rec[0]   
    # 출차 안한경우
    if len(recorddict)>=1:
        for key, value in recorddict.items():
            time = time_calc("23:59",value)
            if key in time_record.keys():
                time_record[key] += time
            else:
                time_record[key] = time
                
    # 각 자동차별로 요금 계산
    for key,value in time_record.items():
        if value>=default_time:
            time_record[key] = int(default_fee + per_fee * math.ceil(((value-default_time)/per_time)))
        else:
            time_record[key] = int(default_fee)
    
    car_num = sorted([key for key, value in time_record.items()])
    answer = [time_record[key] for key in car_num ]
    

    return answer