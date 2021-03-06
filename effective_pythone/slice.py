

#在原列表上切割一个新列表，对新列表进行操作不会影响原列表
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('original a:   ', a)
new = a[-5: -1]
print('before:   ', new)
new[1] = 99
print('after:  ', new)
print('no change:  ', a)


#在赋值时对左侧列表进行切片 把切片的起止地址都留空，那么就会产生一份原列表的拷贝
b = a[:]
assert b == a and b is not a


#对左侧直接进行赋值，此时改变右侧的内容 左侧也将改变 他们是绑在一起的 相互影响
b = a 
a[1] = 1111111
print('b=a, b changed then a also chage:  ', a)
a[2] = 555555
print('right already change:  ', b)


#把汉子 字节 字符串反转过来，
x = b'ilovepython'
y = x[::-1]
print(y)
x = 'qwerty'
y = '感谢'
x_ = x[::-1]
y_ = y[::-1]
print(x_, y_)



#但对编码成UTF-8字节串的unicode字符来说则无效
w = '谢谢'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
#以上的会报错



