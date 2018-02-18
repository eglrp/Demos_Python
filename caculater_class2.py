# -*-coding:UTF-8 -*-
# __author:"Lio"
# date: 2018/1/28

import re


# 格式规范化
def format_string(string):
    string = string.replace('--', '+')
    string = string.replace('++', '+')
    string = string.replace('+-', '-')
    string = string.replace('-+', '-')
    string = string.replace('*+', '*')
    string = string.replace('/+', '/')
    string = string.replace(' ', '')
    return string


# 检查输入是否合法
def check_expression(string):
    check_result = True
    if not string.count('(') == string.count(')'):
        print('表达式错误，括号未闭合！')
        check_result = False
    if re.findall('[a-z]+',string.lower()):
        print('表达式错误，包含非法字符！')
        check_result = False
    return check_result


# 乘除运算
def calc_mul_div(string):
    regular = '\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*'
    while re.findall(regular, string):
        expression = re.search(regular, string).group()
        if expression.count('*') == 1:
            x, y = expression.split('*')
            mul_result = str(float(x) * float(y))
            string = string.replace(expression, mul_result)
            string = format_string(string)
        if expression.count('/'):
            x, y = expression.split('/')
            div_result = str(float(x) / float(y))
            string = string.replace(expression, div_result)
            string = format_string(string)
        if expression.count('*') == 2:
            x, y = expression.split('**')
            pow_result = 1
            for i in range(int(y)):
                pow_result *= int(x)
                string = string.replace(expression, str(pow_result))
            string = format_string(string)
    return string


# 加减运算
def calc_add_sub(string):
    add_regular = '[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
    sub_regular = '[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*'
    while re.findall(add_regular, string):
        add_list = re.findall(add_regular, string)
        for add_str in add_list:
            x, y = add_str.split('+')
            add_result = '+' + str(float(x) + float(y))
            string = string.replace(add_str, add_result)
        string = format_string(string)

    while re.findall(sub_regular, string):
        sub_list = re.findall(sub_regular, string)
        for sub_str in sub_list:
            numbers = sub_str.split('-')
            # -3-5回返回3个值
            if len(numbers) == 3:
                result = 0
                for v in numbers:
                    if v:
                        result -= float(v)
            else:
                x, y = numbers
                result = float(x) - float(y)
            string = '+' + string.replace(sub_str, str(result))
        string = format_string(string)
    return string


if __name__ == '__main__':
    source = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    if check_expression(source):
        print('source:', source)
        print('eval result:', eval(source))
        source = format_string(source)

        while source.count('(') > 0:
            strs = re.search('\([^()]+\)', source).group()
            replace_str = calc_mul_div(strs)
            replace_str = calc_add_sub(strs)
            # 将括号的字符串替换为计算结果，结果包含（），替换时去掉（），既可以用[1:-1]
            source = format_string(source.replace(strs, replace_str[1:-1]))

        else:
            replace_str = calc_mul_div(source)
            replace_str = calc_add_sub(replace_str)
            source = source.replace(source, replace_str)
        print('my result:', source.replace("+", ""))

