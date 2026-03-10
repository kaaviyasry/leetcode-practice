class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){// next number of i
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j} ;// return the new array with ans i and j

                } 

            }
        }
        return new int[]{}; //if target not found it returns empty arr
    }
}