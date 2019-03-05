import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

class Solution {


    // IA qui fait plein d'essais au hasard et choisit celle qui donne le meilleur score

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int rows = in.nextInt();
        int cols = in.nextInt();
        int[][] x = new int[2][rows];
        Random random=new Random();


        while (true) {
            for (int i = 0; i < rows; i++) {
                x[0][i] = in.nextInt();
                x[1][i] = in.nextInt();
            }
            int row=random.nextInt(rows-1);
            boolean trouve=false;
            int new_x=0;
            while (!trouve) {
                row = random.nextInt(rows - 1);
                if (x[0][row] + 1 < x[1][row]) {
                    if (x[0][row]+2==x[1][row]){
                        new_x = x[0][row]+1;
                    } else {
                        new_x = x[0][row] + 1 + random.nextInt(x[1][row] - x[0][row] - 2);
                    }
                    trouve = true;
                }
            }
            System.out.printf("%d %d%n", row, new_x);


        }

    }
}
