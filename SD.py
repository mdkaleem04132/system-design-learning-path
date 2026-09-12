
class Solution(object):
    def maximumWeight(self, intervals):
        intervals = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: x[1]
        )

        n = len(intervals)

        ends = [x[1] for x in intervals]

        import bisect

        prev = []
        for l, r, w, idx in intervals:
            prev.append(bisect.bisect_left(ends, l))

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, idx = intervals[i - 1]
            p = prev[i - 1]

            for k in range(1, 5):
                skip_score, skip_indices = dp[i - 1][k]

                take_score, take_indices = dp[p][k - 1]
                take_score += w
                take_indices = tuple(sorted(take_indices + (idx,)))

                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return list(dp[n][4][1])
