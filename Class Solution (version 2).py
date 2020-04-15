#each boat has a color and a max number
import time #to use the sleep method

#yellow boats cost $15 per hour
#blue boats cost $20 per hour
#red boats cost #30 per hour

class Boat:     #class to be used to stare data for the boats
    def  __init__(self,colour,number):
        self.colour=colour
        self.number=number

YellowBoats = Boat('Yellow',12) #data for all yellow boats
BlueBoats = Boat('Blue',10)     #data for the blue boats
RedBoats = Boat('Red',8)        #data for the all red boats

print('  blue boat   --->    $20/hr.') #there was a need to make the output more presentatable
print('|--------------------------|')  #a simple display for everyone
print('  red boat    --->    $30/hr')
print('|--------------------------|')
print('  yellow boat --->    $15/hr')

time.sleep(4)#delays the program by (x) seconds
    
print('There are {} red boats, {} blue boats, and {} yellow boats.'.format(RedBoats.number,BlueBoats.number,YellowBoats.number))
#the above line is to display the number of available boats.

try: #used try/except incase the user inputs a value thats not an integer
    while True: #while loop to collect all the number of boats
        num_of_blue= int(input(print('How many boats blue boats do you want to take out?')))
            
        num_of_red= int(input(print('How many boats red boats do you want to take out?')))
            
        num_of_yellow= int(input(print('How many boats yellow boats do you want to take out?')))
            
        break  #to break the loop 
except ValueError: 
    print('Invalid input.') #error message to the user...it also ends the program 
        
blue_hours=int(input('How many blue hours do you want? -->'))   #Asks for the hours
red_hours=int(input('How many red hours do you want? -->'))      #<---
yellow_hours=int(input('How many yellow hours do you want? -->'))#<---
total_hours=blue_hours+red_hours+yellow_hours  #calculates the total hours by adding red_hours+ blue_hours + yellow_hours
cost_blue = blue_hours*20*num_of_blue  #calculates the cost for all the blue boats
print('blue boats cost    -->  ${} '.format(cost_blue))#displays the cost
cost_red = red_hours*30*num_of_red     #calculates the cost for all the blue boats
print('red boats cost     -->  ${} '.format(cost_red))#displays the cost
cost_yellow= yellow_hours*15*num_of_yellow   #calculates the cost for all the blue boats
print('yellow boats cost  -->  ${} '.format(cost_yellow))#displays the cost
total_cost= cost_blue + cost_red + cost_yellow#calculates the cost for all the blue boats
print('       total cost   =   ${}  '.format(total_cost))#displays the total 
time.sleep(3)  #delays the program by (x) seconds