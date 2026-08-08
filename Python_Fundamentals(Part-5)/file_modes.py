
#*Uses Pointer concept
# f = open("sample.txt","r") #*file object
#*Read Operation
# data = f.read()
# print(data)
# print(type(data))

# data1 = f.readline()
# print(data1)

# data1 = f.readline()
# print(data1) 

#-----------------x-----------------------------
#*Write Operation
# f = open("sample.txt","w")
# f.write("ankita is my best friend \n we both study together")

#overwrite(sample.txt) -> O/P

#-----------------x----------------------------
#*Default(Read Mode)
# f = open("sample.txt")
# print(f.read())

#-----------------x------------------------------

#*append mode
# f = open("sample.txt","a")
# f.write("\nNew text being appended")

#----------------x----------------------------------

#*New file Created
# f = open("sample1.txt","a")
# f.write("Some random text")

#-------------------x----------------------------
#*New file Created
# f = open("sample2.txt","w")
# f.write("some random text 1")

#----------------x-----------------------------
#*x mode(Throws error)
# f = open("sample1.txt","x")
# f.write("hello")

#---------------x--------------------------
#* + Mode

#*r+
# f = open("sample1.txt","r+")
# print(f.read())
# f.write("123")

# f = open("sample.txt","r+")
# f.write("123")
# print(f.read())
#*its read part prints after the write part

#*w+
# f = open("sample2.txt","w+")
# f.write("123")
# print(f.read())

#*a+
# f = open("sample.txt","a+")
# f.write("123")
# print(f.read())
#*its read part prints nothing as pointer is at end


























f.close()   #*we need to close it