// Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)

import java.util.*;

public class Ass_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char opt = sc.next().charAt(0);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int result;

        if (opt == '+'){
            System.out.println(a+b);
        }
        else if (opt == '-'){
            result = a-b;
            System.out.println(result);
        }
        else if (opt == '/'){
            System.out.println(a/b);
        }
        else if (opt == '*'){
            System.out.println(a*b);
        }
        sc.close();
    }}