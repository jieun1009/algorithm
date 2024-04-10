T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	arr=[]
	for i in range(4):
		arr.append(list(map(str, input().split())))


	answer = 0
	answer_list = set()
	dx = [1,0,-1,0]
	dy = [0,1,0,-1]

	
	def dfs(x,y,value):
		value = value + arr[x][y]
		
		if len(value) ==7:
			answer_list.add(value)
			return
		
		for i in range(4):
			nx = x+ dx[i]
			ny = y+ dy[i]
			if 0<=nx<4 and 0<=ny<4:
				# 내부 안에만 있다면 dfs 호출
				dfs(nx,ny,value)
        
	for i in range(4):
		for  j in range(4):
			dfs(i,j,"") # 시작점
            
	print("#{} {}".format(test_case,len(answer_list)))