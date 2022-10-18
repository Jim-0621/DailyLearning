# 假设现在需要遍历列表，且要用到其位置索引进行相应数据操作，通常会习惯写成如下形式
data = [1, 4, 5, 7, 9]
for i in range(len(data)):
    if data[i] % 2:
        data[i] = 0
print(data)

# 但更好的方式是使用Python的内置枚举函数enumerate，可以直接获取到相应值及其索引
data = [1, 4, 5, 7, 9]
for idx, num in enumerate(data):
    if num % 2:
        data[idx] = 0
print(data)