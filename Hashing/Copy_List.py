# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# @param head, a RandomListNode
# @return a RandomListNode
def copyRandomList(head):
    table = {}
    tmp = head
    new_head = None
    ptr = None
    while tmp != None:
        if new_head == None:
            new_head = RandomListNode(tmp.label)
            ptr = new_head
        else:
            new_node = RandomListNode(tmp.label)
            ptr.next = new_node
            ptr = ptr.next
        if table.get(ptr.label) == None:
            table[ptr.label] = []
        table[ptr.label].append([ptr,tmp])
        tmp = tmp.next
    tmp = head
    tmp1 = new_head
    while tmp != None:
        if tmp.random != None:
            k = tmp.random.label
            for i in range(int(len(table[k]))):
                if table[k][i][1] == tmp.random:
                    tmp1.random = table[k][i][0]
                    break
        else:
            tmp1.random = None
        tmp = tmp.next
        tmp1 = tmp1.next
            
    return new_head