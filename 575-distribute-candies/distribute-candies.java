class Solution {
    public int distributeCandies(int[] candyType) {
        int n=candyType.length/2;
        HashSet<Integer> set=new HashSet<>();
        for(int i:candyType){
            set.add(i);
        }
        int ans=Math.min(n,set.size());


       return ans;
    }
}