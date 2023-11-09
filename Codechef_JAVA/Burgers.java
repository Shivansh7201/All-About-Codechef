/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Burgers
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
	Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();

		while (testCase-- > 0) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			System.out.println(makeBurger(x, y));
	}
	}
	
	public static int makeBurger(int x, int y) {
		if(x<=y)
		return x;
		else
			return y;
		
	}

}
