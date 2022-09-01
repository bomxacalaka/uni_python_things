import java.util.InputMismatchException;

/**
 * Created on 1/21/17.
 */
public class WordSearchSolver1 {

    private int currentChar;
    private char word[];

    public boolean wordExists(char board[][], String word) {

        this.word = new char[word.length()];
        currentChar = 0;

        for (int a = 0; a < word.length(); a++) {
            word.getChars(0, word.length(), this.word, 0);
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (this.word.length != 0 && board[i][j] == this.word[currentChar]) {
                    if (this.word.length == 1) {
                        return true;
                    }

                    if (letterExists(board, i, j, this.word[++currentChar], "N")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "NE")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "E")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "SE")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "S")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "SW")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "W")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    if (letterExists(board, i, j, this.word[++currentChar], "NW")) {
                        System.out.print(this.word);
                        System.out.print(" "+i+" ");
                        System.out.println(j);
                        return true;
                    }
                    currentChar = 0;
                    continue;
                }
            }
        }
        return false;
    }

    public boolean letterExists(char board[][], int i, int j, char letter, String direction) {

        if (i < 0 || i > board.length || j < 0 || j > board.length) {
            throw new IndexOutOfBoundsException("Unable to search for letter " + letter + " with coordinates (" + i + ", " + j + ")");
        }

        currentChar++;//advance search character to next letter in word

        if (i - 1 >= 0 && board[i - 1][j] == letter && direction.equals("N")) { //search N
            if (currentChar == word.length)
                return true;
            return letterExists(board, i - 1, j, word[currentChar], "N");
        } else if (i - 1 >= 0 && j + 1 < board[i].length && board[i - 1][j + 1] == letter && direction.equals("NE")) {//search NE
            if (currentChar == word.length)
                return true;
            return letterExists(board, i - 1, j + 1, word[currentChar], "NE");
        } else if (j + 1 < board[i].length && board[i][j + 1] == letter && direction.equals("E")) { //search E
            if (currentChar == word.length)
                return true;
            return letterExists(board, i, j + 1, word[currentChar], "E");
        } else if (i + 1 < board.length && j + 1 < board[i + 1].length && board[i + 1][j + 1] == letter && direction.equals("SE")) { //search SE
            if (currentChar == word.length)
                return true;
            return letterExists(board, i + 1, j + 1, word[currentChar], "SE");
        } else if (i + 1 < board.length && board[i + 1][j] == letter && direction.equals("S")) {//search S
            if (currentChar == word.length)
                return true;
            return letterExists(board, i + 1, j, word[currentChar], "S");
        } else if (i + 1 < board.length && j - 1 >= 0 && board[i + 1][j - 1] == letter && direction.equals("SW")) { //search SW
            if (currentChar == word.length)
                return true;
            return letterExists(board, i + 1, j - 1, word[currentChar], "SW");
        } else if (j - 1 >= 0 && board[i][j - 1] == letter && direction.equals("W")) { //search W
            if (currentChar == word.length)
                return true;
            return letterExists(board, i, j - 1, word[currentChar], "W");
        } else if (j - 1 >= 0 && i - 1 >= 0 && board[i - 1][j - 1] == letter && direction.equals("NW")) { //search NW
            if (currentChar == word.length)
                return true;
            return letterExists(board, i - 1, j - 1, word[currentChar], "NW");
        }
        return false;
    }

    public static void main(String[] args) {
        /*char row1[] = {'a', 'm', 'e', 'r' };
        char row2[] = {'m', 'i', 'z', 'g' };
        char row3[] = {'k', 'l', 'b', 'f' };
        char row4[] = {'s', 't', 'o', 'c' };
        char row5[] = {'b', 'a', 'y', 'a' };

        char board[][] = new char[5][4];
        board[0] = row1;
        board[1] = row2;
        board[2] = row3;
        board[3] = row4;
        board[4] = row5;*/

        char[][] board = {
            {'S', 'L', 'E', 'F', 'F', 'E', 'D', 'E', 'R', 'A', 'L', 'F', 'D', 'E'},
            {'C', 'U', 'Y', 'A', 'O', 'E', 'T', 'L', 'P', 'M', 'M', 'R', 'O', 'L'},
            {'A', 'F', 'D', 'G', 'T', 'E', 'I', 'R', 'O', 'T', 'I', 'E', 'T', 'U'},
            {'T', 'H', 'E', 'I', 'D', 'H', 'A', 'S', 'I', 'N', 'D', 'Q', 'T', 'F'},
            {'T', 'T', 'N', 'E', 'E', 'I', 'R', 'D', 'S', 'A', 'S', 'U', 'M', 'R'},
            {'E', 'U', 'E', 'I', 'I', 'A', 'A', 'L', 'E', 'T', 'A', 'E', 'D', 'E'},
            {'R', 'O', 'Y', 'C', 'R', 'O', 'D', 'E', 'D', 'R', 'G', 'N', 'M', 'D'},
            {'E', 'Y', 'R', 'E', 'R', 'I', 'E', 'P', 'A', 'O', 'R', 'T', 'E', 'N'},
            {'D', 'P', 'R', 'B', 'A', 'C', 'F', 'R', 'T', 'P', 'U', 'N', 'E', 'O'},
            {'E', 'E', 'A', 'I', 'M', 'R', 'I', 'L', 'N', 'M', 'E', 'R', 'T', 'W'},
            {'D', 'O', 'F', 'D', 'I', 'E', 'N', 'H', 'E', 'I', 'S', 'O', 'A', 'A'},
            {'E', 'T', 'E', 'E', 'U', 'D', 'I', 'T', 'I', 'S', 'O', 'S', 'E', 'I'},
            {'N', 'D', 'I', 'S', 'T', 'I', 'N', 'C', 'T', 'E', 'M', 'A', 'D', 'I'},
            {'T', 'U', 'T', 'R', 'T', 'E', 'W', 'D', 'H', 'A', 'E', 'I', 'R', 'T'},
    };

        WordSearchSolver1 puzzle = new WordSearchSolver1();
        String wordsRaw = "GRUESOME	MARRIED	SCATTERED	YOUTHFUL	FEDERAL UNITED		POISED		WONDERFUL	DISTINCT	ABROAD	IMPORTANT	FREQUENT	WOLVES	POCKETS	ADVANCED";
String[] words = wordsRaw.split("\\s+");
for(String l : words){
        puzzle.wordExists(board, l);

    
    }
    }
}


/*
public class WordSearchSolver {
	
	public static void main(String[] args) {
		
		char[][] grid = {
				{'S', 'L', 'E', 'F', 'F', 'E', 'D', 'E', 'R', 'A', 'L', 'F', 'D', 'E'},
				{'C', 'U', 'Y', 'A', 'O', 'E', 'T', 'L', 'P', 'M', 'M', 'R', 'O', 'L'},
				{'A', 'F', 'D', 'G', 'T', 'E', 'I', 'R', 'O', 'T', 'I', 'E', 'T', 'U'},
				{'T', 'H', 'E', 'I', 'D', 'H', 'A', 'S', 'I', 'N', 'D', 'Q', 'T', 'F'},
				{'T', 'T', 'N', 'E', 'E', 'I', 'R', 'D', 'S', 'A', 'S', 'U', 'M', 'R'},
				{'E', 'U', 'E', 'I', 'I', 'A', 'A', 'L', 'E', 'T', 'A', 'E', 'D', 'E'},
				{'R', 'O', 'Y', 'C', 'R', 'O', 'D', 'E', 'D', 'R', 'G', 'N', 'M', 'D'},
				{'E', 'Y', 'R', 'E', 'R', 'I', 'E', 'P', 'A', 'O', 'R', 'T', 'E', 'N'},
				{'D', 'P', 'R', 'B', 'A', 'C', 'F', 'R', 'T', 'P', 'U', 'N', 'E', 'O'},
				{'E', 'E', 'A', 'I', 'M', 'R', 'I', 'L', 'N', 'M', 'E', 'R', 'T', 'W'},
				{'D', 'O', 'F', 'D', 'I', 'E', 'N', 'H', 'E', 'I', 'S', 'O', 'A', 'A'},
				{'E', 'T', 'E', 'E', 'U', 'D', 'I', 'T', 'I', 'S', 'O', 'S', 'E', 'I'},
				{'N', 'D', 'I', 'S', 'T', 'I', 'N', 'C', 'T', 'E', 'M', 'A', 'D', 'I'},
				{'T', 'U', 'T', 'R', 'T', 'E', 'W', 'D', 'H', 'A', 'E', 'I', 'R', 'T'},
		};
		
	}

}*/