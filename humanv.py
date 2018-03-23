import random

first_number = random.randint(0,9) #Generates first number
second_number = random.randint(0,9) #Generates second number
result = first_number + second_number #Result of sum of both numbers

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 5 #Number of tries to enter the correct result

print(first_number)
print(second_number)

while True:
    print(result)
    number = int(input())

    if number == result:
        print('You are human. You can proceed')
        break
    else:
        i -= 1
        if(i == 0):
            print('You can\'t be human. Try again later')
            exit()
