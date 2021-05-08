class Solution 
{
    public String solution(String s) 
    {
        String answer = "";
        char[] arr = s.toCharArray();
        
        int length = arr.length;
        
        if(length%2 == 0)
        {
            for(int i = (length/2-1); i<=length/2; i++)
            {
                answer = answer + Character.toString(arr[i]);
            }
        }
        else
        {
            answer = Character.toString(arr[length/2]); 
        }
        
        return answer;
    }
}
