class solution:

    def merge(self, intervals):
        # 按左端点排序
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for interval in intervals:
            # 下一个开头>上一个结尾,不会重合，添加到数组末尾
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            # 下一个开头<=上一个结尾，则重合，比较右端点
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


if __name__ == '__main__':
    test = solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(test.merge(intervals))


"""
    sorted(iterable, cmp=None, key=None, reverse=False)
"""

# exp
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
students_age_sorted = sorted(students,key=lambda x:x[2])
students_age_sorted = sorted(students,key=lambda x:x[2],reverse=True)
print(students_age_sorted)