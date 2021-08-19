grocery_list=['Juice', 'tomatoes', 'potatoes', 'apple', 'bannana']

print('first item', grocery_list[0])
print('second item', grocery_list[1])
print('third item', grocery_list[2])
print('fourth item', grocery_list[3])
print('fifth item', grocery_list[4])

grocery_list[0] = 'Green Juice'
print('first item', grocery_list[0])

print(grocery_list[1:3])
#dosen't print 3
                                
other_events=['Wash car', 'Pick up kids','Cash check']
to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1,'pickle')

grocery_list.remove('pickle')

grocery_list.sort()
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)
#grocery list effects to do list

to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

