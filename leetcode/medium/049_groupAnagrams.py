import collections


class solution:
    def group1(self, strs):
        tmp = collections.defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            tmp[key].append(str)
        return list(tmp.values())

    def group2(self, strs):
        tmp = collections.defaultdict(list)
        for str in strs:
            # 由于字符串只包含小写字母，因此对于每个字符串，
            # 可以使用长度为 26 的数组记录每个字母出现的次数
            counts = [0] * 26

            for ch in str:
                counts[ord(ch) - ord("a")] += 1
            tmp[tuple(counts)].append(str)
        return list(tmp.values())


if __name__ == '__main__':
    solution = solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.group1(strs))
    print(solution.group2(strs))
    print("\t")

# tmp
# collections.defaultdict()
strs = "mississippi"
tmp = collections.defaultdict(int)
for str in strs:
    tmp[str] += 1
print(sorted(tmp.items()))
print(sorted(tmp.values()))

strs = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
tmp = collections.defaultdict(list)
for str, index in strs:
    tmp[str].append(index)
print(sorted(tmp.items()))
print(sorted(tmp.values()))
