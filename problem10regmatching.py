from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        len1 = len(s)
        len2 = len(p)

        i = 0
        j = 0
        starflag = 0  # 0：之前无*标  1：之前有星标
        starletter = ''  #之前星标对应的字母

        while i<len1:
            if j>=len2 and starflag ==0:
                return False
            if starflag== 0:
                if j<len2-1 and p[j+1]=="*":
                    starflag = 1
                    starletter = p[j]
                    j+=2
                    continue
                else:
                    if s[i] == p[j] or p[j]==".":
                        i +=1
                        j +=1
                        continue
                    else:
                        return False

            if starflag == 1:  #当前处在星标状态
                if s[i] == starletter or starletter == ".":
                    i +=1
                else:
                    starletter=""
                    starflag = 0
                continue

        if j<len2:
            return False
        return True

if __name__ == '__main__':
    # s="aa"
    # p="a*"
    # print(Solution().isMatch(s,p))
    #
    # s = "ab"
    # p = ".*"
    # print(Solution().isMatch(s, p))

    # s = "mississippi"
    # p = "mis*is*p*."
    # print(Solution().isMatch(s, p))

    s = "ab"
    p = ".*C"
    print(Solution().isMatch(s, p))

    s = "aaa"
    p = "a*a"
    print(Solution().isMatch(s, p))