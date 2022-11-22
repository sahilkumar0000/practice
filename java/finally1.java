import java.io.*;
import java.util.*;
import org.junit.Test;

public class finally1 {

        public void finalize() throws Throwable{
           System.out.println("Object garbage collected.");
        }
        public static void main(String[] args) {
     
           Tester t = new Tester();
           t = null;
           System.gc();
        }
     
}
