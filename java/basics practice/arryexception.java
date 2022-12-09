public class arryexception {
    public static void main(String[] args) {
        try{
            int[] arr = new int[5];
            arr[5]=30/0;
            System.out.println(arr);


       }
       catch(ArithmeticException e){
        System.out.println(e);
       }
       catch(ArrayIndexOutOfBoundsException e){
        System.out.println(e);
       }
       catch(Exception e){
        System.out.println("parent error");
       }
       System.out.println("sahuk");
    }
    
}
