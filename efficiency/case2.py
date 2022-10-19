# 下一个，如果需要对列表进行增删改操作，比如这个例子
# 增强for循环中不可以进行add和remove操作
case2 = [9, 8, 8, 3, 3, 1]
for i in case2:
    if i % 2 == 0:
        case2.remove(i)
print(case2)


# 在上一期中说过这样的操作是错误的，或许你意识到了列表是可变对象，直接对他操作会出问题，但还是喜欢写成如下形式
case2 = [9, 8, 8, 3, 3, 1]
out = []
for i in case2:
    if i % 2 != 0:
        out.append(i)
print(out)


# 但通常列表推导式是更简单更快的方式
# 列表推导式或者说列表解析式是一种非常简洁的创建列表的方式。
# [(x, x**2) for x in range(6) if]
# 三个部分组成：
# 1. 定义最终元素的表达形式
# 2. for循环初步定义列表
# 3. 可选：在for循环后面可以使用if语句进行过滤
case2 = [9, 8, 8, 3, 3, 1]
out = [x for x in case2 if x % 2 != 0]
print(out)

