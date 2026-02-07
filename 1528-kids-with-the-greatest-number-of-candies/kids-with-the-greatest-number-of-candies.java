class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> ans=new ArrayList();
        int max=candies[0]; 
        int n=candies.length;
        for(int i=1;i<n;i++){ //finding max value in candies
            if(candies[i]>max){
                max=candies[i];
            }
        }
        for(int i=0;i<n;i++){ //checking with extra candies
            if(candies[i]+extraCandies<max){
                ans.add(false);
            }
            else if(candies[i]+extraCandies>=max){
                ans.add(true);
            }

        }
        return ans;

    }
}