import java.util.*;
import java.lang.*;
import java.io.*;

 class Good_Turn{

    public static void main(String[] args) throws java.lang.Exception {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        for (int i = 0; i < t; i++) {
            int q = s.nextInt();
            int w = s.nextInt();
            if (q + w <= 6) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }
    }
}