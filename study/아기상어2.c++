#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int bx[8]={-1,0,1,-1,1,-1,0,1};
int by[8]={1,1,1,0,0,-1,-1,-1};
int n,m;
int main(){

    cin >> n >> m;
    queue<pair<int,int>> q;
    vector<vector<int>> map(n, vector<int>(m,0));   

    // 입력

    int tmp;
    for(int i = 0; i < n; i++){
        for(int j =0; j< m; j++){
            cin >> tmp;
            if(tmp==1){
                q.push(make_pair(i,j)); // 상어가 1이면 큐에 삽입(아기상어에서 출발해야 함!)
                map[i][j]=1;
            }
        }
    }

   while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;

        q.pop();
        
        for (int i = 0; i < 8; i++) {
            int nx = x + bx[i];
            int ny = y + by[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;

            if (map[nx][ny] == 0) { // 첫번째 아기 상어
                map[nx][ny] = map[x][y]+1;
                q.push(make_pair(nx,ny));
            }else if (map[nx][ny] > map[x][y]+1) {
                //두번째 아기상어부터 거리 짧으면 갱신
                
                map[nx][ny] = map[x][y]+1;
                q.push(make_pair(nx,ny));
            }
            
        }
   }

   int max_cnt =0;

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            max_cnt = max(max_cnt,map[i][j]);
        }
    }

    cout << max_cnt-1;

    return 0;
}
