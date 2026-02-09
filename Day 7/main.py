#file = open("example1.txt", "r")
#print(file.read())
#print(file.read())
#file.close()

try:
    file=open("simple.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found, pls open exiting file")
finally:
    file.close()
