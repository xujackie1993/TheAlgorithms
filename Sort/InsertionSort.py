"""
插入排序  通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
"""


def insertion_sort1(arr):
    """递增"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def insertion_sort2(arr):
    """递减 """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


if __name__ == "__main__":

    print(insertion_sort1([3, 4, 2, 1]))




