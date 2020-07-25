"""
格式化输出

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# a = 1
# b = 5
# 1 + 5 = 6
# 1 - 5 = -4
# 1 * 5 = 5
# 1 / 5 = 0.200000
# 1 // 5 = 0
# 1 % 5 = 1
# 1 ** 5 = 1
