package BhjornBawi;

import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

public class W3E1seach_Bawi {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); 
        int choice;

        do {
            System.out.println("\n===== STUDENT RECORDS SYSTEM =====");
            System.out.println("1. Input New Student Records");
            System.out.println("2. View Student Records");
            System.out.println("3. Search Student Records");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            choice = input.nextInt();
            input.nextLine();

            switch (choice) {

                case 1:
                    try (FileWriter writer =
                         new FileWriter("Bhjorn.txt", true)) {

                        System.out.print("Enter First Name: ");
                        String firstName = input.nextLine();

                        System.out.print("Enter Last Name: ");
                        String lastName = input.nextLine();

                        System.out.print("Enter Course: ");
                        String course = input.nextLine();

                        writer.write("First Name: " + firstName + "\n");
                        writer.write("Last Name: " + lastName + "\n");
                        writer.write("Course: " + course + "\n");
                        writer.write("-------------------------\n");

                        System.out.println("Student record successfully saved!");

                    } catch (IOException e) {
                        System.out.println("Error writing to file.");
                    }	
                    break;

                case 2:
                    try (BufferedReader reader = new BufferedReader( new FileReader("Bhjorn.txt"))) {

                       String line;

                        System.out.println("\n===== STUDENT RECORDS =====");

                        while ((line = reader.readLine()) != null) {
                            System.out.println(line);
                        }

                    } catch (IOException e) {
                        System.out.println("No student records found.");
                    }
                    break;

                case 3:
                	System.out.print("Enter First Name: ");
                    String search = input.nextLine();

                    boolean found = false;
                    
                    try (BufferedReader reader =
                            new BufferedReader(new FileReader("Bhjorn.txt"))) {

                        String line;
                        String record = "";

                        while ((line = reader.readLine()) != null) {
                            record += line + "\n";

                            if (line.startsWith("----------------")) {

                                if (record.toLowerCase().contains(
                                        "first name: " + search.toLowerCase())) {

                                    System.out.println("\n" + record);
                                    found = true;
                                }

                                record = "";
                            }
                        }

                        if (!found) {
                            System.out.println("Student not found.");
                        }

                    } catch (IOException e) {
                        System.out.println("Error searching file.");
                    }
                    break;
                    
                case 4:
                	System.out.println("Thank you and I love you");
                	break;
                	
                	default:
                		System.out.println("Invalid Choice");
            }
            
        }		while (choice !=4);	
        		input.close();
    }
}
            
                	
                