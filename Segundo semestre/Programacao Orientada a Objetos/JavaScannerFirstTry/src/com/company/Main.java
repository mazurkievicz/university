package com.company;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.println("Enter a num: ");
        int input = num.nextInt();

        if (input > 0) {
            System.out.println("The num is positive");
        }
        else if (input < 0) {
            System.out.println("The num is negative");
        }
        else {
            System.out.println("The num is 0");
        }

    }
}
