class solution:
    def decodeString1(self, s):
        # 栈
        stack, res, multi = [], '', 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif "0" <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

    def decodeString2(self, s):
        # 递归
        def dfs(i):
            res = ''
            multi = 0
            while i < len(s):
                if '0' <= s[i] <= "9":
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(i + 1)
                    res += tmp * multi
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i+=1
            return res

        return dfs(0)


if __name__ == '__main__':
    solution = solution()
    s = "2[abc]3[cd]ef"
    print(solution.decodeString1(s))
    print(solution.decodeString2(s))
