# encoding:UTF-8
# 当你建立了一个列表，你可以逐项地读取这个列表，这叫做一个可迭代对象:
#
mylist = [1, 2, 3]
for i in mylist:
    print(i)
# 1
# 2
# 3

# mylist 是一个可迭代的对象。当你使用一个列表生成式来建立一个列表的时候，就建立了一个可迭代的对象:
#
mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)


# 0
# 1
# 4

# 所有你可以使用 for .. in .. 语法的叫做一个迭代器：列表，字符串，文件……
# 你经常使用它们是因为你可以如你所愿的读取其中的元素，
# 但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。

# yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。
#
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # create a generator
print(mygenerator)  # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(i)
# 0
# 1
# 4

'''
这个例子没什么用途，但是它让你知道，这个函数会返回一大批你只需要读一次的值.

为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。

那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

现在到了关键点了！

第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。这种情况可能因为是循环进行没了，或者是没有满足 if/else 条件。
'''
# 参考https://www.cnblogs.com/welhzh/p/7234376.html