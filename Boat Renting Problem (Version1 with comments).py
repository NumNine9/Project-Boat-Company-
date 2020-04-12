#ASSUMPTIONS MADE DURING CODING:
        #THE USER IS GOOD A MATH
        #USER DOESNT ENTER A WRONG TIME LIKE 0300 OR 2700...INSTEAD ENTERS 300 OR 1500
        #DOESN'T ENTER FLOATING POINT NUMBERS FOR HOURS ...FOR EXAMPLE 2.3
        #PROGRAMMER HASN'T GRASPED OOP
        #BOAT RENTING COMPANY OPENS 24/7 HRS

import time  #for delaying the program
print('WELCOME TO THE HARBOUR PLACE!!')
current_time=4
close_time = 1900
current_time=input(print('What is the time in 24hr notation: '))
blue_choice='Blue'    #going to be using the color for equivalence
yellow_choice='Yellow'     #going to be using the color for equivalence
red_choice='Red'           #going to be using the color for equivalence
current_time=int(current_time)  #changing the input into an integer
#print(current_time)
blue_boat,yellow_boat,red_boat = 10,12,8    #assigning values

available_boats = blue_boat + yellow_boat + red_boat   #adding all the boats to show how many boats are available

def all_boats_taken():  #its function is to show a message
    print('Sorry all boats are taken :/')

if available_boats ==0:
    all_boats_taken()
else:
    time.sleep(3)  #delays the program for 3 seconds
    print('There are {} yellow boats, {} blue boats, and {} red boats available.'.format(yellow_boat,blue_boat,red_boat))

time.sleep(3)     #delays the program for 3 seconds
print('The cost of taking a single boat out is $20')
print('\n') #to print a new line
time.sleep(2)      #delays the program for 2 seconds
color_choice=input(print('Which color do you want?(one at color at a time):'))

if blue_choice=='Blue':   #checking if input is equivalent to a previously defined color
    num_of_boats = int(input('How many boats do you want to take out?' )) #take the input a immediately converts the string into an integer
    blue_boat = blue_boat-num_of_boats #calculate the number of remaining blue boats
    rent_time=int(input('How many hours do you want to rent?' ))  #take the input a immediately converts the string into an integer
    rent_money = rent_time*20*num_of_boats #calculating the amount of money the customer has to pay
    print('You have to pay ${} for renting {} {} boats for {} hours'.format(rent_money,num_of_boats,color_choice,rent_time))


elif yellow_choice=='Yellow':   #has the same comments as "Blue"
    num_of_boats = int(input('How many boats do you want to take out?' ))
    blue_boat = blue_boat-num_of_boats
    rent_time=int(input('How many hours do you want to rent?' ))
    rent_money = rent_time*20*num_of_boats
    print('You have to pay ${} for renting {} {} boats for {} hours'.format(rent_money,num_of_boats,color_choice,rent_time))
    

elif red_choice=='Red':  #has the same comments as "Blue"
    num_of_boats = int(input('How many boats do you want to take out?' ))
    blue_boat = blue_boat-num_of_boats
    rent_time=int(input('How many hours do you want to rent?' ))
    rent_money = rent_time*20*num_of_boats
    print('You have to pay ${} for renting {} {} boats for {} hours'.format(rent_money,num_of_boats,color_choice,rent_time))
#There is a lot of repetion in this version of the program but in Version 2 the goal is to:
        #reduce the lines of code
        #changing the times from 24/7 and putting a opening and closing time
        #put error messages for wrong inputs
        #changing 24hr notation
        