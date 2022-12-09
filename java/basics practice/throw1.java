public class throw1 {
    static int divide(int a, int b){
        if (b==0){
            throw new ArithmeticException("divisor is 0");
        }
        else{
            int c;
            c= a/b;
            return c;
        }
    }
    public static void main(String[] args) {
        try{

        
        int c = divide(2,0);
        System.out.println(c);
        }
        catch(ArithmeticException e){
            System.out.println("Exception");
        }
        
    }
}
