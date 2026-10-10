
class Solution:
    def reverse(self, x: int) -> int:
        strDigits = list(str(x))

        strDigits.reverse()

        if x == 0:
            return 0
        elif x < 0:
            result = -(int(''.join(strDigits[:-1])))
        else:
            result = int(''.join(strDigits))

        if result < -(2**31) or result > 2**31 - 1:
            return 0

        return result
