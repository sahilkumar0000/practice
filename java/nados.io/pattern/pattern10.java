package pattern;
import java.util.*;

public class pattern10 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n =scn.nextInt();
        int os =n/2;
        int is = -1;
        for(int i =1;i<=n;i++){
            for(int j =1;j<=os;j++){
                System.out.print("\t");
            }
            System.out.print("*\t");
            for(int k=1;k<=is;k++){
                System.out.print("\t");
            }
            if(i<n && i>1){
                System.out.print("*\t");
            }
            if(i<=n/2){
                is+=2;
                os--;
            }else {
                os++;
                is-=2;
            }
            
            
            System.out.println();
        }
    
     }
    
}
