# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(A):
    if A==None:
        return A
    B = A
    C = B.next
    prev = A
    check = False

    while C!=None:
        if B.val==C.val:
            while B!=None and B.val==C.val:
                B=B.next
            if B==None:
                C=None
            else:
                C=B.next

            if B==None and check:
                prev.next=None
            elif not check:
                A=B
                prev=A
            elif check and (B!=None and (C==None or B.val!=C.val)):
                prev.next=B
                prev=B
            
        else:
            prev=B
            check=True
            B=B.next
            C=C.next
    return A        
