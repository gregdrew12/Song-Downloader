def gettag(str, tag):
    while True:
        x = input(str)
        if(x): break
        print("Please enter a", tag + ".")
    return x 
