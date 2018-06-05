#用列表推导式来代替map filter 

a = [x for x in range(10)]
print('orignal', a)

#除非是只调用一个参数的情况， 否则使用map要用lambda函数

square = [x*x for x in a]
even_square = [x*x for x in a if x%2 == 0]
print('square:  ', square)
print('even_square:  ', even_square)
#使用map filte会达到同样的效果但会很复杂
alt = map(lambda x:x**2, filter(lambda x: x % 2 == 0, a))
print(alt, list(alt))


#列表推导也支持多重循环 这些for表达式会从左至右循环
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
square = [[x**2 for x in row] for row in matrix]
print('muti level  ', flat, square)



