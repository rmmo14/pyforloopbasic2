# 1. Big size
# def biggie(mylist):
#     empty = []
#     for x in range (0,len(mylist)):
#         if mylist[x] > 0:
#             empty.append('big')
#         else:
#             empty.append(mylist[x])
#     print(empty)
#     return empty
# holder = biggie([-1, 2, 3, -5])

# 2. count positives
# def counting(my_list):
#     count = 0
#     empty = []
#     for x in range (0,len(my_list)):
#         if my_list[x] > 0:
#             count += 1
#     my_list[len(my_list) - 1] = count
#     print (my_list)
#     return my_list
# holder = counting([-1, 2, -3, 9, -3, -4])

# 3. sum total
# def sumtotal(mylist):
#     sum = 0
#     for x in range (0, len(mylist)):
#         sum += mylist[x]
#     print (sum)
#     return sum
# hold = sumtotal([1,2,5,6])

# 4. average
# def average(my_list):
#     sum = 0
#     for x in range (0,len(my_list)):
#         sum += my_list[x]
#     avg = sum / len(my_list)
#     print(avg)
#     return avg
# holder = average([2,3,5,6,4])

# 5. length
# def length(mylist):
#     holder = len(mylist)
#     print(holder)
#     return holder
# hold = length([2,3,4,5,6,7])

# 6. minimum 
# def min(my_list):
#     if my_list == []:
#         print("False")
#         return False
#     else:
#         min = my_list[0]
#         for x in range (0,len(my_list)):
#             if my_list[x] < min:
#                 min = my_list[x]
#         print(min)
#         return min
# holder = min([1,2,3,-1])

# 7. maximum 
# def max(mylist):
#     if mylist == []:
#         print("False")
#         return False
#     else:
#         max = mylist[0]
#         for x in range (0, len(mylist)):
#             if mylist[x] > max:
#                 max = mylist[x]
#         print(max)
#         return max
# hold = max([])

# 8. ulti analysis
# def ult(my_list):
#     if my_list == []:
#         print("False")
#         return False
#     else: 
#         dicto = {}
#         min = my_list[0]
#         max = my_list[0]
#         sum = 0
#         for x in range (0,len(my_list)):
#             sum += my_list[x]
#             if my_list[x] > max:
#                 max = my_list[x]
#             elif my_list[x] < min:
#                 min = my_list[x]
#         avg = sum / len(my_list)
#         dicto['min'] = min
#         dicto['max'] = max
#         dicto['avg'] = avg
#         dicto['length'] = len(my_list)
#         print(dicto)
#         return dicto
# holder = ult([2,3,4,5,6,4])
# potato = ult([-1,-1,-2,-1,0])

# 9. reverse list
def revlist(mylist):
    length = len(mylist) - 1
    for x in range (int(len(mylist)/2)):
        temp = mylist[length - x]
        mylist[length - x] = mylist[x]
        mylist[x] = temp
    print(mylist)
    return mylist

# def reverse_list(nums_list):
#     list_len = len(nums_list)
#     for idx in range(int(list_len/2)):
#         temp = nums_list[list_len-1-idx]
#         nums_list[list_len-1-idx] = nums_list[idx]
#         nums_list[idx] = temp
#         print(nums_list)
#     return nums_list

print(revlist([3, 1, 8, 10, -5, 6]))