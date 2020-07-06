
# 运算符

# 算术运算符

a = 12
b = 20
c = 4
aa = 'aa'
bb = 'bb'

print(a + b, aa + bb, a * b)  # 加减乘除
print(str(10) + 'aa')
print('abc' * 3)
print(10 % 3)  # 取模，得范围内的数，如（对10取余，得0~9）
print(a**c)  # 幂 a^c
print(10 // 3)  # 取整

# ===============
# 比较运算符 返回 True or False

print(a == b, a != b, a > b, a >= b, a < b, a <= b)

# ===============
# 赋值运算符 =

x = 5
print(x)
x += 1
print('自加1：', x)  # a+=1 等于a=a+1 无a++
x -= 1
print("自减1：", x)
x *= 2
print('自乘2', x)
x /= 3
print("自除3：", x)
x //= 1
print('对1取整：', x)
x **= 2
print('2的幂次：', x)
x %= 4
print('对4取模：', x)

# ===============
# 逻辑运算符 and or not
t = True
f = False

print(t and f, t and t, f and f)
print(t or f, t or t, f or f)
print(not t, not f)

# 整数只有0是False，其余都是True
print(1 and 2, 1 and 0, 0 and 1, 0 and 0)  # 有0 都是0，都为True,输出后面一个数
print(1 or 2, 1 or 0, 0 or 1, 0 or 0)  # 都是True,输出前一个数，后面的就不去执行了。

# ================
# 位运算符 将数值转化成二进制，再做计算，再转化回来

print('6的二进制位：', bin(6))
print('10的二进制位：', bin(10))
print('6&10：', 6 & 10, '，其二进制：', bin(6 & 10))
print('6|10：', 6 | 10, '，其二进制：', bin(6 | 10))
print('6^10：', 6 ^ 10, '，其二进制：', bin(6 ^ 10))  # 对应二进位相异为1，相同为0
print('~6：', ~6, '，其二进制：', bin(~6))  # 不理解！等于-x-1
print('~10：', ~10, '，其二进制：', bin(~10))
print('6<<1：', 6 << 1, '，其二进制：', bin(6 << 1))  # 从高位开始整体左移
print('6<<3：', 6 << 3, '，其二进制：', bin(6 << 3))  # a<<b相当于a*a**b
print('6>>1：', 6 >> 1, '，其二进制：', bin(6 >> 1))  # 从高位开始整体右移
print('6>>2：', 6 >> 2, '，其二进制：', bin(6 >> 2))
print('6>>3：', 6 >> 3, '，其二进制：', bin(6 >> 3))
print('6>>4：', 6 >> 4, '，其二进制：', bin(6 >> 4))  # 当右移至没有位数后，为0

# ==============
# 成员运算符 返回T or F

setA = [1, 2, 3]
setB = [1, 2]
setC = ['a', 'b']

print('10 in setA：', 10 in setA)  # 询问成员是否在集合里（可数字，可字符串
print('2 in setA：', 2 in setA)
print('setB in setA：', setB in setA)
print('a in setC：', 'a' in setC)
print()
print('10 not in setA：', 10 not in setA)  # 询问成员是否不在集合里（可数字，可字符串
print('2 not in setA：', 2 not in setA)
print('setB not in setA：', setB not in setA)
print('a not in setC：', 'a' not in setC)

# ===============
# 身份运算符 is 比较的是地址，== 比较的是值

A = B = 20
setD = [1, 2, 3]
setE = setD[:]  # setE 复制 setD的内容

print('A is B：', A is B, '，其中id(A)：', id(A), '，id(B)：', id(B))
print('A is B：', A is not B, '，其中id(A)：', id(A), '，id(B)：', id(B))

print(
    'setD is setE：',
    setD is setE,
    '，其中id(setD)：',
    id(setD),
    '，id(setE)：',
    id(setE),
    'setD==setE：',
    setD == setE)
