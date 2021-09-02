class solution:

    def generatePara(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generatePara(c):
                for right in self.generatePara(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

    def generatePara1(self, n):
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans

    def generatePara2(self, n):
        ans = []

        def backtrack(S, L, R):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if L < n:
                S.append("(")
                backtrack(S, L + 1, R)
                S.pop()
            if R < L:
                S.append(')')
                backtrack(S, L, R + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    test = solution()
    n = 3
    print(test.generatePara(n))
    print(test.generatePara1(n))
    print(test.generatePara2(n))
