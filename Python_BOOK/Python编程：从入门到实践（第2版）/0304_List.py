"""
    列表概念 2022.3.13 hackerBaidan
"""
print("=========列表概念 2022.3.13 hackerBaidan=========")
# 访问列元素
bicycles =["trek","cannondale","redline","specialized"]
print(bicycles[0].title())
# 修改列元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
# 添加列元素
motorcycles.append("honda")
print(motorcycles)
# 插入列元素
motorcycles.insert(0,"shanghai")
print(motorcycles)
# 删除列元素
del motorcycles[0]
print(motorcycles)
# 弹出获取
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 指定弹出
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
# 指定值删除
motorcycles.remove("ducati")
print(motorcycles)
# 永久排序
cars =['bmw','audi','toyota','subaru']
sorted(cars)
print(cars)
print(sorted(cars))
cars.sort()
print(cars)
# 翻转列表
cars =['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)
# 列表长度
print(len(cars))
"""
    操作列表 2022.3.13 hackerBaidan
"""
print("=========操作列表 2022.3.13 hackerBaidan=========")
# 遍历列表
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
# range列表
numbers = list(range(1,6))
print(numbers)
# range偶数列表
even_numbers =list(range(2,11,2))
print(even_numbers)
# 列表解析
squares = [value **2 for value in range(1,11)]
print(squares)
"""
    列表切片 2022.3.13 hackerBaidan
"""
print("=========列表切片 2022.3.13 hackerBaidan=========")
# 遍历切片
players=['charles','martina','michael','florence','eli']
print(players[0:3])
for player in players[:3]:
    print(player.title())
# 复制切片
other_players = players[:]
print(other_players)
"""
    元组 2022.3.13 hackerBaidan
"""
print("=========元组 2022.3.13 hackerBaidan=========")
# 访问元组元素
diemensions=(200,50)
print(diemensions[0])
