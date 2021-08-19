#a tuple is like a list that is harder to change it's values
pi_tuple = (3,1,4,1,5,9)

#how to change tuple values

new_tuple = list(pi_tuple) #now its a list
pi_tuple.remove("1")
new_list = tuple(pi_tuple) #back to a tuple

len(tuple)
min(tuple)
max(tuple)
