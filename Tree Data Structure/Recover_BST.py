# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @param A : root node of tree
# @return a list of integers
def recoverTree(A):
    current = A
    curd = None
    res = []

    while current != None:
        if (current.left == None):
            pred = curd
            curd = current.val
            if pred != None and (curd < pred):
                    res.append(pred)
                    res.append(curd)
            current = current.right   
        else:
            tmp = current.left
            while (tmp.right != None and tmp.right != current):
                tmp = tmp.right
            if (tmp.right == None):
                tmp.right = current
                current = current.left
            else:
                tmp.right = None
                pred = curd
                curd = current.val
                if pred != None and (curd < pred):
                    res.append(pred)
                    res.append(curd)
                current = current.right

    if len(res) > 2:
        res = [res[0],res[3]]
    res = sorted(res)
    
    return res
                