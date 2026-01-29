class Solution {
    public int distributeCandies(int[] candyType) {
        HashSet<Integer> set=new HashSet<>(); // for adding  unique candytype
        for(int i:candyType){
            set.add(i); // adding candytypes
        }
        int n=candyType.length;
        int m=set.size();
        return m>=n/2?n/2:m; 
        
    }
}