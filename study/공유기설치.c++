#include <iostream>
#include <algorithm>
using namespace std;

int n,c;
int house[200000];

void binary_search( int n, int c){
    int ans;
    int right = house[n-1]; //집의 인덱스 위치가 아니라 마지막 집의 거리를 나타내야 함
    int left=0; // 첫집에서 첫집까지의 거리
    while(left<= right){
        int mid = (right+ left)/2; //가운데 집의 위치가 아니라 양끝집 사이/2의 '거리'
        int width;
        int start = 0;
        int cnt=1; // 공유기 갯수
        for(int i=1;i<n;i++){
            width = house[i]-house[start]; // 현재집과 처음집까지 거리 구함
            if(width >= mid){ // mid보다 길다면
                cnt ++;
                start = i; //공유기 설치하고 해당위치에서 다시 탐색
            }
        }

        if(cnt < c){ //공유기 갯수가 적다면 길이 줄여 공유기 늘림
            right = mid-1; // 거리 줄이기
        }
        else if(cnt >= c){ // 공유기 갯수가 많다면 길이 늘려 공유기 줄임
            ans = mid;
            left = mid +1;
        }


    }
    cout << ans;
}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> c;

    for(int i=0;i<n;i++){
        cin >> house[i];
    }

    sort(house, house+n);
    binary_search(n,c);

    
    return 0;
}