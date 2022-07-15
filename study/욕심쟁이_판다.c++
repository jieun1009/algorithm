#include <iostream>
#include <cstring>
#define MAX 501
using namespace std;

int n;
int soop[MAX][MAX];
int visited[MAX][MAX];

int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
int cnt;
void dfs(int x, int y){
    visited[x][y]=1;
    cnt ++;
    for(int i=0;i<4;i++){

        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx < 0 || nx > n || ny < 0 || ny > n) // 범위 확인
            continue;

        if(!visited[nx][ny] && soop[x][y] < soop[nx][ny]){
            // 방문 안하고 이전 지역보다 대나무 많은 지역 탐색
            dfs(nx,ny);
        }

    }

}

int main(){

    // 입력
    cin >> n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin >> soop[i][j];
        }
    }

    int max_cnt =0;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            memset(visited,0,sizeof(visited));
            cnt =0;
            dfs(i,j); 
            // 각 칸마다 dfs 돌려서 가장 큰 cnt로 변경
            max_cnt = max(max_cnt,cnt);
        }
    }

    cout << max_cnt;

    return 0;
}