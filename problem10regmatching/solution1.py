from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True

if __name__ == '__main__':
    s="aa"
    p="a"
    print(Solution().isMatch(s,p))
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
    p = ".*a"
    print(Solution().isMatch(s, p))