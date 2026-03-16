class Solution {
    public int findClosest(int x, int y, int z) {

        int temp1=Math.abs(x-z);
        int temp2=Math.abs(y-z);
        if(temp1==temp2){
            return 0;
        }
        if(temp1<temp2){
            return 1;
        }
        return 2;
    }
}