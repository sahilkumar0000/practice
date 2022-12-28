package pattern;
import java.util.*;

public class pattern17 {
    public static void main (String[] args) {
        Scanner sc =new Scanner(System.in);
        int n =sc.nextInt();
        int st=2;
        System.out.println("*\t");

        for(int i=1;i<=n;i++){
            for(int j =1; j<=n/2;j++){
                if(i==(n/2)+1){
                    System.out.print("*\t");
                }else{
                    System.out.print("\t");
                }
                }
            for(int k=1;k<=st;k++){
                System.out.print("*\t");
            }System.out.println();
            if(i<=n/2){
                st++;
            }else{st--;}
            }
            
        }
    
}
