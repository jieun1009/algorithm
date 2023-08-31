def solution(id_list, report, k):
    # report = 신고한 사람 - 신고 당한 사람
    # k만큼 신고 당하면 메일 +1, 신고 한사람도 +1
    answer = [0]*len(id_list)
    stop=set()
    report = set(report) #한 사람이 같은 사람 여러번 신고한 것 지움
    report_count = { i:0  for i in id_list}
    
    for i in report:
        person = i.split(" ")
        reporter = person[0]
        reported = person[1]
        
        report_count[reported] += 1 # 신고 누적도 +1

        if report_count[reported] == k:
            stop.add(reported) 
        

            
    for i in report:
        person = i.split(" ")
        reporter = person[0]
        reported = person[1]
        
        if reported in stop: #정지 목록에 있으면
            answer[id_list.index(reporter)] +=1
        
            
    
    return answer