/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1==null)
        return l2;
        if(l2==null)
        return l1;
        ListNode ans=new ListNode();
        ListNode curr=ans;
        ListNode n1=reverse(l1);
        ListNode n2=reverse(l2);
        int carry=0;
        while(n1 != null || n2 != null || carry>0){
            int sum=carry;
            if(n1 != null){
                sum += n1.val;
                n1=n1.next;
            }
            if(n2 != null){
                sum += n2.val;
                n2=n2.next;
            }
            carry=sum/10;
          
            curr.next=new ListNode(sum % 10);
            curr=curr.next;
        }
        return reverse(ans.next);
    }
    private ListNode reverse(ListNode node){
        if(node==null || node.next==null) return node;
        ListNode prev=null;
        ListNode pres=node;
        ListNode next=pres.next;
        while(pres != null){
            pres.next=prev;
            prev=pres;
            pres=next;
            if(next != null) next=next.next;
        }
        return prev;
    }
}