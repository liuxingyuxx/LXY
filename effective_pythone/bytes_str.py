"""
python3中有两种表示字符序列的类型：
    bytes和str 
编写程序的时候一定要把编码和解码操作放在界面最外围来操作，程序的核心部分应该使用Unicode字符类型（最常见的编码方式是utf-8）（也就是python3中的string python2中的Unicode 
"""

#在python3中我们接受str或bytes并且总返回str或者bytes的方法
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str 
    return value 

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str 
    return value


#对于python3给open函数添加了默认参数值'utf-8‘，要求传入的默认值必须是包含Unicode字符的str，所以不接受二进制格式和bytes实例。不能直接采用字符写入模式’w'，必须要用二进制写入模式'wb'来开启操作文件
with open('/tmp/random(10)', 'wb') as f:
    f.write(os.urandom(10))



