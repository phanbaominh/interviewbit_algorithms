/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        TreeLinkNode p = null;
        TreeLinkNode left = root;
        TreeLinkNode right = null;
        TreeLinkNode cur = null;
        TreeLinkNode tmp = null;
        while (left != null || cur != null) {
            
            if (cur == left || left == null){
                if (cur.left != null){
                    left = cur.left;
                }
                else if (cur.left == null && cur.right != null){
                    left = cur.right;
                }
                else{
                    left = null;
                }
            }

            while (p != null && p.next != null && (p.left == null || p.left == cur) && (p.right == null || p.right == cur)){
                p = p.next;
            }

            if (p != null && p.left != cur && p.left != null){
                right = p.left;
            } else if (p != null && p.right != cur && p.right != null){
                right = p.right;
                p = p.next;
            } else{
                right = null;
            }
            
            if (cur!=null){
                cur.next = right;
            }

            if (cur == null || cur.next == null){
                p = tmp;
                cur = left;
                tmp = left;
            }
            else if (cur != null && cur.next != null){
                cur = cur.next;
            }
        }
        //System.out.println(" ");
    }
}