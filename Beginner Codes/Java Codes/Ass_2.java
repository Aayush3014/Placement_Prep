import java.util.Scanner;

// Take name as input and print a greeting message for that particular name.

public class Ass_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s = input.nextLine();
        System.out.println("Hello " + s + " broo");
        input.close();
    }
}
