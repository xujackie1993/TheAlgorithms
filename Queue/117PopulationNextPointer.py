# -*-coding=utf-8 -*-
# class TreeNode(object):
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def Connect(self, root):
        """
        修改二叉树中的next指针，使其指向右边的节点 
        然后为了清晰表明思路，这里我就用了两个变量，oneLayer表示当前这一层树的所有节点，nextLayer表示下一层树的所有节点。

        然后最核心的思想就是，其实整个题就是要把树拆成一层一层的，然后每层里面，前一个节点的next指向后一个节点。后面没有就是空的。

        其实对于oneLayer这一层树的所有节点来说，把他们每个节点的左右取出来，就是下一层的节点了。

        for i in oneLayer:
            if i.left:
                nextLayer.append(i.left)
            if i.right:
                nextLayer.append(i.right)
        然后对nextLayer里所有节点，每个节点的next指向后一个节点就可以了。

        :type root: TreeNode
        :rtype ans: TreeNode
        """
        if root == None:
            return root
        
        def BFS(oneLayer):
            nextLayer = []
            for i in oneLayer:
                if i.left:
                    nextLayer.append(i.left)
                if i.right:
                    nextLayer.append(i.right)
            if len(nextLayer) > 1:
                for j in range(0, len(nextLayer) - 1):
                    nextLayer[j].next = nextLayer[j+1]
            if nextLayer:
                BFS(nextLayer)
        BFS([root])
        return root

    def connect_2(self, root):
        """
        rootNode 代表当前层的一个节点，这个点是不停的往右移动的。
        oneNode_Next 代表当前层下面一层的某一个节点，这个点是不停的往右移动的。
        first_Next 代表当前层下面一层的最左边的第一个节点，这个点是用来标记当前层扫描完以后，rootNode要下来进入这一层的时候的位置。


        大概分3步走

        首先我们最开始的话，rootNode就是根节点，oneNode_Next和first_Next都是空的。
        然后我们看rootNode的下一层，注意，如果这时候first_Next是空的的话，我们找到的第一个节点就是下一层的最左边的节点，要第一时间传给first_Next。
        2.1 比如说rootNode.left不是空的，那第一时间标记一下first_Next = rootNode.left。
        2.2 如果我们找到了一个非空的节点，同时oneNode_Next已经帮我们记录了上一个节点，那么我们就要把next指向连起来。oneNode_Next.next = rootNode.left（比如我们找到rootNode.left不是空的）
        2.3 同时，只要找到一个节点不是空的，我们的oneNode_Next的任务就是逐个充当这些节点。当rootNode到头了。这个时候，也就是说当前层我们用rootNode全都过了一遍。并且同时，
        我们把下面一层节点的next全都连好了。我们就可以把rootNode跳到刚才我们标记的下一层最左节点first_Next位置。因为next全都标好了，next就是右边节点的位置。
        我们就用rootNode = rootNode.next逐个移动rootNode，同时继续把下一层的节点的next都连上。

        """
        if root == None:
            return root

        rootNode = root  # 初始状态  代表当前层的一个节点，这个点是不停的往右移动的。

        oneNode_Next = None  # 初始状态  代表当前层下面一层的某一个节点，这个点是不停的往右移动的。
        first_Next = None  # 初始状态    代表当前层下面一层的最左边的第一个节点，这个点是用来标记当前层扫描完以后，rootNode要下来进入这一层的时候的位置。

        while rootNode:                         # 当前层节点不是空的时候
            if rootNode.left:                   # 当前层节点下面的左子节点不是空
                if not first_Next:  # 还没有记录first_Next的话，第一时间记录下来。
                    first_Next = rootNode.left
                if oneNode_Next:  # 如果之前有记录的oneNode_Next就把它的next指向现在这个位置。
                    oneNode_Next.next = rootNode.left
                oneNode_Next = rootNode.left # 移动oneNode_Next到当前位置。

            if rootNode.right: # 同上一段。
                if not first_Next:
                    first_Next = rootNode.right
                if oneNode_Next:
                    oneNode_Next.next = rootNode.right
                oneNode_Next = rootNode.right

            rootNode = rootNode.next  # 当前行内rootNode往右移动。

            if not rootNode:  # 移动rootNode到下一行的初始位置。
                rootNode = first_Next
                oneNode_Next = None
                first_Next = None

        return root