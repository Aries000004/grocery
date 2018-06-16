---
title: 05-Python yield函数,生成器
date: 2018-02-13 20:10:43
tags: Python基础
---

<h4 style="color: #228B22;">yield函数简单用法, 后续会继续添加..

</h4>



### `sys`

- 在Linux系统命令行参数  在输入命令是给的参数 
- `sys.argv`  接受所有的参数  保存在数组中

### `yield`

```python
# 生成式   列表已存在,占用空间大
list1 = [x for x in range(10)]

#生成器    得到的是 generator  对象 引用 
list3 = (x for c in range(10))
for i in list3:   # 在需要用的时候再计算出值
    print(i)
   
# 生成器函数
def fibo(n):  #普通函数 
    a, b = (0, 1)
    for _ in range(n):
        a, b = b, a + b
    return a

def fibo(n):  #生成器函数   保留上次计算的值 不会重复计算 
    a, b = (0, 1)
    for _ in range(n):
        a, b = b, a + b
    	yield a
```

```python
string.center(占据的位置大小, [,空位填补])
string.ljust()
string.rjust()
# 二选一列表
[[0], [1]][True] = [1]
[[0], [1]][False] = [0]

```



