numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e_count=0
o_count=0
for number in numbers:
    if number%2==0:
        e_count+=1
        print(e_count)
    else:
        o_count +=1


print("Even numbers in the list: ", e_count)
print("Odd numbers in the list: ", o_count)