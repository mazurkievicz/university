package com.company;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in1 = new Scanner(System.in);
        System.out.println("Enter a num: ");
        int myInput = in1.nextInt();

        Scanner in2 = new Scanner(System.in);
        System.out.println("Enter a num: ");
        int myInput2 = in2.nextInt();

        Scanner in3 = new Scanner(System.in);
        System.out.println("Enter a num: ");
        int myInput3 = in3.nextInt();

        if (myInput > myInput2 && myInput > myInput3) {
            System.out.println("Num 1 is the biggest");

        }
        else if (myInput2 > myInput && myInput2 > myInput3) {
            System.out.println("Num 2 is the biggest");
        }
        else {
            System.out.println("Num 3 is the biggest");
        }

    }
}
