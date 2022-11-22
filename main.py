import random
x = int(input("Lowest number in range:\n"))
y = int(input("\nHighest number in range:\n"))
print("\nThe random number in that range is: \033[0;32m" + str(random.randint(x,y)))