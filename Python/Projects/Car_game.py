first_command = input("Enter the command : ")

if first_command.lower() == "help":
    print("Start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")

    user_command = input()
    user_command.lower()

    
    if user_command == "start":
        print("Car started ... Ready to go!")
    elif user_command == "stop":
        print("Car Stopped")
    elif user_command == "quit":
        print("exit")
else:
     print("i dont understand")