import java.util.Scanner;

public class SelectionSort
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        int[] arr = new int[num];

        for(int i = 0; i<num; i++)
        {
            arr[i] = input.nextInt();
        }

        for(int i = 0; i<num-1; i++)
        {
            int maxNum = i;
            for(int j = i+1; j<num; j++)
            {
                if(arr[j] < arr[maxNum])
                {
                    maxNum = j;    
                }
                int temp = arr[i];
                arr[i] = arr[maxNum];
                arr[maxNum] = temp;
            }
        }

        for(int i = 0; i<num; i++)
        {
            System.out.print(arr[i] + " ");
        }
	}
}