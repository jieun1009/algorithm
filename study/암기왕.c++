#include <iostream>
#include <algorithm>
using namespace std;
int t,n,m;
int binary_search(int note[],int start,int end, int num){
    while(end >= start){
        int mid = (end+start)/2;
        if(note[mid]==num){
            return 1;
        }else if(note[mid]>num){
            end = mid-1;
        }else if(note[mid]<num){
            start = mid+1;
        }
    }
    return 0;
}
int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
 

    cin >> t;
    for(int j=0;j<t;j++){
        cin >> n;
        int note[n];
        for(int i=0;i<n;i++){
            cin >> note[i];
        }

        sort(note, note+n);
    
        cin >> m;
        int num;
        for(int i=0;i<m;i++){
            cin >> num;
            cout << binary_search(note,0,n-1,num) <<"\n";
        }
    }
    
}