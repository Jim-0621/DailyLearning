# 如果想合并两个字典，无需遍历对比判断键，只需使用如下语法即可达到目的
# 需要在Python3.5+中运行
data_1 = {"name" : "sds", "age" : "18"}
data_2 = {"name" : "sds", "uid" : "6688"}
out_data = {**data_1, **data_2}
print(out_data)

