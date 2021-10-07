class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        mp = dict()
        for i in range(len(s1)):
            if s1[i] not in mp.keys():
                mp[s1[i]] = 0
            mp[s1[i]] += 1

        mp2 = dict()
        for i in range(len(s1) - 1):
            if s2[i] not in mp2.keys():
                mp2[s2[i]] = 0
            mp2[s2[i]] += 1

        start = 0
        for i in range(len(s1) - 1, len(s2)):
            if s2[i] not in mp2.keys():
                mp2[s2[i]] = 0

            mp2[s2[i]] += 1
            chk = True
            for key in mp2.keys():
                if key in mp.keys():
                    if mp[key] != mp2[key]:
                        chk = False
                        break
                elif mp2[key] != 0:
                    chk = False
                    break

            if chk:
                return True
            mp2[s2[start]] -= 1
            start += 1
        return False

# based on two pointers / sliding
