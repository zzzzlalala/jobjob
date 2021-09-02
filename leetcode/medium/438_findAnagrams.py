class solution:
    # 滑动窗口+数组（s中找p）
    def findAna1(self, s, p):
        n, m, ans = len(s), len(p), []
        if n < m: return ans
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(m):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1
        if s_count == p_count:
            ans.append(0)
        for i in range(m, n):
            s_count[ord(s[i - m]) - ord('a')] -= 1
            s_count[ord(s[i]) - ord('a')] += 1
            if s_count == p_count:
                ans.append(i - m + 1)
        return ans

    # 滑动窗口 + 双指针

    def findAna2(self, s, p):
        n, m, ans = len(s), len(p), []
        if n < m: return ans
        p_cut = [0] * 26
        s_cut = [0] * 26
        for i in range(m):
            p_cut[ord(p[i]) - ord('a')] += 1
        left = 0
        for right in range(n):
            cur_right = ord(s[right]) - ord("a")
            s_cut[cur_right] += 1
            while s_cut[cur_right] > p_cut[cur_right]:
                cur_left = ord(s[left]) - ord('a')
                s_cut[cur_left] -= 1
                left += 1
            if right - left + 1 == m:
                ans.append(left)
        return ans


s = solution()
ans1 = s.findAna1(s="cbaebabacd", p="abc")
ans2 = s.findAna2(s="cbaebabacd", p="abc")
print(ans1)
print(ans2)
