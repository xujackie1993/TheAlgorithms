import random
#
class SortList(object):
    def inserting_sort(self, arr):
        """插入"""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def bubble_sort(self, items):
        for i in range(len(items) -1):
            for j  in range(len(items) -1 - i):
                if items[j] > items[j+1]:
                    items[j], items[j+1] = items[j+1], items[j]
        return items

    def bubble_sort_1(self, items):
        for i in range(len(items) - 1):
            flag = False
            for j in range(len(items)-1-i):
                if items[j] > items[j+1]:
                    items[j], items[j+1] = items[j+1], items[j]
                    flag = True
            if not flag:
                break
        return items

    def bubble_sort_2(self, arr):
        for i in range(len(arr) - 1):
            flag = False
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = True
            if flag:
                flag = False
                for j in range(len(arr)-2-i, 0, -1):
                    if arr[j-1] > arr[j]:
                        arr[j-1], arr[j] = arr[j], arr[j-1]
                        flag = True
                i += 1
            if not flag:
                break
        return arr

    '''
    快排步骤
    第一步，选择一个值作为基准值。
    第二步，找到基准值的位置，并将小于基准值的元素放在基准值的前面，大于基准值的元素放在基准值的后面。
    第三步，对基准值的左右两侧递归地进行这个过程。
    '''

    def quicksort(self, arr):
        """快速排序"""
        if len(arr) < 2:
            return arr
        # 选取基准，随便选哪个都可以，选中间的便于理解
        mid = arr[len(arr) // 2]
        # 定义基准值左右两个数列
        left, right = [], []
        # 从原始数组中移除基准值
        arr.remove(mid)
        for item in arr:
            # 大于基准值放右边
            if item >= mid:
                right.append(item)
            else:
                # 小于基准值放左边
                left.append(item)
        return self.quicksort(left) + [mid] + self.quicksort(right)

    def quick_sort(self, items):
        if len(items) < 2:
            return items
        mid = items[0]
        left = [i for i in items[1:] if i <= mid]
        right = [i for i in items[1:] if i > mid]

        return self.quick_sort(left) + [mid] + self.quick_sort(right)

    def quick_sort_1(self, nums, start, end):
        """
        更快的分区    两边向中间遍历 的双向分区方式，
        """
        # 递归退出条件
        if start >= end:
            return
        # 基准值
        pivot = nums[start]
        low = start
        high = end
        # 如果 low与high未重合
        while low < high:
            # high指向的元素不比基准值小 则high向左移动
            while low < high and nums[high] >= pivot:
                high -= 1
            # 将high指向的元素放在low的位置上
            nums[low] = nums[high]
            # low 指向的元素比基准值小，则low向右移动
            while low < high and nums[low] < pivot:
                low += 1
            # 将low指向的元素放在high的位置上
            nums[high] = nums[low]
        # 推出循环后,low与high重合，此时所指元素为基准元素的正确位置
        # 将基准元素放入该位置
        nums[low] = pivot
        # 对基准元素左右的子序列进行快速排序
        self.quick_sort_1(nums, start, low-1)
        self.quick_sort_1(nums, low+1, end)

    def quick_sort_2(self, nums, left, right):
        """优化：
        1、合理选择基准值     固定位置、随机选取基准、三数取中
        2、更快的分区    两边向中间遍历 的双向分区方式，而不是从左到右，当然前提是基准值选择数组的中位数
        3、三路快排，把和基准元素相等的元素放在中间，比他小的在左边，大的在右边。这样避免了重复元素过多的情况
        https://www.jianshu.com/p/9eff99d403fb
        """
        if left >= right:
            return
        # random_index = random.randint(left, right)
        # nums[left], nums[random_index] = nums[random_index], nums[left]
        # pivot = nums[left]
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] < nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        pivot = nums[left]
        # 定义lt：小于v部分元素 的下标，初始是空的，因为arr[left]是基准元素
        lt = left  # arr[left+1...lt] < v
        # gt 大于v 部分开始的下标，初始为空
        gt = right + 1  # arr[gt...right] > v
        i = left + 1  # arr[lt+1...i] == v
        # 终止条件：下标i 和gt 遇到一起，说明都排完了
        while i < gt:
            if nums[i] < pivot:
                nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
                gt -= 1
            else:
                i += 1
        # 最后把第一个元素（基准元素）放到等于v的部分
        nums[left], nums[lt] = nums[lt], nums[left]
        # 递归排序
        self.quick_sort_2(nums, left, lt - 1)
        self.quick_sort_2(nums, gt, right)


if __name__ == "__main__":
    alist = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    sqlist = SortList()
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.quick_sort_2(alist, 0, len(alist)-1)
    print(alist)






