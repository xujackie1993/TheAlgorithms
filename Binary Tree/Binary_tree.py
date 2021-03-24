#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BrinaryNode(object):
    """二叉树节点类"""
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BrinaryTree(object):
    """二叉树及几种遍历方法"""
    def __init__(self):
        self.root = None
        self.bi_list = []           # 使用队列存放二叉树的层次节点信息

    def is_empty(self):
        return self.root is None

    def add(self, item):
        """依次为二叉树添加节点 从上到下 从左到右"""
        node = BrinaryNode(item)
        if self.is_empty():
            self.root = node
            self.bi_list.append(node)
        else:
            temp_node = self.bi_list[0]
            if temp_node.left is None:
                temp_node.left = node
                self.bi_list.append(node)
            else:
                temp_node.right = node
                self.bi_list.append(node)
                self.bi_list.pop(0)

    def pre_order(self, root):
        """前序遍历"""
        if root is None:
            return
        print(root.item)
        self.in_order(root.left)
        self.in_order(root.right)

    def in_order(self, root):
        """中序遍历"""
        if root is None:
            return

        self.pre_order(root.left)
        print(root.item)
        self.pre_order(root.right)

    def post_order(self, root):
        """后序"""
        if root is None:
            return
        self.pre_order(root.left)
        self.pre_order(root.right)
        print(root.item)

    def level_order(self, root):
        """层次遍历 广度优先遍历"""
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            print(node.item)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


    def pre_order_stack(self, root):
        """先序遍历的非递归实现"""
        if root is None:
            return



