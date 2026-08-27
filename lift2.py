class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(s)
        prefix = []
        answer = ""

     
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
