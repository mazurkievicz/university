package com.company;
//Write a Java program to iterate through all elements in a array list.
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
	    ArrayList<String> names = new ArrayList<String>();

	    names.add("Yasmin");
	    names.add("Teemo");
	    names.add("Zed");

	for (String elements : names) {
	    System.out.println(elements);
    }
    }
}
