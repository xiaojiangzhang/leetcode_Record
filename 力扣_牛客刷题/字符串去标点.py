# 编一个程序，从 string 对象中去掉标点符号。要求输入到程序的字符串必须含
# 有标点符号，输出结果则是去掉标点符号后的 string 对象

'''
样例输入
String：a1,b2.c3-d4!

样例输出
Enter a string:

Result:

Stringa1b2c3d4
'''
print("Enter a string:")
string = input()
re = str()
for i in string:
    if 47 < ord(i) < 58 or 64 < ord(i) < 91 or 96 < ord(i) < 123:
        re += i
if re:
    print("Result:")
    print(re)
else:
    print("")
