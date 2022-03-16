- 字符串
    
    ```python
    # 首字母大写
    title() 
    # 全大写
    upper()
    # 全小写
    lower()
    # 字符串变量替代
    f"{变量名}"
    # 删除空白
    左 → lstrip()
    右 → rstrip()
    均 → strip()
    ```
    - 数
    
    ```python
    # 乘方运算
    **
    # 易读下划线
    14_000_000_000 → 14000000000
    # 同时赋值
    x,y,z=0,0,0
    # 索引
    [-x] 倒数
    ```
    - 列表
    
    ```python
    # 添加
    append()
    # 插入
    inster(index,"")
    # 删除
    del 变量[index]
    # 弹出
    pop()
    # 指定弹出
    pop(index)
    # 指定值删除
    remove("value")
    # 永久排序
    sort()
    # 临时排序
    sorted(list)
    # 翻转列表
    reverse()
    # 列表长度
    len(list)
    # range列表
    range(1,5): → 1 2 3 4
    # range偶数列表
    range(x,y,2)
    # 列表解析
    [value ** 2 for value in range(1,5)] → [1, 4, 9, 16]
    # 切片
    [起,末-1]
    # 副本
    another = other[:]
    # 元组(不可变)
    (,)
    ```
    - 字典（可嵌套）
    
    ```python
    # 访问
    dict[key]
    # 添加&修改
    dict[key]= value
    # 删除
    del dict[key]
    # get访问
    dict.get(key,不存在返回)
    # 遍历
    for key,value in dict.items():
    # 遍历键
    for key in dict.keys():
    # 遍历值
    for value in dict.values():
    # 删除多项指定
    while value in dict:
    	dict.remove(value)
    ```
    - 交互
    
    ```python
    # 输入
    input(提示)
    # 用户退出
    while message !='quit':
    	message = input("输入quit退出")
    ```
    - 函数
    
    ```python
    # 实参默认值
    def fun(value1,value2='default')
    # 实参可选
    def fun(value="")
    # 任意数量的实参
    def fun(*value) → 元组
    def fun(**value) → 字典
    # 特定函数别名
    from func import pyfile as 别名(func)
    import pyfile as 别名(pyfile)
    ```
    - 类
    
    ```python
    # 自动执行
    del __init__(self) 
    # 继承超类
    class 子类(父类):
    	def fun():
    		supper().父类fun()
    ```
    - 异常
    
    ```python
    try:
    	
    except 错误:
    ```