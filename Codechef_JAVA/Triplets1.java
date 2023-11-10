import java.util.Arrays;

class Triplets1{
public static boolean isTriplets(int[] arr){

int n= arr.length;

for(int i=0; i<n ; i++){
    arr[i]= arr[i] + arr[i];

}
Arrays.sort(arr);
 for(int i=n-1 ;i>=2; i++){
  int left=0;
  int right =i - 1;

  while( left < right){
    if(arr[left] + arr[right] == arr [i]){
        return true;

    }else if(arr[left] + arr[right] < arr [i]){
        left++;
    }else{
        right++;
    }
  }
 }
return false;
}
public static void main(String[] args) {
    int[] arr = {3, 1, 4, 6, 5};
    boolean result = isTriplets(arr);
    System.out.println(result);

}
}


