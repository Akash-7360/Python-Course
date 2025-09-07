# name = "Harry" #Strings are immutable

# #name[0] = "R" #it is not possible 

# a = len(name)
# print(a)

# s = "hello world"
# k= "HELLO WORLD"
# a= len(s)
# print(s.upper(), s)#the actual value of string doesnt change
# print(k.lower())
# print(s.capitalize())
# print(s.title())

# text ="  hello world  "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip())# Output: "hello world  "
# print(text.rstrip())# Output: "  hello world"

# text = "Python is fun"
# print(text.find("is"))
# print(text.replace("fun","cool"))

# text = "apple, banana, cherry"
# fruits = text.split(",")
# print(fruits)

# new_text= "-" .join(fruits)
# print(new_text)

text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())