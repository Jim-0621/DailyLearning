# 如果你需要对可迭代对象进行排序，比如列表、元组、字典，首先以列表为例子，可以直接使用内置函数sorted完成任务
# 可迭代对象的概念及其使用：
# 　　可迭代对象，即可以进行迭代操作的一类对象。
# 　　迭代是访问集合元素的⼀种⽅式。迭代器是⼀个可以记住遍历的位置的对象。迭代器对象从集合的第⼀个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 　　迭代是对元素进行的一种遍历，python语法 for element in Iterable:
data = [-1, -10, 0, 9, 5]
new_data = sorted(data)
print(new_data)


# 如果想使用降序，可以将参数reverse设置为True
data = [-1, -10, 0, 9, 5]
new_data = sorted(data, reverse=True)
print(new_data)


# 同样的适用于元组，但注意此时输出类型变成了列表
data = (-1, -10, 0, 9, 5)
new_data = sorted(data, reverse=True)
print(new_data)


# 如果需要对复杂的可迭代对象进行排序，比如列表中的元素为字典类型，在这个例子中，需要按age大小对列表进行排序，那么可以在参数key这使用匿名函数lambda
data = [
    {"name" : "jia", "age" : 18},
    {"name" : "yi", "age" : 60},
    {"name" : "bing", "age" : 20}
]
new_data = sorted(data, key= lambda x: x["age"])
print(new_data)
