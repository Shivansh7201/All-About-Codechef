import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		for(int i=0;i<n;i++){
		    int a=sc.nextInt();
		    int s=a;
		    int c= 0;
		    int ans;
		    if(a%2==0){
		        ans=0;
		    }else{
		        ans=1;
		    }
		    
		    while(s!=0){
		        s=s/2;
		        c=s%2;
		        ans=ans+c;
		        
		    }
		    if(ans%2==0){
		        System.out.println("EVEN");
		        
		    }else{
		        System.out.println("ODD");
		    }
		}
		

	}
}
