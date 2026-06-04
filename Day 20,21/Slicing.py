python_list = ["a","b","c","d","e","f"]

print(python_list[1:]) #returns the list starting from index 1 till end
print(python_list[3:5]) #returns the list from index 3 to 5 (index 5 is not inclusive)
print(python_list[1:5:2]) #returns the list starting from index 1 till index 4 (5 not inclusive) incrementing by 2
print(python_list[5:1:-1]) #retunrs the list starting from index 5 till index 2 (1 not inclusive ) decrementing by 1
print(python_list[4::-1]) #starting from index 4 decrements by 1 till the end of list


#refer readme file for understanding below 4 statements :
print(python_list[:2:-1])
print(python_list[:2:1])
print(python_list[2::1])
print(python_list[2::-1])

#strings , lists and tuples can be sliced.