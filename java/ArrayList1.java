import java.util.ArrayList;
public class ArrayList1{
    public static void main(String[]args){
        ArrayList<Integer> al= new ArrayList<Integer>();
        al.add(34);
        al.add(45);
        ArrayList<String> ai= new ArrayList<String>();
        ai.add("Hello");
        ai.add("World");
        System.out.println(al.get(0));
        System.out.println(ai);
    }
}