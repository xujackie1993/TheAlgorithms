# 给定目标值，一颗二叉树 输出所有路径，满足根节点至叶子节点之和等于给定的数值

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):

    def __init__(self):
        self.ans = False

    # 深度优先 DFS
    def hasPathSumDFS(self, root, sum):
        if not root:
            return False
        if not root.left and not root.left:
            return root.val == sum
        return self.hasPathSumDFS(root.left, sum-root.val) or self.hasPathSumDFS(root.right, sum-root.val)


    def preOrder(self, root, sum, target):
        if not root or self.ans:
            return
        sum += root.val
        if not root.left and not root.right:
            if sum == target:
                self.ans = True
                return
        self.preOrder(root.left, sum, target)
        self.preOrder(root.right, sum, target)



    def hasPathSumBackTrace(self, root, target):
        self.preOrder(root, 0, target)
        return self.ans



