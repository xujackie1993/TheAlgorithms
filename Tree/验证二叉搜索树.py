
class TreeNode(object):
    def __int__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.ans = True
        self.pre = float('-inf')

    def preOrder(self, root, l, r):
        if not root or not self.ans:
            return

        if not (l < root.val and r > root.val):
            self.ans = False
            return

        self.preOrder(root.left, l, root.val)
        self.preOrder(root.right, root.val, r)


    def midOrder(self, root):
        if root and self.ans:
            self.midOrder(root.left)
            if self.pre >= root.val:
                self.ans = False
                return
            self.pre = root.val
            self.midOrder(root.right)




    def is_valid(self, root):
        self.ans = True
        self.preOrder(root, float('-inf'), float('inf'))
        return self.ans

