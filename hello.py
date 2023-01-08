



def noob_fun():
    # Small brain
    print("To be or not to be \"Joke\"")
def generic_triangle(s, basewidth):
    w = len(s)
    
    id = " " * w

    # I have no idea if this will work
    for i in range(0, (basewidth + 1) // 2):
        print((id + " ") * (basewidth // 2 - i), end="")
        print((s + " ") * (i * 2 + 1))

generic_triangle("noob", 9)

# Yo install minecraft