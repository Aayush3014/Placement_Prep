import java.util.Scanner;

// Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.
public class Ass_3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float p = input.nextFloat();
        float r = input.nextFloat();
        float t = input.nextFloat();

        float s = (p * r * t) / 100;
        System.out.println("Simple Interest is " + s);
        input.close();
    }
}