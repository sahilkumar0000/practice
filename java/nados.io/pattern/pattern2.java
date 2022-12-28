package pattern;
import java.util.*;
public class pattern2 {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        for(int i=1;i<=n;i++){
            for(int j =n;j<=0;j--){
                System.out.print("*	");
            }
            System.out.println();
        }

    }
}