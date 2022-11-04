import java.util.Scanner;
import java.time.Period;
public class hh {

    public static void main(String[]args){
        // Scanner sc = new Scanner(System.in);
        // System.out.println("enter your \nname");
        // String name= sc.next();
        // System.out.println(name);
        // String i = "100";
        // int x = Integer.parseInt(i);
        // System.out.println(x);
        // System.out.println(x+100);
        // System.out.println(i+100);
        String age = "P21Y12M31D";
        Period p = Period.parse(age);
        System.out.println(p.getYears()+ "Year\n" + p.getMonths()+"month\n" +p.getDays()+"days");
    }
    
}
