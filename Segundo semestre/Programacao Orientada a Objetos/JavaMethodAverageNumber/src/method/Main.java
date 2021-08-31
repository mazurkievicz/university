package method;
import java.util.Scanner;
//Write a Java method to compute the average of three numbers.

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner myNum = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int x = myNum.nextInt();
        System.out.println("Enter a num: ");
        int y = myNum.nextInt();
        System.out.println("Enter a num: ");
        int z = myNum.nextInt();
        System.out.println("The average between the numbers is: " + average(x, y, z));
    }

    public static int average(int x, int y, int z) {
        return (x + y + z) / 3;
    }
}
