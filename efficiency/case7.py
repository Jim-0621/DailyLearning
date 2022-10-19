# 如果想完成字符串中某位置插入某对象的格式化操作，f-Strings将会是一个不错的方式
name = "sds"
data = f"Hi {name}"
print(data)


# 还可以在大括号内进行运算，这是Python3.6开始支持的新的格式化操作，相比以前更简洁方便。
i = 9
data = f"{i} * {i} = {i * i}"
print(data)
