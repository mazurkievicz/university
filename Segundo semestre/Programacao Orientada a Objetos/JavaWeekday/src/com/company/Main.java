package com.company;
//Write a Java program that keeps a number from the user and generates an integer
//between 1 and 7 and displays the name of the weekday.
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner weekDay = new Scanner(System.in);
        System.out.println("Enter a num: ");
        int userInput = weekDay.nextInt();
        System.out.println(getDayName(userInput));

    }

    public static String getDayName(int userInput) {
        String dayName = "";
        switch (userInput) {
            case 1: dayName = "Monday";
                break;
            case 2: dayName = "Tuesday";
                break;
            case 3: dayName = "Wednesday";
                break;
            case 4: dayName = "Thursday";
                break;
            case 5: dayName = "Friday";
                break;
            case 6: dayName = "Saturday";
                break;
            case 7: dayName = "Sunday";
                break;
            default: dayName = "Invalid";
        }

        return dayName;

    }
}
