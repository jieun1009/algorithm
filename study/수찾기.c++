#include <iostream>
#include <algorithm>
using namespace std;
int n, m;
int A[100001];
int binarySearch(int A[], int start, int end, int num) {



    // 중간값과 num 비교
    while (end >= start) { //역전 방지
        int mid = (end + start) / 2;

        if (A[start] > num || A[end] < num) {
            return 0;
        }
        else if (A[mid] == num || A[start] == num || A[end] == num) {
            return 1;
        }
        else if (A[mid] > num) {
            end = mid - 1;

        }
        else if (A[mid] < num) {
            start = mid + 1;

        }
    }


    return 0;
}

int main() {

    ios_base::sync_with_stdio(0); cin.tie(0);

    //입력
    scanf("%d", &n);

    int tmp;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        A[i] = tmp;
    }

    sort(A, A + n); //배열 정렬

    scanf("%d", &m);
    int num;
    for (int i = 0; i < m; i++) {
        scanf("%d", &num);
        printf("%d\n", binarySearch(A, 0, n - 1, num));
    }

    return 0;
}
