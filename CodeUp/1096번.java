import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        int[][] put = new int[num][2];
        
        for(int i = 0; i<num; i++)
        {
            for(int j = 0; j<2; j++)
            {
                put[i][j] = input.nextInt();
            }
        }

        int[][] arr= new int[19][19];
        for(int i = 0; i<19; i++)
        {
            for(int j = 0; j<19; j++)
            {
                arr[i][j] = 0;
            }
        }


        for(int i = 0; i<num; i++)
        {
           arr[put[i][0]-1][put[i][1]-1] = 1;
        }


        for(int i = 0; i<19; i++)
        {
            for(int j = 0; j<19; j++)
            {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
