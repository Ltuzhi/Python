
# 第3节课

# 标识符（字母、数字（不可开头）、下划线组成，区分大小写
import keyword  # 导入keywod库
name = "ltuzhi"
Name = "Ltuzhi"
print(name, Name)

# 输出系统的关键字（保留字）
print(keyword.kwlist)

# ====================
print('=' * 20)
# 变量 （不用声明，用前先赋值（类似MATLAB），可多个变量连续赋值）
num1 = 123
print(type(num1))
num2 = "abc"  # 赋值字符要加引号啊！！！
print(type(num2))

# 多值赋值
a = b = c = 10
x, y, z = 10, 20, 30
print(a, b, c, x, y, z)

# ====================
print('=' * 20)

# 缩进（Pyhon一大特色，用缩进表示代码块，而不是C or Java 的{}

num = input("请输入1或2：")  # 还不会回车
if num == 1:     # 别忘记冒号！！
    print("谢谢你来看我！")
else:  # 这里也有冒号！（怎么不能使用else if？？）
    print("要一起加油学Pyhon！")


# 为什么我的if是错的？怎么输入都是执行else语句？？？？？
