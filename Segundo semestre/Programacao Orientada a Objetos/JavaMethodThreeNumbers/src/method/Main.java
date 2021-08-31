package method;
import java.util.Scanner;
//Write a Java method to find the smallest number among three numbers

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner myNum = new Scanner(System.in);
        System.out.println("Type a number: ");
        int x = myNum.nextInt();
        System.out.println("Type another number: ");
        int y = myNum.nextInt();
        System.out.println("Type the last number: ");
        int z = myNum.nextInt();
        System.out.println("The smallest number is: " + smallest(x,y,z)+ "\n");

    }
    public static int smallest(int x, int y, int z) {
        return Math.min(Math.min(x,y), z);
    }
}
