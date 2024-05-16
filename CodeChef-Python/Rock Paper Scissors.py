#include <bits/stdc++.h>
using namespace std;

void solution(){
	// your code goes here
	int n;
	string s;
	cin>>n>>s;
	int ans=1;
	for(int i=1;i<n;i++){
	    if(s[i]==s[i-1]){
	        s[i]='*';
	    }else{
	        ans++;
	    }
	}
    cout<<ans<<"\n";
    
}

int main(){
    int t;
    cin>>t;
    while(t--){
        solution();
    }
    return 0;
}
