import time
secsnow = 0
def twentyfourh():
    hoursnow = int(input("enter the current hour in 24 hour format"))
    minutenow = int(input("enter the current minute"))
    seconds = 0
    for hours in range (24):
        hours = hours + hoursnow
        for mins in range(60):
            mins = mins + minutenow
            seconds = seconds + secsnow
            for seconds in range(60):
                print(hours, ":", mins, ":", seconds)
                time.sleep(1)
               
def twelvehour():
    hoursnow = int(input("enter the current hour in 12 hour format"))
    minutenow = int(input("enter the current minute"))
    seconds = 0
    for hours in range (12):
        hours = hours + hoursnow
        for mins in range(60):
            mins = mins + minutenow
            seconds = seconds + secsnow
            for seconds in range(60):
                print(hours, ":", mins, ":", seconds)
                time.sleep(1)
            


ask = input("would you like your flip clock in a 24 hour version? y/n")
if ask == "y":
    twentyfourh()
else:
    twelvehour()

#We are aiming to produce this: https://www.youtube.com/watch?v=rbOStasEUV0

#1) Run the program

#2) Get this to display the time from 0:00 to 23:59.
#Make sure it does not display as 0 0 or 0 1 as these are not correct times
#it should be 0:00, 0:01 etc

#3) Give them the option to display in 24hrs or (12hr with AM and PM)

#4) Write each version of the clock in separate procedures and call
#each one when requested

#5) Add in seconds hint: nest another for loop

#6) Use time.sleep() to get it to be pseudo-accurate in incrementing the seconds. If you are in IDLE, use Ctrl-C to break this when testing

#7) Ask the user to enter the current time and then keep outputting the
#time from then onwards

#Build your own calendar to output the correct dates in order.
#You will need to use lots of if statements as each month has different days.

