# 下一个，如果需要对列表进行增删改操作，比如这个例子
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
