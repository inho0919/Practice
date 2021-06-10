import java.util.Scanner;
public class Main
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);

		int num = input.nextInt();
		
		for(int i = num; i>=1; i--)
		{
		    for(int j = 1; j<=i; j++)
		    {
		        System.out.print(i + " ");   
		    }
		    System.out.println();
		}
	}
}
