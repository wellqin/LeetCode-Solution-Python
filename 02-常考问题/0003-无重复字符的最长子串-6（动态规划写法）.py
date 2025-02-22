class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        # 特判
        if size < 2:
            return size

        # dp[i] 表示以 s[i] 结尾的最长不重复子串的长度
        # 因为自己肯定是不重复子串，所以初始值设置为 1
        dp = [1 for _ in range(size)]
        d = dict()

        d[s[0]] = 0
        # 因为要考虑 dp[i - 1]，索引得从 1 开始，故 d[s[0]] = 0 得先写上
        for i in range(1, size):
            if s[i] in d:
                if dp[i - 1] >= i - d[s[i]]:
                    dp[i] = i - d[s[i]]
                else:
                    dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + 1
            # 设置字符与索引键值对
            d[s[i]] = i
        # 最后拉通看一遍最大值
        return max(dp)


if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
