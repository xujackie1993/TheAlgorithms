#

class TreeNode(object):
    def __int__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # 前序遍历
    def pre_order_traversal(self, root):

        if not root:
            return []
        return [root.val] + self.pre_order_traversal(root.left) + self.pre_order_traversal(root.right)


    def mid_order_traversal(self, root):
        if not root:
            return []
        return self.mid_order_traversal(root.left) + [root.val] + self.mid_order_traversal(root.right)


    def post_order_traversal(self, root):
        if not root:
            return []
        return self.post_order_traversal(root.left) + self.post_order_traversal(root.right) + [root.val]


    def pre_order_travel2(self, root):
        stack = []
        ans = []
        cur = root
        while cur or stack:
            if cur:
                ans.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return ans

    def mid_order_traversal2(self, root):
        stack = []
        ans = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur.val)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans

    def post_order_travel2(self, root):
        # 后序遍历
        stack = []
        ans = []
        cur = root
        while cur or stack:
            if cur:
                ans.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()
        return ans[::-1]
