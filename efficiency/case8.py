# 定义一个列表，里面存放字符串对象，如果想实现拼接，由于字符串是不可变对象，很多人会定义空字符串进行遍历拼接，但，对于大型字符串可能会导致特别慢
data = ["Hi", "my", "data"]
newdata = ''
for i in data:
    newdata += i + " "
print(newdata)


# 更优的方案是使用join，实现将列表中内容进行全部拼接
data = ["Hi", "my", "data"]
newdata = " ".join(data)
print(newdata)


# join前引号中的内容将作为分隔符，例如将其换成逗号将输出如下内容
data = ["Hi", "my", "data"]
newdata = ",".join(data)
print(newdata)
