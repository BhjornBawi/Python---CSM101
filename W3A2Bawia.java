package BhjornBawi;
import java.io.FileReader;
import java.io.IOException;
public class W3A2Bawia {

	public static void main(String[] args) {
	      try (FileReader reader = new FileReader("message.txt")) {
	            int ch;

	            while ((ch = reader.read()) != -1) {
	                System.out.print((char) ch);
	            }

	        } catch (IOException e) {
	            System.out.println("Error reading file");
	        }
	    }
	}
