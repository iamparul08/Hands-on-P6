#f = open("newfile1_ADID.txt", "r")
#print(f.readlines())
# it shows an error message that FileNotFound
#f.close()

f = open("newfile1_ADID.txt", "w")

s1_ADID = "This is the newline added at end"
f.write(s1_ADID)
f = open("newfile1_ADID.txt", "r")
print(f.readlines())

'''s1_ADID = "This is the newline added at end"
f.write(s1_ADID)
f = open("newfile1_ADID.txt", "r")
print(f.readlines())''' #UnsupportedOperation