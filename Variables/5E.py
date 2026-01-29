x = "Best"
def myfunc():
    global x
    x = "Good"
    print("KBTU is " + x)
myfunc()
print("KBTU is " + x)