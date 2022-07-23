#include <iostream>
#include <algorithm>

using namespace std;

int k, n;
int loop[10001];

int main() {

    cin >> k >> n;

    for (int i = 0; i < k; i++) {
        cin >> loop[i];
    }

    sort(loop, loop + k);


    long min = 1; // 1 부터
    long maxi = loop[k - 1]; //802로 나누기

    // 특정 갯수 n에 대한 최대 길이 
    // n보다 많거나 같다면 길이를 늘려서 최대 길이로
    // n보다 적다면 길이를 줄여 갯수를 맞춤

    long result = 0;
    while (min <= maxi) {
        long mid = (maxi + min) / 2;
        long cnt = 0;

        for (int i = 0; i < k; i++) { // 1~802의 mid 값으로 나눔
            cnt += loop[i] / mid; // 각 루프마다 mid로 나눔
        }

        if (cnt >= n) { //길이 늘리기
            min = mid + 1;

            // mid로 나눈값이 n보다 크다면 최솟값을 늘려 
            // 더 길게 만들수 있는지 검사

            //( +1을 할때 )n개를 만들 수 있을때, result는 더 큰값으로 갱신
            result = max(result, mid);
            
        }
        else { //길이 줄이기
            maxi = mid-1;
        }
    }
    // uppor-bound : 해당하는 값을 초과한 인덱스 구함

    cout << result;

    return 0;
}