package com.company;
//Write a Java program to retrieve an element (at a specified index) from a given array list.
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
	    ArrayList<String> adjectives = new ArrayList<String>();

	    adjectives.add("funny");
	    adjectives.add("wonderful");
	    adjectives.add("cute");
	    adjectives.add("happy");

	    System.out.println(adjectives);

	    String first = adjectives.get(0);
	    System.out.println("My first element is:  " + first);
	    String second = adjectives.get(1);
	    System.out.println("My second element is:  " + second);

    }
}
