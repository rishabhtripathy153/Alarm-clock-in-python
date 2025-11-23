from datetime import datetime
from playsound import playsound
import winsound
 #TAke input from user date time 
date = input("Enter the date for alarm to be set on = ")
time = input("Enter time for alarm to be set on(in HH:MM,AM/PM)=")
alarm_hour=time[0:2]
alarm_minute=time[3:5]
alarm_period=time[6:8]


print(" Setiing alarm ..............")
print("Alarm set ")


while True:
    current_time=datetime.now()
    current_hour=current_time.strftime('%I')
    current_minute=current_time.strftime('%M')
    current_period=current_time.strftime('%p')
    current_date=current_time.strftime('%d')
    if(current_date==date and current_period==alarm_period and current_hour==alarm_hour and current_minute==alarm_minute):
        print('*'*10)
        print('| '+'Wake up!'+' |')
        print('*'*10)
        playsound('audio.wav')
    



    #Thankyou 