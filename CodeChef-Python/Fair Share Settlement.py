#include <iostream>
#include<cmath>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--){
	    int n,k;
	    cin>>n>>k;
	    
	    int share = floor(n/(k+1));
	    
	    int final = n-share * k ;
	    cout<< final <<endl;
	}
	return 0;
}
