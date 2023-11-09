/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Age_Limit
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int i,T,x,y,a;
		T = sc.nextInt();
		for(i=0;i<T;i++){
		    x = sc.nextInt();
		    y = sc.nextInt();
		    a = sc.nextInt();
		    if(a>=x && a<y){
		        System.out.println("YES");
		   }else{
		        System.out.println("NO");
		   }
		}
	}
}
