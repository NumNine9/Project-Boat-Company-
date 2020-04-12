import time
print('WELCOME TO THE HARBOUR PLACE!!')
current_time=4
close_time = 1900
current_time=input(print('What is the time in 24hr notation: '))
blue_choice='Blue'
yellow_choice='Yellow'
red_choice='Red'
current_time=int(current_time)
#print(current_time)
blue_boat,yellow_boat,red_boat = 10,12,8

available_boats = blue_boat + yellow_boat + red_boat

def all_boats_taken():
    print('Sorry all boats are taken :/')

if available_boats ==0:
    all_boats_taken()
else:
    time.sleep(3)
    print('There are {} yellow boats, {} blue boats, and {} red boats available.'.format(yellow_boat,blue_boat,red_boat))

time.sleep(3)
print('The cost of taking a single boat out is $20')
print('\n') #to print a new line
time.sleep(2)
color_choice=input(print('Which color do you want?(one at color at a time):'))

if blue_choice=='Blue':
    num_of_boats = int(input('How many boats do you want to take out?' ))
    blue_boat = blue_boat-num_of_boats
    rent_time=int(input('How many hours do you want to rent?' ))
    rent_money = rent_time*20*num_of_boats
    print('You have to pay ${} for renting {} {} boats for {} hours'.format(rent_money,num_of_boats,color_choice,rent_time))


elif yellow_choice=='Yellow':
    num_of_boats = int(input('How many boats do you want to take out?' ))
    blue_boat = blue_boat-num_of_boats
    rent_time=int(input('How many hours do you want to rent?' ))
    rent_money = rent_time*20*num_of_boats
    print('You have to pay ${} for renting {} {} boats for {} hours'.format(rent_money,num_of_boats,color_choice,rent_time))
    

elif red_choice=='Red':
    num_of_boats = int(input('How many boats do you want to take out?' ))
    blue_boat = blue_boat-num_of_boats
    rent_time=int(input('How many hours do you want to rent?' ))
    rent_money = rent_time*20*num_of_boats
    print('You have to pay ${} for renting {} {} boats for {} hours'.format(rent_money,num_of_boats,color_choice,rent_time))