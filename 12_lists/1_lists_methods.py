#lists are ordered , mutable(changable) collection of items
marks = [11, 22, 33, 44, 55]

mixed = [11 ,"Hello", False, 4.2]

print(marks)

# print(mixed)

# print(marks[2:4])
# print(mixed[2])

marks.append(63)
print(marks)
marks.pop()
print(marks)

marks.extend(mixed)
print(marks)