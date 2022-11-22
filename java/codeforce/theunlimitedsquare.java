import java.util.*;
class theunlimitedsquare
{
	public static void main(String[] args) {
	    Scanner scn = new Scanner(System.in);
	    int t = scn.nextInt();
	    int arr[]=new int[t];
	    for(int i=0;i<t;i++){
	        int n =scn.nextInt();
	        arr[i]=n;
	    }
	    for(int j=0; j<t;j++){
	        if(arr[j]%2!=0){
	            System.out.println((arr[j]/2)+1);
	        }
	        else{
	            System.out.println(arr[j]/2);
	        }
	    }
	    }	    
	     
	}