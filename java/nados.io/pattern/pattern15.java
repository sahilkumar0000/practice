package pattern;
import java.util.*;

public class pattern15 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int sp =n/2;
        int num=1;
        int numn=1;
        int tnum =num;
        for(int i=1; i<=n;i++){
            for(int j=1;j<=sp;j++){
                System.out.print("\t");
            }
            for(int m=1; m<=num;m++){
                System.out.print(tnum+"\t");
                tnum++;
            }
            tnum--;
            for(int q=1;q<=num-1;q++){
                tnum--;
                System.out.print(tnum+"\t");
            }
            // System.out.print(num+"\t");
            // if(i!=1 && i!=n){
            //     System.out.print(num);
            // }
            System.out.println();


            if(i>n/2){
                sp++;
                num--;
                numn-=2;
            }
            else{
                sp--;
                num++;
                numn+=2;
            }
            tnum=num;
        }

    }
    
}
