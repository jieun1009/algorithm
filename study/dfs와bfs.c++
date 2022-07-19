#include <iostream>
#include<string.h>
#include <queue>
#include <vector>

using namespace std;
#define MAX 1001

int n, m, v;
int graph[MAX][MAX];
int visited[MAX];
queue<int> q;


void dfs(int v) { // 하나의 정점 dfs
    cout << v << " ";

    visited[v] = 1;
    
    for (int i = 1; i <= n; i++) { // 1(첫 정점)부터 최대 정점 갯수만큼 반복
        if (graph[v][i] == 1 && visited[i] == 0) { // 앞으로 방문할 정점이 연결o & 방문x = 탐색
            dfs(i);
        }

    }

}

//dfs : 한 정점을 넣어서 연결된 한 가지의 모든 정점에 방문 -> 다음 가지로 넘어감 (= 깊이 우선)



void bfs(int v) {

    cout << v << " ";
    visited[v] = 1;
 
    q.push(v);

    while (!q.empty()) { //큐가 빌때까지 반복
        v = q.front(); //큐에 있는 정점 대입
        q.pop(); //pop
        
        for (int i = 1; i <= n; i++) { //첫 정점에서 최대 정점까지 반복
            if (graph[v][i] == 1 && visited[i] == 0) { // 현재 정점과 연결 o & 앞으로 갈 정점이 방문 x = 큐에 추가
                q.push(i);
                visited[i] = 1;
                cout << i << " ";

            }
        }
    }

}
// bfs : 한 정점을 넣어서 큐에 연결된 정점들을 넣어 탐색 -> 주변 먼저 탐색 후 자식 노드로 넘어감 (= 너비 우선)

int main() {

    //입력
    cin >> n >> m >> v;

    int a, b;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    // 방문 배열 초기화
    memset(visited, 0, sizeof(visited));

    //dfs
    dfs(v);
    cout << "\n";

    // 방문 배열 초기화
    memset(visited, 0, sizeof(visited));

    bfs(v);


    return 0;
}
