#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[300];
int dp[300];
int main() {

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int total = 0;
    dp[0] = arr[0]; //0번 계단까지 올랐을때 최댓값
    dp[1] = arr[0] + arr[1];
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]);

    for (int i = 3; i < n;i++) {

        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
    }


    cout <<  dp[n-1];
}