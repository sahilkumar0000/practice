public class gcdlcm {
    public static void main(String[] args) {
        int n1=10;
        int n2=20;
        int tn1,tn2;
        tn1=n1;
        tn2=n2;

        while(n1%n2!=0){
            int rem = n1%n2;
            n1=n2;
            n2=rem;
        }
        int gcd =n2;
        int lcm =(tn1*tn2)/gcd;
        System.out.println(lcm);
        System.out.println(gcd);
        
    }
    
}
