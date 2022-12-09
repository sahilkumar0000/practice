public class gcdlcm {
    public static void main(String[] args) {
        int n1=10;
        int n2=20;
        while(n1%n2!=0){
            int rem = n1%n2;
            n1=n2;
            n2=rem;
        }
        System.out.println(n2);
    }
    
}
