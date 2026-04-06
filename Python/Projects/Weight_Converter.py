w = int(input("Enter you weight : "))
m = input("(L)bs or (K)g : ")

if m == "L" or m == 'l':
    print(w * 0.45)
elif m == "K" or m == "k":
    print(w*2.20) 