import java.util.Scanner;

// Input currency in rupees and output in USD.


public class Ass_6 {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    double curr_rs = input.nextDouble();
    System.out.println("The currency in USD is "+curr_rs*70);        
    input.close();
    }
}
