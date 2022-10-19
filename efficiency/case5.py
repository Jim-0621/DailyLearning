# 下一个，当我们有一个包含很多数据的列表，如果执行如sum等操作，可能会出现内存问题
# 这里用了我们之前在case2提到的列表推导式
data = [i for i in range(10000)]
print(sum(data))


# 但是如果将中括号改成小括号，即变成生成器，将提升效率
data = (i for i in range(10000))
print(sum(data))


# 为方便对比，我们导入Python标准库sys进行演示，可以看到生成器的方式将大大节省空间
import sys

data_1 = [i for i in range(10000)]
print(sys.getsizeof(data_1), "bytes")

data_2 = (i for i in range(10000))
print(sys.getsizeof(data_2), "bytes")
