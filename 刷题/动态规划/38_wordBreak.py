class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True

        # 因为要求子串，最好是遍历背包放在外循环，将遍历物品放在内循环
        # 先遍历背包
        for j in range(1, len(s)+1):
            # 再遍历物品
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j-len(word)] and word == s[j-len(word):j])
        return dp[len(s)]
