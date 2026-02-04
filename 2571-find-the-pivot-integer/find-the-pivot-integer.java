class Solution {
    public int pivotInteger(int n) {
        int total=n*(n+1)/2; //finding sum of total from 1 to n
        int x=(int)Math.sqrt(total); 
        if(x*x==total){
            return x;
        }
        return -1;
    }
}