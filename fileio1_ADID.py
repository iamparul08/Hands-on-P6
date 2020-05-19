#read file line by line
f = open("in1_ADID.txt", "r")
print(f.readlines())
f.close()

#read the entire content of the file
f = open("in1_ADID.txt", "r")
for x in f:
    print(x)
f.close()