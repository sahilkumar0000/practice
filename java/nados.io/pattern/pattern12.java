package pattern;
import java.util.*;

public class pattern12 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int l1 =0;
        int l2 =1;
        int c;
        for(int i =0;i<n;i++){
            for(int j =1;j<=i+1;j++){
                System.out.print(l1+"\t");
               c=l1+l2;
               l1=l2;
               l2=c;
            }System.out.println();
        }


    }
    
}
