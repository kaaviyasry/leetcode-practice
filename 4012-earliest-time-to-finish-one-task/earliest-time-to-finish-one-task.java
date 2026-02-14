class Solution {
    public int earliestTime(int[][] tasks) {
        int min=Integer.MAX_VALUE;
        for(int i=0;i<tasks.length;i++){
            int starting=tasks[i][0]; // 1st value
            int duration=tasks[i][1]; //it takes 2nd value
            int finishing=starting+duration;
            min=Math.min(min,finishing);
        }
        return min;
        
    }
}