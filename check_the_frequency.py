
# creating the dictionary:
dictionary1 = {'Codlingal' : 3, 'is' : 2 , 'the' : 2, 'best' : 2, 'for' : 1, 'coding' : 1}
print(dictionary1)

try:
    # Take input from the user:
    k = int(input("Enter your amount to check the frequency: "))

    # creating a for loop:
    for key in dictionary1:
        if dictionary1 [key] == k:
            print(key, end = " ")
        else:
            print("enter a number between 1 to 3!")
            break

except ValueError:
    print("Please enter valid numerical value!")







