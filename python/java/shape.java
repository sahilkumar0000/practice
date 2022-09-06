package javaTesting; 
  
public class shape { 
 
    void draw(){ 
        System.out.println("Drawing shape"); 
    }  
    void erase(){ 
        System.out.println("Erasing shape"); 
    } 
 
}  
class Circle extends shape{ 
     void draw(){ 
        System.out.println("Drawing Circle"); 
    }  
    void erase(){ 
        System.out.println("Erasing Circle"); 
    } 
 
}  class Triangle extends shape{ 
     void draw(){ 
        System.out.println("Drawing Triangle"); 
    }  
    void erase(){ 
        System.out.println("Erasing Triangle"); 
    } 
 
}  
class Square extends shape{ 
     void draw(){ 
        System.out.println("Drawing Square"); 
    }  
    void erase(){ 
        System.out.println("Erasing Square"); 
    }      public static void main(String args[]){ 
 
        shape c = new Circle();         
shape t = new Triangle();        
shape s = new Square();  
        System.out.print("\n"); 
 
        c.draw(); 
        c.erase(); 
        System.out.print("\n"); 
 
        t.draw(); 
        t.erase();         
System.out.print("\n"); 
 
        s.draw(); 
        s.erase(); 
    } 
 
} 
