from itertools import combinations_with_replacement, permutations
# set the char_set elements out of which you want to make your possible password strings 
char_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pass_length = int(input("Enter password length: "))
# step 1:
pass_set_1 = list(combinations_with_replacement(char_set, pass_length))
pass_set_2 = list()
# step 2:
for i in pass_set_1:
    temp = set(permutations(i))  # to avoid duplicate possibilities. set stores unique elements
    pass_set_2.append(tuple(temp))
pass_set_3 = set()
# step 3:
for i in pass_set_2:
    for j in range(len(i)):
        pass_set_3.add(i[j])
pass_set_4 = list()
# step 4:
for i in pass_set_3:
    string = ''
    for j in i:
        string += str(j)
    pass_set_4.append(string)
my_num = input(f"Enter your {pass_length} digit password: ")
count = 0
# checking our pass in the list of all possible passwords of given pass length
for i in pass_set_4:
    count += 1
    if my_num == i:
        print(f"pass found at attempt no.  {count}")
        break