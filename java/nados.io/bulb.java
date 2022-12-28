public class bulb {
    public static void main(String[] args) {
        int n = 6;
        boolean[] arr=new boolean[n-1];
        for(int i =0;i>n;i++){
            arr[i]=true;

            }
        for(int j=2;j<=n;j++){
            for(int k=1;k<n/j;k++){
                arr[k*j]=false;
                }

        }
        System.out.println(java.util.Arrays.toString(arr));
    }
    
}
