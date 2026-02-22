class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        while(k>0){
        int Minvalue=0; //index value
        for(int i=1;i<nums.length;i++){
           if(nums[Minvalue]>nums[i]){
            Minvalue=i;
          
           }}
           nums[Minvalue]*=multiplier;
           k--;
            
        }
        return nums;
    }
}