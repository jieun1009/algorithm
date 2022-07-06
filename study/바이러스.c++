#include <iostream>
#include <cstring>
using namespace std;
#define MAX 101

int n,m;
int computer[MAX][MAX];
int visited[MAX];
int cnt=0;

void dfs(int v){
    visited[v]=1;

    for(int i=1;i<=n;i++){
        if(computer[v][i]==1 && visited[i]==0){
            cnt++;
            dfs(i);
        }
    }

}


int main(){

    //입력
    cin >> n;
    cin >> m;

    int a,b;
    for(int i=0;i<m;i++){
        cin >> a >> b;
        computer[a][b]=1;
        computer[b][a]=1;
    }

    memset(visited,0,sizeof(visited));

    //dfs : 1번 컴퓨터가 바이러스 걸릴때
    dfs(1);

    return 0;
}