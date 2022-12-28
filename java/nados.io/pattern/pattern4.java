package pattern;
import java.util.*;

public class pattern4 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n =scn.nextInt();
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(j>=i){
                    System.out.print("*	");
                }else if (j<i){
                    System.out.print("	");
                }
            }
            System.out.println();
        }
    }
}
