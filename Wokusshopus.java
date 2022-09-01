package workshop5;

import java.util.Scanner;

public class Wokusshopus {
	
	static String toHex(int dec) {
			String str = "";
	        int[] hexNum = new int[45];
	        int i = 0;
	        while (dec != 0) {
	            hexNum[i] = dec % 16;
	            dec = dec / 16;
	            i++;   }
	        for (int j = i - 1; j >= 0; j--) {
	            if (hexNum[j] > 9) str += (char)(55 + hexNum[j]);
	            	else str += hexNum[j];   }
		return str;
	}
	
	static String toOct(int dec) {
		String str = "";
	       int[] octalNum = new int[105];
	        int i = 0;
	        while (dec != 0) {
	            octalNum[i] = dec % 8;
	            dec = dec / 8;
	            i++;   }
	        for (int j = i - 1; j >= 0; j--)
	        	str += octalNum[j];
		return str;
	}
	
	static String toBin(int dec) {
			String str = "";
			if (dec > 15) {
				str += "NOPE"; //sensible message of course ^^'
			} else {
	        int[] binaryNum = new int[8];
	        int i = 0;
	        while (dec > 0) {
	            binaryNum[i] = dec % 2;
	            dec = dec / 2;
	            i++;
	        }
	        for (int j = i - 1; j >= 0; j--)
	            str += binaryNum[j];
			}
	        return str;
	    }

	
	
public static void main(String[] args) {	
	Scanner inp = new Scanner(System.in);
	System.out.println("To convert a decimal to HEX, please type “1” and hit enter.");
	System.out.println("To convert a decimal to OCT, please type “2” and hit enter.");
	System.out.println("To convert a decimal to Binary, please type “3” and hit enter.");
	int chosen_one = inp.nextInt();
	int num_num = inp.nextInt();
	
	
	switch (chosen_one) {
	
	case 3:
		System.out.print(toBin(num_num));
		break;
	case 1:
		System.out.print("Hexadecimal: ");
		System.out.println(toHex(num_num));
		break;
	case 2:
		System.out.print("Octaldecimal: ");
		System.out.println(toOct(num_num));
		break;
	}
	inp.close();
}
}
