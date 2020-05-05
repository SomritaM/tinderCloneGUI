a=10
b=0
mylist=[1,2,3,4]
try:
    c=a/b
    print(mylist[2])
except  TypeError as e:
    print("Hii")
    print("Error is",type(e).__name__)
except  ZeroDivisionError as ex:
    print("Hoo")
    print(type(ex).__name__)
except Exception as e:
    print("List error")
    print(type(e).__name__)
else:
    print("hola")
finally:
    print("Ok Bye")