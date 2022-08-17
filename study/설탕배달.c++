#include <iostream>
#include <algorithm>
using namespace std;

int n;
int dp[50000];
int main(){

    cin >> n;

    dp[1]=-1;
    dp[2]=-1;
    dp[3]=1;
    dp[4]=-1;
    dp[5]=1;

    for(int i=1;i<=n;i++){
        if(dp[i]==0){
            if(dp[i-5]!=-1){
                dp[i]=dp[i-5]+1;
            }else if(dp[i-3]!=-1){
                dp[i]=dp[i-3]+1;
            }else{
                dp[i]=-1;
            }
            
        }
    }

    cout << dp[n];

}