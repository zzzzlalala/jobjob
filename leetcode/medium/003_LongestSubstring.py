class solution:
    def LongestSubstring(self, s):
        # 滑动窗口
        occ = set()
        right, left = -1, 0
        # 两个指针都向右移动，左指针移动移除一个字符，右指针移动增加一个字符
        for i in range(len(s)):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while right + 1 < len(s) and s[right + 1] not in occ:
                occ.add(s[right + 1])
                right += 1
            left = max(left, right + 1 - i)
        return left

    def LongestSubstring1(self, s):
        k, res, c_dict = -1, 0, {}
        for j, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = j
            else:
                c_dict[c] = j
                res = max(res, j - k)
        return res


if __name__ == '__main__':
    test = solution()
    s = "abcabcbb"
    print(test.LongestSubstring(s))
    print(test.LongestSubstring1(s))
