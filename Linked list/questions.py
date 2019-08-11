#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""关于链表的笔试题目"""

# 剑指offer 从尾到头打印链表 返回一个数组


class ListNode(object):
    def __init__(self, _value):
        self.val = _value
        self.next = None


class RandomListNode(object):
    def __init__(self, _value):
        self.val = _value
        self.next = None
        self.random = None


class Solution1(object):
    def print_linked_list_from_tail_to_head(self, list_node):
        if not list_node:
            return []
        ls = []
        current = list_node
        while current.next is not None:
            ls.append(current.val)
            current = current.next
        return ls[::-1]


# 剑指offer 删除链表中重复的节点   链表1>2>3>3>4>4>5  -- 1>2>5

class Solution2(object):

    def create_linked_list(self, arr):
        pre = ListNode(0)
        tmp = pre
        for i in arr:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return pre.next

    def print(self, linked_list):
        tmp = linked_list
        l_pp = []
        while tmp:
            l_pp.append(str(tmp.val))
            # print(tmp.val)
            tmp = tmp.next
        return "-".join(l_pp)

    # 在原链表前加一个pre_head,用它的next返回原链表去重后的链表头指针
    # 使用两个指针pHead和pre，分别指当前判断的节点和当前节点的前一个节点；
    def delete_duplication1(self, pHead):
        pre_head = ListNode(0)
        pre_head.next = pHead
        pre = pre_head
        print(self.print(pre_head.next))
        print()
        while pHead is not None:
            if pHead.next is not None and pHead.next.val == pHead.val:
                tmp = pHead.next
                while tmp is not None and tmp.val == pHead.val:
                    tmp = tmp.next
                pre.next = tmp
                pHead = tmp
            else:
                pre = pHead
                pHead = pHead.next
        return pre_head.next


    # 采用递归
    def delete_duplication2(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        real_Head = pHead                   # real_head为原链表除去重复节点之后的链表头指针
        aft = pHead.next                    # aft为原链表的第二个节点
        if aft.val != real_Head.val:
            # 若前两个节点不同,则real_head就是pHead 对面的链表递归调用
            real_Head.next = self.delete_duplication2(aft)
        else:
            # 若前两个节点相同，则需要找到真正的链表头节点
            tmp = aft
            # 循环向后找到与pHead不同的那个节点
            while tmp.val == real_Head.val and tmp.next is not None:
                tmp = tmp.next
            if tmp.val != real_Head.val:
                # 后半段链表的链表头为原链表的链表头
                real_Head = self.delete_duplication2(tmp)
            else:
                # 若整个链表完全重复
                return None
        return real_Head


class Solution3(object):

    def create_linked_list(self, arr):
        pre = ListNode(0)
        tmp = pre
        for i in arr:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return pre.next

    def print(self, linked_list):
        tmp = linked_list
        l_pp = []
        while tmp:
            l_pp.append(tmp.val)
            tmp = tmp.next
        print("-".join(l_pp))

    # 反转链表  以单链表的第一个元素为循环变量  设置2个辅助变量  tmp保存数据 new_head 新的反转链表的表头
    def reverse_linked1(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        cur = pHead
        new_head = None
        while cur is not None:
            tmp = cur.next
            cur.next = new_head
            new_head = cur
            cur = tmp
        return new_head

    def reverse_linked2(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        else:
            newHead = self.reverse_linked2(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
        return newHead

    # 判断链表是否成环  使用快慢指针
    def is_circle(self, pHead):
        slowPtr = pHead
        fastPtr = pHead
        loopExist = None
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if fastPtr == slowPtr:
                loopExist = True
                print("存在环结构")
                break
        if loopExist:
            slowPtr = pHead
            while slowPtr != fastPtr:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next
            return slowPtr
        print("不是环结构")
        return False

    # 输出链表的倒数第K个节点
    def find_kth_tofail(self, pHead, k):
        if k < 1:
            return
        nodes = []
        cur = pHead
        while cur is not None:
            nodes.append(cur)
            cur = cur.next
        if k > len(nodes):
            return
        else:
            return nodes[-k]


    # 合并两个排序的链表
    def merge_two_sorted_linked_list(self, pHead1, pHead2):
        newHead = ListNode(-1)
        cur = newHead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
        while pHead1:
            cur.next = pHead1
        while pHead2:
            cur.next = pHead2
        return newHead.next


    # 复制复杂链表 1、把复制的节点链接在原链表对应节点后边 2、把复制节点的random指针指向被复制节点的random指针的下一个节点
    # 3、 拆分链表 奇数位置为原链表 偶数位置的复制链表
    def clone(self, pHead):
        if pHead is None:
            return
        cur = pHead
        while cur:
            copy_node = RandomListNode(_value=cur.val)
            next = cur.next
            cur.next = copy_node
            copy_node.next = next
            cur = next

        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next

        copy_head = pHead.next
        cur = pHead
        while cur:
            copy_node = cur.next
            cur.next = copy_node.next
            copy_node.next = copy_node.next.next if copy_node is not None else None
            cur = cur.next
        return copy_head

    def find_first_common_node(self, pHead1, pHead2):
        cur1, cur2 = pHead1, pHead2
        len1, len2 = 0, 0
        while cur1:
            len1 += 1
            cur1 = cur1.next
        while cur2:
            len2 += 1
            cur2 = cur2.next

        if len1 > len2:
            while len1 - len2 > 0:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            while len1 - len2 < 0:
                pHead2 = pHead2.next

        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1

    # 两个非空链表表示两个非负的数 位数按照逆序来存储 返回一个新的链表表示它们的和
    def addTwoNumber(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_head = ListNode(0)
        cur = sum_head
        cur1, cur2 = l1, l2
        is_add = 0
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            tmp = val1 + val2 + is_add
            is_add = tmp // 10
            cur.next = ListNode(tmp % 10)
            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        if is_add == 1:
            cur.next = ListNode(1)
        return sum_head.next




















if __name__ == "__main__":

    s2 = Solution2()
    linked2 = s2.create_linked_list([1,2,2,3,3,4,5])
    # s2.print(linked2)
    link2 = s2.delete_duplication1(linked2)
    s2.print(link2)
    # s3 = Solution3()
    # linked = s3.create_linked_list(range(1,5))
    # s.print(linked)
    # rever1 = s.reverse_linked1(linked)
    # s.print(rever1)
    # rever2 = s3.reverse_linked2(linked)
    # s3.print(rever2)






