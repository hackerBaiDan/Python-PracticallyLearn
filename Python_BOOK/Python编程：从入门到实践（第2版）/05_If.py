"""
    If 2022.3.13 hackerBaidan
"""
print("=========If 2022.3.13 hackerBaidan=========")
# if 格式
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car =="bmw":
        print(car.upper())
    else:
        print(car.title())
# 多个条件
age_0=22
age_1=18
print(age_0 >=21 and age_1>=21)
print(age_0 >=21 or age_1>=21)
# 检查包含
requested_toppings =['mushrooms','onions','pineapple']
print('onions' in requested_toppings)
if 'marie' not in requested_toppings:
    print(f"marie not in")