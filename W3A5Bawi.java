package BhjornBawi;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
public class W3A5Bawi {

	public static void main(String[] args) {
		try (FileReader reader = new FileReader ("input.txt");
				FileWriter writer = new FileWriter ("uppercase.txt");
				){
			int ch;
			while ((ch = reader.read ()) != -1) {
				char letter = (char) ch;
				writer.write(Character.toUpperCase (letter));
				
			}
			System.out.println("UpperCase file created.");
		}catch (IOException e) {
			System.out.println("File proccessing error");
		}

	}

}
