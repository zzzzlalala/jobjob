class solution:
    def findNums(self,nums):
        oral = set(nums)
        find = []
        for i in range(1,len(nums)+1):
            if i not in oral:
                find.append(i)
        return find

test = solution()
nums = [4,3,2,7,8,2,3,1]
print(test.findNums(nums))
