import java.util.Scanner;

public class Main{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        int[] arr = new int[num];
        
        for(int i = 0; i<num; i++)
        {
            arr[i] = input.nextInt();
        }

        for(int i = num-1; i>=0; i--)
        {
            System.out.print(arr[i] + " ");
        }
    }
}
