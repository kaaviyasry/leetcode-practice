class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int last=nums[nums.length-1]; //last value
        int pointer=1;//it contains max value position
        for(int i=nums.length-2;i>=0;i--){
            if(nums[i]!=last){
                pointer++;
                last=nums[i];
            }if(pointer==3){
                return nums[i];
            }
        }

        return nums[nums.length-1];
        
    }
}