
class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
            dp = new_dp

        # Remove the empty subsequence
        return (dp - 1) % MOD
