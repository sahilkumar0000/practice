public class throws1 {
    static  int divide(int a, int b) throws ArithmeticException {
        int c=a/b;
        return c;
    }
    public static void main(String[] args) {

        int c=divide(9,0);
        System.out.println(c);
    }
    
}
