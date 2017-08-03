def prime(x):
    print x
    return

def swap(a, b, list, str):
    # c = a
    # a = b
    # b = c
    # global a
    a = 3
    b = 2
    str = 'c'
    list.append(2)
    return

prime('aaa')
a, b1, _list = 1, 2, [0, 1]
_str = 'a'
print a, b1, _list, _str
swap(a=a, b=b1, list=_list, str=_str)
print a, b1, _list, _str


def sign(val):
    if val > 0:
        return 'pos'
    elif val < 0:
        return 'neg'
    else:
        return 'zero'


for x in [-1, 0, 1]:
    print sign(x)


def hello(name, loud=False):
    if loud:
        print 'Hello,%s' % name.upper()
    else:
        print 'Hello,%s' % name


hello('Bob')
hello('Fred', loude=True);