magic_number = 9
count = 0

while( count <3):
    guess = int(input("Guess :"))
    if(count == 2):
        break
    count = count + 1
    if(guess == magic_number):
        print("you win")
        break
    
    
print("Game Over")