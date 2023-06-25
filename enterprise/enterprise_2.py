# 反转一个整数，例如-123 --> -321
# 方法1
a = -123
b = -int(str(abs(a))[::-1])
print(b)


# 方法2
class Solution(object):
    def reverse(self, x):
        # 整数为个位数时
        if -10 < x < 10:
            return x
        str_x = str(x)
        # 整数为正数时
        if str_x[0] != '-':
            str_x = str_x[::-1]
            x = int(str_x)
        # 整数为负数时
        else:
            str_x = str_x[1:][::-1]  # 取数字反转
            x = -int(str_x)
        return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-123)
    print(reverse_int)
