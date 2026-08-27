class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(s)
        prefix = []
        answer = ""

        for i in range(n):
            target_idx = ord(target[i]) - ord('a')

            # Try choosing the smallest character greater than target[i]
            for j in range(target_idx + 1, 26):
                if freq[j] > 0:
                    freq[j] -= 1

                    result = prefix + [chr(j + ord('a'))]

                    # Add remaining characters in sorted order
                    for k in range(26):
                        result.extend([chr(k + ord('a'))] * freq[k])

                    candidate = "".join(result)

                    if answer == "" or candidate < answer:
                        answer = candidate

                    freq[j] += 1
                    break

            # Continue matching target
            if freq[target_idx] > 0:
                freq[target_idx] -= 1
                prefix.append(target[i])
            else:
                break

        return answer
