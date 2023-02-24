// To find out whether the given String is Palindrome or not.

public class Ass_8 {
    public static void main(String[] args) {
        String s = "Hello";
        String newstr = "";
        char ch;
        for (int i = 0; i < s.length(); i++) {
            ch = s.charAt(i);
            newstr = ch + newstr;
        }
        System.out.println(newstr);
    }
}
