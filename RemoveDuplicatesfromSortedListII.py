class Solution: 
    def deleteDuplicates(self, head):
        # add dummy and initialize all the pointers
        dummy = ListNode(0) 
        dummy.next = head 
        pre = dummy
        cur = head 
        while cur: 
            # if cur is not the last not and it has the same 
            # value as the next node, we update the cur pointer
            while cur.next and cur.val == cur.next.val: 
                cur = cur.next 

            if pre.next == cur:   # 1 #
                # this means cur pointer is not updated in 
                # the while loop, thus cur's value is distinct
                # we move pre pointer to the cur's location
                pre = cur 
            else:  # 2 # 
                # cur's value has repeated itself so
                # we skip the entire sequence of nodes with 
                # this value
                pre.next = cur.next 
            # and in either case we update the cur pointer
            cur = cur.next # 3 #
        return dummy.next