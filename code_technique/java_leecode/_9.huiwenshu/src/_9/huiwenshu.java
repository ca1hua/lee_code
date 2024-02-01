package _9;
//学习了 java中的键盘输入

import java.util.Scanner;

public class huiwenshu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int count = 0;
        if (num < 0) {
            System.out.println("false");
        } else {

            while (num == 0) {
                num = num /10;
                count++;
            }

        }
    }
}
