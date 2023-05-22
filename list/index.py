#List 

boys=['akash', 'sagor', 'manu', 'jubayer'];
#changeable, ordered and allow duplicates


# add list items


#add items to the end of the list use append();

boys.append('Hridoy')




# to insert a list item specified index use the insert();
boys.insert(0,'Suvro')



# Extend List
# To append elements from another list to the current list, use the extend() method.

boys1=['Asadul', 'Emon','Robin'];


boys.extend(boys1);


# Remove Specified Item 
# The remove() method removes the specified item.


boys.remove('akash')
boys.pop()

#The del keyword also removes the specified index:

boys.clear()
print(boys);



# Loping on list items

lang=['javascript', 'python', 'c++', 'c', 'dart'];


for x in lang:
    print(x);
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable. 
print(range(len(lang)))
for i in range(len(lang)):
    print(i)   
    
    
# While loop
# Remember to increase the index by 1 after each iteration.  

i =0;
while i < len(lang):
    print(lang[i]);
    i+=1




