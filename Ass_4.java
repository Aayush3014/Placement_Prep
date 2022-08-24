// Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)

import java.util.*;
public class Ass_4{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt();
        int num2 = input.nextInt();

        String s = input.nextLine();
        if(s=="+"){
            System.out.println(num1+num2);
        }
        if(s == "-"){
            System.out.println(num1-num2);

        }
        if (s=="*"){
            System.out.println(num1*num2);
        }
        if (s=="/"){
            System.out.println(num1/num2);
        }
        // else{
        //     System.out.println("Entered operation is invalid");
        input.close();
        }
    
    }

// }