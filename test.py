from typing import Optional 

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """   
            cur = l1
            curr = l2
            while cur.next is not None:
                x = cur.val
                cur = cur.next
                y = curr.vals
            print(cur.val + curr.val)
        """

        # after learning the dummy head tech this how we solve this now
        dum = cur = ListNode(0)

        # if both list dont have a next node return
        if l1.next is None and l2.next is None:
            return dum

        while l1 and l2:
            nd = l1.val + l2.val
            if nd > 9:
                nw = nd % 10
                nw = ListNode(nd)
                l1.next.val + nw.val

                nd1 = nd - nw.val
                cur.next = ListNode(nd1) 

            else:
                cur.next = nd
                l1 = l1.next
                l2 = l2.next
        print(cur)


if __name__ == "__main__":
    s = Solution()
    s.addTwoNumbers([2,4,3], [5,6,4])


    

