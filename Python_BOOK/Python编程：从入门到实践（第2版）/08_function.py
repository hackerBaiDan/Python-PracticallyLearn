"""
    func 2022.3.14 hackerBaidan
"""
print("=========func 2022.3.14 hackerBaidan=========")
# 实参默认值
def describe_pet(pet_name,animal_type='dog'):
    print(f'I have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name='while')
# 实参可选
def get_formatted_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('jimi','hendrix','lee')
print(musician)
# 任意数量的实参
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='physics')
print(user_profile)
