#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int tree[1000000];
void max_tree(int tree[], int left, int right, int m) {
    int ans = 0;
    // tree[start] 즉, 가장 작은 나무의 위치부터가 아니라 0부터 시작해야 함

    while (left <= right) {
        int mid = (left + right) / 2; // 자르는 위치
        long long cnt = 0;
        for (int i = 0; i < n; i++) {
            if (mid < tree[i]) // 같으면 자를수 있는게 없음
                cnt += (tree[i] - mid);

        }

        if (cnt < m) {
            right = mid - 1;
        }
        else if (cnt > m) {
            if (ans < mid) {
                ans = mid; // cnt ==m인 경우가 없으면 이 경우의 mid가 답이 되기때문
                // 적어도 m개 이상은 가져가야 하니까
            }
            left = mid + 1;
        }
        else if (cnt == m) {
             ans = mid;
             break;
        }

    }
    cout << ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    int num;
    int maxi = 0;
    for (int i = 0; i < n; i++) {
        cin >> num;
        maxi = max(maxi, num);
        tree[i] = num;
    }


    max_tree(tree, 0, maxi, m);

    return 0;
}