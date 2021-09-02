class solution:
    def numTrees1(self, nums):
        # 哈希表/动态规划
        ans = 0
        hash_dict = dict()
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                hash_dict[num] = 1
                length = left + right + 1
                ans = max(ans, length)
                hash_dict[num] = length
                hash_dict[num - left] = length
                hash_dict[num + right] = length
        return ans

    def numTrees2(self, nums):
        ans = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_steak = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_steak += 1
                ans = max(ans, current_steak)
        return ans


if __name__ == '__main__':
    solution = solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.numTrees1(nums))
    print(solution.numTrees2(nums))
