package pattern;
import java.util.*;

public class pattern16 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int sp = (2*n)-3;
        for(int i=1; i<=n;i++){
            for(int k=1;k<=i;k++){
                System.out.print(k+"\t");
            }
            for(int m=1;m<=sp;m++){
                System.out.print("\t");
            }
            for(int l=i;l>=1;l--){
                if(l!=n){
                System.out.print(l+"\t");}
            }
            System.out.println();
            if(sp!=0){
                sp-=2;
            }
        }
    
       }
}
