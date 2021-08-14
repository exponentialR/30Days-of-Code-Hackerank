# Task
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  name is not found, print Not found instead.
#
#
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.
# **Sample Input**
#
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
#
#
# **Sample Output**
#
# sam=99912222
# Not found
# harry=12299933
#



N = int(input())
phone_book = {}
for i in range(N):
    x = input().split()
    phone_book[a[0]] = x[1]

for m in range(N):
    y = str(input())
    if y in phone_book:
        print(str(y) + '=' + str(phone_book[y]))
    else:
        print('Not found')