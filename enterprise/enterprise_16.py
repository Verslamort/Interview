# 输入某年某月某日，判断这一天是这一年的第几天？
import datetime

y = int(input('请输入4位数的年份:'))
m = int(input('请输入月份:'))
d = int(input('请输入哪一天:'))

targetday = datetime.date(y, m, d)  # 需要查询的日期
dayCount = targetday - datetime.date(targetday.year - 1, 12, 31)
print("%s是%s年的第%s天。" % (targetday, y, dayCount.days))

