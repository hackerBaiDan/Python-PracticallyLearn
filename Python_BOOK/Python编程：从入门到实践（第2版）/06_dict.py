"""
    dict 2022.3.14 hackerBaidan
"""
print("=========dict 2022.3.14 hackerBaidan=========")
# 访问字典中的值
alien_0={'color':'green'}
print(alien_0['color'])
# 添加字典的值
alien_0['x_position']=0
alien_0["y_position"]=25
print(alien_0)
# 修改字典中的值
alien_0['color']="red"
print(alien_0)
# 删除字典中的值
del alien_0['color']
print(alien_0)
# get访问
point_value = alien_0.get("points","No point value assigned.")
print(point_value)
# 遍历
for key,value in alien_0.items():
    print(key,value)

"""
    nesting 2022.3.14 hackerBaidan
"""
print("=========nesting 2022.3.14 hackerBaidan=========")
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)