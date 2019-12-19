"""
data type的使用
data type的转换
按位操作符的使用

"""
c = int('11',2)#c为'11'的十进制表示


print("int('11',2) = %d" % c)
c= 2 & 1#按位运算先将十进制转为二进制 本例中：2 & 1 == 10 & 01 = 0
print('2 & 1 = %d' % c)


c = 10#二进制表示：1010
c = c << 2#左移两位，即：c = 101000 = 40
print('c << 2 = %d' % c)

a = int(input("a = "))
b = str(a)

print(type(a))#不使用print不会输出type
print(type(type(a)))#type(a)的数据类型是type
print(type(b))
print(type(str(a)))#类型转换的函数并不会影响原有变量的数据类型
print(type(a))
print('%s' % a)

"""
is 和 == 的区别

"""
a = ['I ' 'love ' 'python']
print(a)
b = a
print(b)
print(a == b)#true
print(a is b)#true
b = ['I ' 'love ' 'python']
print(a == b)#true
print(a is b)#false