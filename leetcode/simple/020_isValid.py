class solution():
    # 栈
    def isValid1(self, s):
        if len(s) % 2 == 1:
            return False
        kuohao = {
            ")": '(',
            "}": "{",
            "]": "[",
        }
        stack = list()
        for ch in s:
            if ch in kuohao:
                if not stack or stack[-1] != kuohao[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

    def isValid2(self, s):
        kuohao = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for i in s:
            if stack and i in kuohao:
                if stack[-1] == kuohao[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack


test = solution()
print(test.isValid2("(){}[]"))
print(test.isValid2("(){"))
print(test.isValid2("[{]}"))
