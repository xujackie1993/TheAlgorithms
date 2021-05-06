# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def TreeMaxDepth_1(self, root):
        if root is None:
            return 0
        return max(self.TreeMaxDepth_1(root.left), self.TreeMaxDepth_1(root.right)) + 1


    def TreeMaxDepth_2(self, root):
        if root is None:
            return 0
        arr = [root]
        count = 0
        while arr:
            for i in range(len(arr)):
                node = arr.pop(0)
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)
            count += 1
        return count


    def TreeMinDepth_1(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return self.TreeMinDepth_1(root.right) + 1
        if root.left is not None and root.right is None:
            return self.TreeMinDepth_1(root.left) + 1
        left = self.TreeMinDepth_1(root.left)
        return min(left, self.TreeMinDepth_1(root.right) + 1)


    def TreeMinDepth_2(self, pRoot):
        """
        算法遍历二叉树每一层，一旦发现某层的某个结点无子树，就返回该层的深度，这个深度就是该二叉树的最小深度
        :param pRoot:
        :return:
        """
        if pRoot is None:
            return 0
        arr = [pRoot]
        min_length = 0
        while arr:
            tmp = []
            for node in arr:
                if not node.left and not node.right:
                    return min_length
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            arr = tmp
            min_length += 1
        return min_length
