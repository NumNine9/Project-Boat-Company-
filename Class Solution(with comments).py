#each boat has a color and a max number
import time #to slow the program down (with the sleep method)

#yellow boats cost $15 per hour
#blue boats cost $20 per hour
#red boats cost #30 per hour

class Boat:  #class to be used to stare data for the boats
    def  __init__(self,colour,number):  #class to be used to stare data for the boats
        self.colour=colour
        self.number=number


YellowBoats = Boat('Yellow',12) #data for all boats
BlueBoats = Boat('Blue',10)     #<---
RedBoats = Boat('Red',8)        #<---

print('The cost of renting a blue boat is $20 per hour.\nThe cost of renting a red boat is $30.\nThe cost for renting a yellow boat is $15.')
#above line is to display the costs 
time.sleep(4)

print('There are {} red boats, {} blue boats, and {} yellow boats.'.format(RedBoats.number,BlueBoats.number,YellowBoats.number))
#above line to display all the available boats
try:  #used try/except just incase the user enters anything thats not an integer
    time.sleep(4)
    colour_choice=input(print('Which colour boat do you want to take out? Press 1 for blue, 2 for red, and 3 for yellow.'))
    #above line is to make the user choice which colour boat they want.
    colour_choice=int(colour_choice)  #Stores the value as an integer 

except ValueError:

    print('Invalid value input')#to display an error ....this also terminates the program 

time.sleep(2)

if colour_choice==1:  #operations will done on the blue boats
    number_of_boats = input('How many {} boats do you want to take out?'.format(BlueBoats.colour))#asks the user for the amount of boats
    number_of_boats=int(number_of_boats) #turns the input into an integer
    BlueBoats.number=10-number_of_boats #takes away the entered number from 10

    time.sleep(2)

    number_of_hours= input('How many hours do you want to take the boat(s)?')#ask for the number of hours
    number_of_hours=int(number_of_hours)#turns the input into an integer
    cost = number_of_hours*20*number_of_boats#calculates the cost by multiplying (hours*cost of rent*number of boats)

    time.sleep(2)

    print('The total cost for taking {} boats for {} hours is ${}.'.format(number_of_boats,number_of_hours,cost))
    #above line shows displays all the info and the cost in dollars
elif colour_choice==2:  #it has the same comments as from line 36- line 50
    number_of_boats = input('How many {} boats do you want to take out?'.format(RedBoats.colour))
    number_of_boats=int(number_of_boats)
    BlueBoats.number=8-number_of_boats
    
    time.sleep(4)

    number_of_hours= input('How many hours do you want to take the boat(s)?')
    number_of_hours=int(number_of_hours)
    cost = number_of_hours*30*number_of_boats
    
    time.sleep(3)

    print('The total cost for taking {} boats for {} hours is ${}.'.format(number_of_boats,number_of_hours,cost))

elif colour_choice==3:
    number_of_boats = input('How many {} boats do you want to take out?'.format(YellowBoats.colour))
    number_of_boats=int(number_of_boats)
    BlueBoats.number=12-number_of_boats

    time.sleep(2)

    number_of_hours= input('How many hours do you want to take the boat(s)?')
    number_of_hours=int(number_of_hours)
    cost = number_of_hours*15*number_of_boats

    time.sleep(2)

    print('The total cost for taking {} boats for {} hours is ${}.'.format(number_of_boats,number_of_hours,cost))
    print('There are {} {} boats.'.format(YellowBoats.number,YellowBoats.colour))#shows the number of boats left
    print('There are {} {} boats.'.format(BlueBoats.number,BlueBoats.colour))
    print('There are {} {} boats.'.format(RedBoats.number,RedBoats.colour))

