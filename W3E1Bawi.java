
package BhjornBawi;

import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class W3E1Bawi {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); 
        int choice;

        do {
            System.out.println("\n===== STUDENT RECORDS SYSTEM =====");
            System.out.println("1. Input New Student Records");
            System.out.println("2. View Student Records");
            System.out.println("3. Exit");
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
                    try (FileReader reader =
                         new FileReader("Bhjorn.txt")) {

                        int ch;

                        System.out.println("\n===== STUDENT RECORDS =====");

                        while ((ch = reader.read()) != -1) {
                            System.out.print((char) ch);
                        }

                    } catch (IOException e) {
                        System.out.println("No student records found.");
                    }
                    break;

                case 3:
                    System.out.println("Exiting program. Thank you!");
                    break;

                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }

        } while (choice != 3);

        input.close();
    }
}
