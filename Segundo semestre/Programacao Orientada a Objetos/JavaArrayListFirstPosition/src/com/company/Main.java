package com.company;
// Write a Java program to insert an element into the array list at the first position.
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
	    ArrayList<String> dogName = new ArrayList<String>();

	    dogName.add("Willie Nelson");
	    dogName.add("Drica");
	    dogName.add("Grizzly");
	    dogName.add("Scooby-doo");
	    dogName.add("Kica");

	    System.out.println(dogName);

	    dogName.add(0, "Nelsinha");
	    dogName.add(0, "Driquinha");
	    System.out.println(dogName);
    }
}
