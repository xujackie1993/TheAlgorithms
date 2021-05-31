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
    def hasPathSumDFS(self, root, target):
        if not root:
            return False
        if not root.left and not root.left:
            return root.val == target
        return self.hasPathSumDFS(root.left, target-root.val) or self.hasPathSumDFS(root.right, target-root.val)


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
        """
        回溯指 利用 DFS 找出从根节点到叶子节点的所有路径，只要有任意一条路径的 和 等于 sum，就返回 True。
        :param root:
        :param target:
        :return:
        """
        self.preOrder(root, 0, target)
        return self.ans

    def hasPathSumBFS(self, pRoot, target):
        if not pRoot:
            return False
        arr = [(pRoot, pRoot.val)]
        while arr:
            node, path = arr.pop(0)
            if not node.left and not node.right and path == target:
                return True
            if node.left:
                arr.append((node.left, path + node.left.val))
            if node.right:
                arr.append((node.right, path + node.right.val))
        return False


