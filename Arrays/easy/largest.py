# 1.find largest in an array
array = [1,3,6,7,9]
max_element=array[0]

for x in array:
    if x>max_element:
        max_element=x
print("largest element in an array is ",max_element)

#time complexity = o(n)
#space complexity = o(1)