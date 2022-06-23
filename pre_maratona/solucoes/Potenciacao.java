package problemas;

import java.util.Scanner;

public class Potenciacao {

    private int a, b;

    public void setA (int number) {
        this.a = number;
    }

    public void setB (int number) {
        this.b = number;
    }

    public int getResult () {
        int result = 1;
        for (int i=0; i < this.b; i++) {
            result *= a;
        }
        return result;
    }
    public static void main(String[] args) {
        
        Potenciacao num = new Potenciacao();

        Scanner input = new Scanner(System.in);

        System.out.print("");
        num.setA(input.nextInt());
        input.nextLine();

        System.out.print("");
        num.setB(input.nextInt());
        input.nextLine();

        input.close();

        System.out.print(num.getResult());
    }
}
