
holyDays = ["Naw Ruz"]
print(holyDays)
print(holyDays[0])
print(f"the first Holy Day is: ", {holyDays[0]})


holyDays.append("Ridvan")
print(f"the second Twin Holy Day is: ", {holyDays[1]})
print(holyDays)

nawruz = holyDays.pop(0)
print(nawruz)
ridvan = holyDays.pop()
print(ridvan)
holyDays.append(ridvan)
holyDays.append(nawruz)
print(holyDays)

holyDays.append("Martyrdom of the Bab")
print(holyDays)
martyrdomOfTheBab = holyDays.pop()
print(martyrdomOfTheBab)
print(holyDays)

print(holyDays.__len__())