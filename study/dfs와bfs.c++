#include <iostream>
#include<string.h>
using namespace std;
#define  MAX 1000

int n, m, v = 0;
int cnt = 0;
int graph[1001][1001];
int visited[1001][1001];
int dx[4] = {0,-1,0,1};
int dy[4] = {-1,0,1,0};

int main(){

    //입력
    cin >> n, m, v;


    memset(visited, 0, sizeof(visited));

    int a, b;
    for(int i =0; i<m ; i++){
        cin >> a, b;
        graph[a][b] =1;
        graph[b][a] =1;
    }

    //dfs
    void dfs(int x, int y){
        visited[x][y]=1;

        for(int i=0;i<4;i++){
            int nx = x + bx[i];
            int ny = y + by[i];

            //범위 벗어나는지 확인
            if(nx < 0 || nx > MAX || ny <0 || ny > MAX) 
                continue;

            if(visited[nx][ny] ==0 && graph[nx][ny]==1) { //범위 안 & 연결o & 방문x == 탐색
                dfs[nx][ny];
                cout << ny;
            }



        }

    }


    return 0;
}
