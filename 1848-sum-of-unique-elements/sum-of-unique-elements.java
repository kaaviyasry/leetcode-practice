class Solution {
    public int sumOfUnique(int[] nums) {
        int sum=0;
    int freq[]=new int[105];
    for(int i=0;i<nums.length;i++){
        freq[nums[i]]++; // adding nums[i] count 

    }
    for(int i=0;i<freq.length;i++){
        if (freq[i]==1){
            sum+=i;

        }
    }

        return sum;
    }
}