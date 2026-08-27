class Solution(object):
    def lexGreaterPermutation(self, s, target):
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        def build(i):
            if i == len(target):
                # Exactly equal to target
                return None

            target_index = ord(target[i]) - ord('a')

            # 1. Try to keep the same character
            if count[target_index] > 0:
                count[target_index] -= 1

                result = build(i + 1)

                if result is not None:
                    return target[i] + result

                count[target_index] += 1

            # 2. Try the smallest character greater than target[i]
            for j in range(target_index + 1, 26):
                if count[j] > 0:
                    count[j] -= 1

                    # Fill remaining positions with smallest characters
                    result = ""

                    for k in range(26):
                        result += chr(k + ord('a')) * count[k]

                    return chr(j + ord('a')) + result

            return None

        answer = build(0)

        return answer if answer is not None else ""
        