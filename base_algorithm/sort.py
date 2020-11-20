"""
排序算法
"""
import time


class BaseSort(object):
    def __init__(self, arg_list, **kwargs):
        self.arg_list = arg_list
        self.step = 0
        self.length = len(arg_list)
        start = time.time()
        if self.length > 1:
            self.sort()
        self.time = (time.time() - start) * 1000

    def sort(self):
        pass

    def swap(self, i, j):
        self.arg_list[i], self.arg_list[j] = self.arg_list[j], self.arg_list[i]

    def insert(self, i, j):
        """将i位置元素插入j位置,j到i的元素全部后移一位"""
        a = self.arg_list.pop(i)
        self.arg_list.insert(j, a)
        # a = self.arg_list[i]
        # for jj in reversed(range(j, i)):
        #     self.arg_list[i] = self.arg_list[jj]
        #     i = jj
        # self.arg_list[j] = a

    def copy_list(self, a_list):
        result = [i for i in a_list]
        return result

    def print(self):
        print(self.__class__.__name__, self.time, "ms,", "step", self.step)


class BubbleSort(BaseSort):
    """冒泡排序"""
    def __init__(self, arg_list, **kwargs):
        super(BubbleSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        while True:
            flag = True
            for i in range(self.length - 1):
                if self.arg_list[i+1] < self.arg_list[i]:
                    self.step += 1
                    self.swap(i+1, i)
                    flag = False
            if flag:
                break


class SelectSort(BaseSort):
    """选择排序"""
    def __init__(self, arg_list, **kwargs):
        super(SelectSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        for i in range(self.length):
            for j in range(self.length):
                if j > i and self.arg_list[j] < self.arg_list[i]:
                    self.step += 1
                    self.swap(j, i)


class InsertSort(BaseSort):
    """插入排序"""
    def __init__(self, arg_list, **kwargs):
        super(InsertSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        for i in range(1, self.length):
            for j in range(i):
                if self.arg_list[i] < self.arg_list[j]:
                    self.step += 1
                    self.insert(i, j)
                    break


class ShellSort(BaseSort):
    """希尔排序"""
    def __init__(self, arg_list, **kwargs):
        super(ShellSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        k = self.length
        while k > 1:
            k = k // 2
            for i in range(k, self.length):
                tem = self.arg_list[i]
                for j in range(i-k, -1, -k):
                    if self.arg_list[i] < self.arg_list[j]:
                        self.swap(j, i)
                        i = j
                    else:
                        break



class MergeSort(BaseSort):
    """归并排序"""
    def __init__(self, arg_list, **kwargs):
        super(MergeSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        # self.merge(self.arg_list)
        self.merge_list()

    def merge_list(self):
        """非递归"""
        k = 2
        half_k = 1
        max = self.length * 2
        while k < max:
            for i in range(0, self.length, k):
                a_list = self.copy_list(self.arg_list[i: i+half_k])
                b_list = self.copy_list(self.arg_list[i+half_k: i+k])
                j = i
                while a_list and b_list:
                    self.step += 1
                    if a_list[0] < b_list[0]:
                        self.arg_list[j] = a_list.pop(0)
                    else:
                        self.arg_list[j] = b_list.pop(0)
                    j += 1
                for v in a_list:
                    self.arg_list[j] = v
                    j += 1
                for v in b_list:
                    self.arg_list[j] = v
                    j += 1
            half_k = k
            k *= 2

    def merge(self, arg_list):
        """递归"""
        length = len(arg_list)
        if length < 2:
            return
        mid = length // 2
        a_list = self.copy_list(arg_list[:mid])
        b_list = self.copy_list(arg_list[mid:])
        self.merge(a_list)
        self.merge(b_list)
        j = 0
        while a_list and b_list:
            self.step += 1
            if a_list[0] < b_list[0]:
                arg_list[j] = a_list.pop(0)
            else:
                arg_list[j] = b_list.pop(0)
            j += 1
        for v in a_list:
            arg_list[j] = v
            j += 1
        for v in b_list:
            arg_list[j] = v
            j += 1


class FastSort(BaseSort):
    """快速排序"""
    def __init__(self, arg_list, **kwargs):
        super(FastSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        # self.fast(self.arg_list)
        # self.fast(self.arg_list, 0, self.length-1)
        self.fast_list()

    def fast_list2(self):
        """非递归形式"""
        stack = [self.arg_list]
        result = []
        while stack:
            arg_list = stack.pop()
            length = len(arg_list)
            if length < 2:
                if result and arg_list:
                    if result[0] < arg_list[0]:
                        result.extend(arg_list)
                        self.step += 1
                    else:
                        tem_list = result
                        result = []
                        result.extend(arg_list)
                        result.extend(tem_list)
                        self.step += 1
                else:
                    result.extend(arg_list)
                continue
            a = arg_list[0]
            a_list = []
            b_list = []
            for v in arg_list:
                self.step += 1
                if v <= a:
                    a_list.insert(0, v)
                else:
                    b_list.append(v)
            stack.append(b_list)
            stack.append(a_list)
        self.arg_list = result

    def fast_list(self):
        # 非递归
        stack = [(0, self.length - 1)]
        while stack:
            start, end = stack.pop()
            if start < end:
                left = start - 1
                p = self.arg_list[end]
                for i in range(start, end):
                    if self.arg_list[i] < p:
                        self.swap(left+1, i)
                        left += 1
                self.swap(left + 1, end)
                stack.append((left+2, end))
                stack.append((start, left))

    def fast(self, arg_list, start, end):
        if start < end:
            p = arg_list[end]
            left = start - 1
            for i in range(start, end + 1):
                if arg_list[i] < p:
                    self.swap(left+1, i)
                    left += 1
            self.swap(left+1, end)

            self.fast(arg_list, start, left)
            self.fast(arg_list, left+1, end)

    def fast2(self, arg_list):
        """递归形式"""
        length = len(arg_list)
        if length < 2:
            return
        a = arg_list[0]
        a_list = []
        b_list = []
        for v in arg_list:
            self.step += 1
            if v <= a:
                a_list.insert(0, v)
            else:
                b_list.append(v)
        self.fast(a_list)
        self.fast(b_list)
        i = 0
        self.step += 1
        for v in a_list:
            arg_list[i] = v
            i += 1
        self.step += 1
        for v in b_list:
            arg_list[i] = v
            i += 1


class HeapSort(BaseSort):
    """堆排序"""
    def __init__(self, arg_list, **kwargs):
        super(HeapSort, self).__init__(arg_list, **kwargs)

    def sort(self):
        n = self.length // 2
        for i in reversed(range(n)):
            self.heap(self.length, i)
        for i in range(self.length):
            #self.arg_list.append(self.arg_list.pop(0))
            self.swap(self.length - i - 1, 0)
            self.heap(self.length - i - 1, 0)

    def heap(self, length, i):
        if length < 2:
            return
        left = i * 2 + 1
        right = i * 2 + 2
        t = i
            
        if left < length and self.arg_list[left] < self.arg_list[i]:
            # self.step += 1
                #self.swap(left, i)
            i = left
        if right < length and self.arg_list[right] < self.arg_list[i]:
            # self.step += 1
            i = right
                #self.swap(right, i)
        if t != i:
            self.swap(t, i)
            self.heap(length, i)
            


if __name__ == '__main__':
    import random
    arg_list = [i for i in range(5000)]
    random.shuffle(arg_list)
    # print(arg_list)
    #sort = BubbleSort(arg_list.copy())
    #sort.print()
    #sort = SelectSort(arg_list.copy())
    #sort.print()
    sort = InsertSort(arg_list.copy())
    sort.print()
    sort = ShellSort(arg_list.copy())
    sort.print()
    sort = MergeSort(arg_list.copy())
    sort.print()
    sort = FastSort(arg_list.copy())
    sort.print()
    # print(sort.arg_list)
    sort = HeapSort(arg_list.copy())
    sort.print()
    #print(sort.arg_list)
    # print(sort.time)