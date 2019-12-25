
# create a list with an item
holyDays = ["Naw Ruz"]
print("Baha'i Holy Days: ", holyDays)

# append an item to a list
holyDays.append("Ridvan")

# access the second item in the list
print("added: ", {holyDays[1]})

# print appended list
print("Baha'i Holy Days: ", holyDays)

# pop the first item
nawruz = holyDays.pop(0)
print("first popped item: " , nawruz)

# pop the second item
ridvan = holyDays.pop()
print("second popped item: ", ridvan)

# add both items back, reversing order
holyDays.append(ridvan)
holyDays.append(nawruz)
print(holyDays)

# add a third item
holyDays.append("Martyrdom of the Bab")
# access at final index, 2
print("added: ", holyDays[2])
print("Baha'i Holy Days: ", holyDays)

# prepare box for last item
martyrdomOfTheBab = holyDays.pop()
print("popped: ", martyrdomOfTheBab)

# print remaining items
print("Baha'i Holy Days: ", holyDays)

# print length
print("length of Holy Day list: ", holyDays.__len__())