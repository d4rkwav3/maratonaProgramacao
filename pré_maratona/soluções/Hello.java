package problemas;

import java.util.Scanner;

public class Hello {

	private String userName;

	public void setUserName (String nome) {
		this.userName = nome;
	}

	public String getUserName () {
		return this.userName;
	}

	public static void main (String[] args) {

		Hello oi = new Hello();
		
		Scanner input = new Scanner(System.in);

		System.out.print("");
		oi.setUserName(input.nextLine());
		input.close();
		
		System.out.print("Hello, " + oi.getUserName());

	}
}
