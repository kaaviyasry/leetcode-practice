class Solution {
    public int[] leftRightDifference(int[] nums) {
        int leftSum=0;
        int total=0;

       for(int i=0;i<nums.length;i++){
        total+=nums[i];
       }
       int ans[]=new int[nums.length];

       for(int i=0;i<nums.length;i++){
        int rightSum=total-nums[i]-leftSum;
        ans[i]=Math.abs(rightSum-leftSum);
        leftSum+=nums[i];

       }
       return ans;

    }
}