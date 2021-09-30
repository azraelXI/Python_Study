import re

# #findall:匹配字符串中所有符合正则的内容
# lst=re.findall(r"\d+","我的电话号码是10086，我女朋友的电话是10010")
# print(lst)
#
# #finditer:匹配字符串中所有的内容【返回的是迭代器】
# it = re.finditer(r"\d+","我的电话号码是10086，我女朋友的电话是10010")
# for i in it:
#     print(i.group())

# #search找到一个结果就返回，返回的结果是match对象。拿数据需要.group()
# s=re.search(r"\d+","我的电话号码是10086，我女朋友的电话是10010")
# print(s.group())

# #预加载正则表达式
# obj=re.compile(r"\d+")
