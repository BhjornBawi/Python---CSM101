package BhjornBawi;
import java.io.FileWriter;
import java.io.IOException;
public class W3A4Bawi {

	public static void main(String[] args) {
		try (FileWriter writer = new FileWriter ("lastname4.txt", true)) {
			
			writer.write("\n Today I learned FileWriter.");
			System.out.println("New text added.");
		} catch (IOException e) {
			System.out.println("Unable to update file.");
		}

	}

}
