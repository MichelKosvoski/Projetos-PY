package Aplication;

import entities.Rectangle;
import java.util.Locale;
import java.util.Scanner;

public class program {

	public static void main(String[] args) {
		// Calcular a area do Retangulo	
			Locale.setDefault(Locale.US);
			Scanner sc = new Scanner(System.in);
			
			Rectangle x, y;
			x = new Rectangle();
			y = new Rectangle();
			
			System.out.println("Enter Rectangle width and height");
			rect.width= sc.nextDouble();
			rect.height = sc.nextDouble();
			
			System.out.printf("AREA = %.2f%n", rect.area());
			System.out.printf("PERIMETER = %.2f%n", rect.perimeter());
			System.out.printf("DIAGONAL = %.2f%n", rect.diagonal());
			
	}

}
