import java.util.Scanner;

// To calculate Fibonacci Series up to n numbers.

public class Ass_7 {
    public static void main(String[] args) {
        int a = 0;
        int b = 1;
        int c;

        int count_loop = 1;
        Scanner input = new Scanner(System.in);
        int count = input.nextInt();
        System.out.println(a);
        System.out.println(b);
        while (count_loop != count-1) {
            c = a + b;
            
            System.out.println(c);
            a = b;
            b = c;
            count_loop++;
        }
        input.close();
    }
}
