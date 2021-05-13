import java.util.Scanner;

public class Main{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        int[] arr = new int[num];
        int[] student = new int[23];
        
        for(int i = 0; i<num; i++)
        {
            arr[i] = input.nextInt();
        }

        for(int i = 0; i<23; i++)
        {
            student[i] = 0;
        }

        for(int i = 0; i<num; i++)
        {
            student[arr[i]-1] = student[arr[i]-1] + 1;
        }

        for(int i = 0; i<23; i++)
        {
            System.out.print(student[i] + " ");
        }
    }
}
