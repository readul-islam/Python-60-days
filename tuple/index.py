this_tuple = ('apple', 'banana', 'orange')
convert_tuple_to_list = list(this_tuple)

convert_tuple_to_list[0] = 'Mango'

convert_list_to_tuple = tuple(convert_tuple_to_list)


another_tuple = ('eggs',)

this_tuple += another_tuple
print(this_tuple)


(food1, food2, food3, food4) = this_tuple


print(food1)
