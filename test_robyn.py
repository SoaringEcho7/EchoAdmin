from robyn import Robyn

app = Robyn(__file__)

# 查看所有属性和方法
print("\n=== 所有属性和方法 ===")
print(dir(app))

# 查看帮助文档
print("\n=== 帮助文档 ===")
help(app)
