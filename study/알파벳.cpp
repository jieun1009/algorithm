#include <iostream>
#include <cstring>
#define MAX 20

using namespace std;

int r, c;
char graph[MAX][MAX];
// int visited[MAX][MAX]; //지나간 칸 기록 -> 사용할 필요 없음
int visited_alpha[26]={0}; //중복 알파벳 기록
int cnt; //dfs 방문 횟수
int max_cnt = 0;

int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };

void dfs(int x, int y, int cnt) {

    max_cnt = max(max_cnt, cnt); // 현재까지 방문한 횟수와 기록된 max 횟수 비교

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        int ascii_num = (int)graph[nx][ny]-65; //전역변수로 생성x

        if (nx < 0 || nx >= r || ny < 0 || ny >= c) //범위 체크
            continue;

        if (visited_alpha[ascii_num] == 0) {

            visited_alpha[ascii_num] = 1; // 알파벳 방문 
            dfs(nx, ny, cnt + 1);

            visited_alpha[ascii_num] = 0; // 방문 취소, 상하좌우 중 다른 길도 찾아봐야 하므로!
        }
    }


}

int main() {

    //입력
    cin >> r >> c;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c ; j++) {
            cin >> graph[i][j];
        }
    }


    int ascii_num = (int)graph[0][0]-65;
    visited_alpha[ascii_num] = 1;

    dfs(0, 0, 1); //1행 1열부터 탐색

    cout << max_cnt;

    return 0;
}