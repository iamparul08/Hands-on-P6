#reading first 11 characters from the file

print("First 11 characters of the file:")
f = open("in1_ADID.txt", "r")
print(f.read(11))
f.close()

#reading first line
print("\nReading first line of the file:")
f = open("in1_ADID.txt", "r")
print(f.readline())
f.close()


#using read() method
print("\nRead the content of the file:")
f = open("in1_ADID.txt", "r")
print(f.read())