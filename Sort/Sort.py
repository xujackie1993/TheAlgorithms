# 
class SortList(object):
    def __init__(self, l):
        self.arr = l

    def inserting_sort(self):
        """插入"""
        arr = self.arr
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    
    def bubble_sort(self):
        arr = self.arr
        for i in range(len(arr) - 1):
            flag = False
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = True
            if not flag:
                return arr
            if flag:
                flag = False
                for j in range(len(arr)-2 - i, 0, -1):
                    if arr[j-1] > arr[j]:
                        arr[j-1], arr[j] = arr[j], arr[j-1]
                        flag = True
        return arr

    def __str__(self):
        ret = ""
        for i in self.arr:
            ret += " %s" % i
        return ret


if __name__ == "__main__":
    sqlist = SortList([4,1,7,3,8,5,9,2,6])
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.bubble_sort()
    print(sqlist)






