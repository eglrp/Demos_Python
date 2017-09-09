# coding:UTF-8
# 参考这个帖子，基本都有 http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
import re

pattern = re.compile("\\w+@\\w+\\.\\w{1,3}", re.I)  # 忽略大小写

match = pattern.match("a@qq.commcmd@126.cn")
# match是要求必须匹配，所以这里只能匹配到a@qq.com,如果是1a...直接就匹配不到了

if match:
    print match.group(0)

# 或者直接
match = re.match('@\\d+', '@123')
print match.group(0)


#  替换
'''
sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):
使用repl替换string中每一个匹配的子串后返回替换后的字符串。
当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
count用于指定最多替换次数，不指定时全部替换。
'''

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print p.sub(r'\2 \1', s)  # sub执行替换，\1 \2 引用分组


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print p.sub(func, s)