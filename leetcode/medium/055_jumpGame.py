class solution:
    def jump(self, nums):
        # 贪心
        # 判断当前位置能到达，并且当前位置+跳数》最远位置，就更新最远位置
        # 返回最远位置和数组长度
        jump_max = 0
        for i, jump in enumerate(nums):
            if jump_max >= i and i + jump > jump_max:
                jump_max = i + jump
        return jump_max > i


if __name__ == '__main__':
    test = solution()
    nums = [2, 3, 1, 1, 4]
    print(test.jump(nums))
