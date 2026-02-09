#file=open("example3.txt","w")
#file.write("welcome to the lion movie")
#file.close()

try:
    file=open("simple.txt","r")
    print(file.read())
except Exception as e:
    print(f"Error :{e}")
#finally:
    #file.close()