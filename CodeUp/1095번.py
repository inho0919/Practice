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

        for(int i = 0; i<num; i++)
        {
            for(int j = 0; j<num; j++)
            {
                if(arr[i] < arr[j])
                {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        System.out.print(arr[0]);    
        
    }
}
