from datetime import datetime
from display import time_in_russian
                      
flag=False
while not flag:
    choice=input("To get current time enter [Y], if you want to enter it yourself press [N]:\n").upper()
    if choice =='Y' or choice == 'N':
        flag=True
        break
if choice=='Y':
    current_time = list(str(datetime.now())[11:16].split(':'))
    hours, minits = current_time[0], current_time[1]
    time_in_russian(hours, minits)    
else:
    flag=False
    while not flag:
            print("Enter date in format hh:mm, where hours does not exceed 23 and minutes 59:")
            try:
                hours, minits = map(str,input().split(':'))
                if len(hours)==2 and len(minits)==2:
                    if hours.isdigit() and minits.isdigit():           
                        if (int(hours) < 24 and int(hours) >= 0) and (int(minits) >= 0 and int(minits) < 60):
                            flag=True
                            break
            except:          
                print("when entering, do not forget about the colon between numbers!")
    time_in_russian(hours, minits)
