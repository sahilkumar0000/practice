package javaTesting; 
import java.util.*; 
public class numreverse { 

     public static void main(String[] args){ 
        Scanner sc=new Scanner(System.in); 
        System.out.println("Enter the number which you want to reverse:- ");         
        int n = sc.nextInt();         
        int temp = n;         
        int reverse = 0; 

        while(temp!=0){
              int a = temp%10;
              reverse = reverse*10 + a;
              temp /= 10; 
        } 
        System.out.print(reverse); 
    } 
} 
