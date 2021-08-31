package com.company;
//Write a Java program to create a new array list, add some colors (string) and print out the collection.

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> colors = new ArrayList<String>();

        colors.add("Blue");
        colors.add("Green");
        colors.add("Orange");

        System.out.println(colors);
    }
}
