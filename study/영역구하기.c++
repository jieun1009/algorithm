#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <cstring>
#include <algorithm>
#define MAX 101
using namespace std;

int n, m, k;
int map[MAX][MAX];
int visited[MAX][MAX] = { 0 };
vector<int> total;
int cnt=0;
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };

void dfs(int x, int y) {
    visited[x][y] = 1;
    cnt++;
    for (int i = 0; i < 4; i++) {

        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || nx >= m || ny < 0 || ny >= n) // 왜 nx >= m ??
            continue;

        if (!visited[nx][ny] && map[nx][ny]==0) {
            dfs(nx, ny);
        }
    }
}

int main() {

    //입력
    cin >> m >> n >> k; // y,x,개수

    int a, b, c, d;

    for (int i = 0; i < k; i++) {
        cin >> a >> b >> c >> d;
        for (int x = a; x < c ; x++) {
            for (int y = b; y < d ; y++) {
                map[y][x] = 1; // x,y가 바뀌면 빈공간 1개가 안읽힘
            }
        }
    }

    memset(visited, 0, sizeof(visited));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == 0 && !visited[i][j]) {
                
                dfs(i, j);
                total.push_back(cnt);
            }
            cnt = 0;
        }
    }

    sort(total.begin(), total.end());

    cout << total.size() << "\n";
    for (int i = 0; i < total.size(); i++)
        cout << total[i] << " ";
    
    return 0;
}