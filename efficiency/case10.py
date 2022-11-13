# 如果需要在if中将某对象与多个其他对象进行对比判断，你可能会进行如下定义
data = "a"
if data == "a" or data == "b" or data == "c":
    print("HHH")


# 但是当对比对象增加时，很不方便，且可能存在拼写错误，所以通常会使用如下方式，也是我个人喜欢用的方法
datas = ["a", "b", "c"]
data = "a"
if data in datas:
    print("HHH")

# 11/13
