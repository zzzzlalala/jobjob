class solution:
    # 回溯

    def letterCombinations(self, digits):
        if not digits: return []
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(comb, nextdigits):
            if len(nextdigits) == 0:
                res.append(comb)
            else:
                for letter in phone[nextdigits[0]]:
                    backtrack(comb + letter, nextdigits[1:])

        res = []
        backtrack('', digits)
        return res

    # 回溯
    def letterCombinations1(selfs, digits):
        if not digits: return []
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index):
            if index == len(digits):
                comb.append(''.join(comb))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    comb.append(letter)
                    backtrack(index + 1)
                    comb.pop()

        comb = []
        combs = []
        backtrack(0)
        return combs

    # 队列
    def letterCombinations2(self, digits):
        if not digits: return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']
        for digit in digits:
            # print("digits:",digit)
            for _ in range(len(queue)):
                # print("_:",_)
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:
                    # print("letter:",letter,"index:",ord(digit)-50)
                    queue.append(tmp + letter)
                    # print("queue:",queue)
        return queue


if __name__ == '__main__':
    test = solution()
    digits = "234"
    print(test.letterCombinations(digits))
    print(test.letterCombinations1(digits))
    print(test.letterCombinations2(digits))
