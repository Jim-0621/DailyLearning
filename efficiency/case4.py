# 下一个知识点，现在有一个包含多个值的列表，但存在重复值，如果需要去重，最简单的做法是将我们的list转为set，会自动进行重复值的删除
data = [1, 1, 2, 3, 3, 4, 5, 5, 7]
new_data = set(data)
print(new_data)


# 关于集合set，常见的用法是在两组数据中进行运算
# 求交集
data_1 = {'Mathematics', 'Chinese', 'English', 'Physics', 'Chemistry', 'Biology'}
data_2 = {'Mathematics', 'Chinese', 'English', 'Politics', 'Geography', 'History'}
print(data_1 & data_2)


# 求并集
data_1 = {'Mathematics', 'Chinese', 'English', 'Physics', 'Chemistry', 'Biology'}
data_2 = {'Mathematics', 'Chinese', 'English', 'Politics', 'Geography', 'History'}
print(data_1 | data_2)


# 求差集
data_1 = {'Mathematics', 'Chinese', 'English', 'Physics', 'Chemistry', 'Biology'}
data_2 = {'Mathematics', 'Chinese', 'English', 'Politics', 'Geography', 'History'}
print(data_1 - data_2)


# 求不同时包含于两集合中的数据
data_1 = {'Mathematics', 'Chinese', 'English', 'Physics', 'Chemistry', 'Biology'}
data_2 = {'Mathematics', 'Chinese', 'English', 'Politics', 'Geography', 'History'}
print(data_1 ^ data_2)
