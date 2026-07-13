# list

# empty_list = []
# nums = [1, 2, 3, 4, 5]
# shopping_list = ['apple', 'kiwi', 'mango']
# user_items = ['Abe' , 100, True]

# print(len(empty_list))
# print(len(nums))
# print(len(shopping_list))
# print(len(user_items))
# print("==========================")
# print(nums[2])
# print(shopping_list[-1])
# print(nums[1:3])


# =========== Tuples ===========

tup1 = (1,)
tup2 = (1, "Shivani", 3, [])

tup2[3].append("Saanvi")
print(tup2)


values  = [35, 74, 663, 89, 56]
def min_and_max(args):
    min = sorted(args)[0]
    max = sorted(args)[-1]
    return (min, max)

print(min_and_max(values))