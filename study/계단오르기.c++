#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[300];
int dp[300];
int main(){

    cin >> n;
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }

    dp[0]=0; //출발지
  
    int i=0;
    int total=0;
    while(i<n){
        
        if(i==n-2 || i==n-3){
            total+=max(arr[n-2],arr[n-3]);
            total += arr[n-1];
            break;
        }

        if(arr[i+1]>arr[i+2]){
            total+=arr[i];
            i=i+1;
        }else{
            total+=arr[i];
            i=i+2;
        }
    }

    cout << total;
}