#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int card[500001];

int main() {

    ios_base::sync_with_stdio(0); cin.tie(0);
    scanf("%d", &n);

    int tmp;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        card[i] = tmp;
    }

    sort(card, card + n);

    scanf("%d", &m);
    int num;
    for (int i = 0; i < m; i++) {
        scanf("%d", &num);
        int result = upper_bound(card,card+n,num)-lower_bound(card,card+n,num)-card;
        printf("%d ",result);
    }



    return 0;
}
