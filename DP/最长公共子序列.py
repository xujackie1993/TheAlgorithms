"""
最长 公共子序列

定义子问题是res[i][j]为截至到字符串A的第i个字符串到字符串B的第j个字符的最长公共子序列

状态之间的转换方程
当i=0 or j=0时，res[i][j] = 0
当A[i] = B[j]时，res[i][j] = res[i-1][j-1] + 1
当A[i] != B[j], res[i][j] = max(res[i-1][j], res[i][j-1])

"""

class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        """最长公共子序列"""
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def LCS(self, str1, str2):
        """
        最长公共子串
        """
        # write code here
        len1 = len(str1)
        len2 = len(str2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        result = 0
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i-1] == str2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(result, dp[i][j])
        return result

    def LCS1(self, str1, str2):
        a, b = "", ""
        for i in str1:
            a += i
            if a in str2:
                b = a
            else:
                a = a[1:]
        return b

    def lengthOfLongestSubstring(self, s):
        """最长不含重复字符的子字符串  by + 双指针+ 哈希表"""
        dic = {}
        res = 0
        i = -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j-i)
        return res

    





if __name__ == "__main__":
    s = Solution()
    # res = s.longestCommonSubsequence("abcde", "ace")
    # print(res)
    res2 = s.LCS("1AB2345CD","12345EF")
    print(res2)

