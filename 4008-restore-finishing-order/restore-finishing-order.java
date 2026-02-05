import java.util.*;
class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
      ArrayList<Integer> list=new ArrayList<>();
      for(int i=0;i<order.length;i++){
        for(int j=0;j<friends.length;j++){
            if(order[i]==friends[j]){
                list.add(order[i]);
                break;
            }
        }
      }
      int ans[]=new int[list.size()];
      for(int i=0;i<ans.length;i++){
        ans[i]=list.get(i); // storing list[i] in ans[i]
      }
      return ans;
    }
}