import re
def hump2underline(hunp_str):
    '''
    驼峰形式字符串转成下划线形式
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    '''
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub

def dict_convert(old):
    new = {}
    for k in old:
        new_k = hump2underline(k)
        new[new_k] = old[k]
        if isinstance(new[new_k], dict):
            new[new_k] = convert(new[new_k])
    print(new)
    return new



if __name__ == __main__():


