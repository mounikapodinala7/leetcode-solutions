class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            r = ord(s2[right]) - ord('a')
            count2[r] += 1
            if count2[r] == count1[r]:
                matches += 1
            elif count2[r] == count1[r] + 1:
                matches -= 1

            l = ord(s2[left]) - ord('a')
            count2[l] -= 1
            if count2[l] == count1[l]:
                matches += 1
            elif count2[l] == count1[l] - 1:
                matches -= 1

            left += 1

        return matches == 26
