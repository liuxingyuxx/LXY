#两个内置函数format 和 enumerate 都是从0开始的

list_a = ['a', 'b', 'c', 'd']
for i,v in enumerate(list_a):
    print('{0} : {1}'.format(i+1, v))
