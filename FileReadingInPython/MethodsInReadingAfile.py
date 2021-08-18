# Cursor position in the File

obj = open("C:/Users/ramadhma/Selenium/read.txt" ,'r')

print(obj.tell())
obj.seek(5)
print(obj.tell())