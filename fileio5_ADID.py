fd1 = open("in1_ADID.txt", "r")
print(fd1.name) #outputs the name of the file

print(fd1.close()) #none

print(fd1.mode) #returns the mode of the file that is r
fd1.close()

print(fd1.close()) #none