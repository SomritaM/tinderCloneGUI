f = open("test.txt","w+")

f.write("""Hiii
How you doing?
 All Good.
 How About you ?""")

f.seek(0,0)
for i in f:
    for j in i.split():
        print(j)
    print(i)
f.close()