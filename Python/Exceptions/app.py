try:
    age = int(input("AGE : "))
    print(age)
except ValueError:
    print("Invalid value")
finally:
    print("This block always excutes")


