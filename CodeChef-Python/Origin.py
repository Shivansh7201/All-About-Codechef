#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve(){
    int n;
    cin>>n;
    int count=n/9;
    int rem=n%9;
    int ans=count*45+((rem)*(rem+1))/2;
    cout<<ans<<"\n";
}




signed main() {
	// your code goes here
int t;
cin>>t;
while(t--){
    solve();
}
return 0;
}
