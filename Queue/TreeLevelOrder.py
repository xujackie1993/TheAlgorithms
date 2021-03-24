# -*- coding=utf-8 -*-
# 二叉树遍历
# class TreeNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def levelOrderByQueue(self, root):
        """
        使用优先队列
        :type root: TreeNode
        :rtype: list[List[int]]
        """
        ans = []
        Q = queue.Queue()
        if root:
            Q.put(root)
        
        while not Q.empty():
            qSize = Q.qsize()
            curLevel = []
            for i in range(qSize):
                node = Q.get()
                curLevel.append(node.value)
                if node.left:
                    Q.put(node.left)
                if node.right:
                    Q.put(node.right)
            ans.append([x for x in curLevel])
        return ans
    

    def levelOrder(self, root):
        """
        使用两层数组表示FIFO队列
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        curLevel = []
        if root:
            curLevel.append(root)
        while curLevel > 0:
            curResult = []
            nextLevel = []
            for i in range(len(curLevel)):
                node = curLevel[i]
                curResult.append(node.value)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ans.append(curResult)
            curLevel = nextLevel
        return ans

    


