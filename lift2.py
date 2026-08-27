class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

            # Continue matching target
            if freq[target_idx] > 0:
                freq[target_idx] -= 1
                prefix.append(target[i])
            else:
                break

        return answer
