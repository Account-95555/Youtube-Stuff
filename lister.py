#This program outputs a github list format based on what number you input. This was created to make the music listing easier

#Keep in mind that this program only runs once, you have to restart it in order to run it again!

initial = 1
numbers = int(input("Enter how many numbers your list needs (outputted as (no.).): "))
while initial < numbers + 1:
    print(str(initial) + ". ")
    initial += 1
