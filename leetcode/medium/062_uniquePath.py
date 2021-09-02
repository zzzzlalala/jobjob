from scipy.special import comb


class solution:
    def uniquePath(self, m, n):
        # 向右m-1，向下n-1 C(m+n-2/m-1)?
        return comb(m + n - 2, m - 1)


if __name__ == '__main__':
    test = solution()
    m = 7
    n = 3
    print(test.uniquePath(m, n))

"""
    组合数学
    from scipy.special import perm, comb
    
"""
# exp
from scipy.special import perm, comb

m = 7
n = 3
A = int(perm(m, n))
C = int(comb(m + n - 2, n - 1))
print(A, C)
