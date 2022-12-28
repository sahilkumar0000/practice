package pattern;
import java.util.*;

public class pattern8 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        System.out.println("*\t");
        for(int i =n-1;i>=1;i--){
            for(int j=1;j<=n-1;j++){

                if(i==j){
                    System.out.print("*\t");}
                else{
                    System.out.print("\t");
                }
            }System.out.println();
        }

    }
    
}
