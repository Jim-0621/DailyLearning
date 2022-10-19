# 下一个，定义一个拥有不同键值对的字典，正常情况下当你获取字典中不存在的键时会报错
# data = {"name" : "sds", "age" : "18"}
# uid = data["uid"]
# print(uid)


# 而你在工程文件中经常会注意到使用get方法，避免因键不存在而引起的程序崩溃，若索引不到，将返回在第二个位置定义的参数
data = {"name": "sds", "age": "18"}
uid = data.get("uid", "6688")
print(uid)


# 类似的还有setdefault，如果键不存在于字典中，将会添加键并将值设为默认值，这些非常实用
data = {"name": "sds", "age": "18"}
uid = data.setdefault("uid", "6688")
print(uid)
print(data)
