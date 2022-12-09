public class trycatch{
    public static void main(String[] args) {
        int a=10,b=0,c;
        try{
            c=a/b;
            System.out.println(c);
        }
        catch(Exception e){
            System.out.println("Some error has Occured");
        }
    }
}
