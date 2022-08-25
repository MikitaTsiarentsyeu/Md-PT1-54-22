from time_data import time_selector, clock_words

def time_in_russian(hh, mm):
    hours_12 = int(hh) % 12
    minits_60 = int(mm) % 60 
    if minits_60 == 0:
        if hours_12 == 1:
            print(time_selector[hours_12][0] + clock_words["hours"][0])
        elif hours_12 in range(2,5):
            print(time_selector[hours_12][0] + clock_words["hours"][1])
        else:
            print(time_selector[hours_12][0] + clock_words["hours"][2])
    elif minits_60 in range(1,30):
        if minits_60==1:
            print(time_selector[minits_60][1] + clock_words["minits"][0] + time_selector[hours_12 + 1][2])
        elif minits_60 in range(2,5):
            print(time_selector[minits_60][1] + clock_words["minits"][1] + time_selector[hours_12 + 1][2])       
        elif minits_60 in range(5,21):
            print(time_selector[minits_60][1] + clock_words["minits"][2] + time_selector[hours_12 + 1][2])
        else:
            if minits_60 % 20 == 1:
                print(time_selector[20][0] + time_selector[minits_60 - 20][1] + clock_words["minits"][0] + time_selector[hours_12 +1][2])     
            elif minits_60 % 20 in range(2,5):
                print(time_selector[20][0] + time_selector[minits_60 - 20][1] + clock_words["minits"][1] + time_selector[hours_12 + 1][2])    
            else:
                print(time_selector[20][0] + time_selector[minits_60 - 20][1] + clock_words["minits"][2] + time_selector[hours_12 + 1][2])                    
    elif minits_60 == 30:
        print(clock_words["hours"][-1] + time_selector[hours_12 + 1][2])
    elif minits_60 in range(31,45):
        if minits_60 // 10 == 3:
            if minits_60 % 30 == 1:
                print(time_selector[30][0] + time_selector[minits_60 - 30][1] + clock_words["minits"][0] + time_selector[hours_12 + 1][2])     
            elif minits_60 % 30 in range(2,5):
                print(time_selector[30][0] + time_selector[minits_60 - 30][1] + clock_words["minits"][1] + time_selector[hours_12 + 1][2])
            else:
                print(time_selector[30][0] + time_selector[minits_60 - 30][1] + clock_words["minits"][2] + time_selector[hours_12 + 1][2])
        else:
            if minits_60 % 40 == 1:
                print(time_selector[40][0] + time_selector[minits_60 - 40][1] + clock_words["minits"][0] + time_selector[hours_12 + 1][2])     
            elif minits_60 % 40 in range(2,5):
                print(time_selector[40][0] + time_selector[minits_60 - 40][1] + clock_words["minits"][1] + time_selector[hours_12 + 1][2])
            else:
                print(time_selector[40][0] + time_selector[minits_60 - 40][1] + clock_words["minits"][2] + time_selector[hours_12 + 1][2])                     
    else:
        if minits_60 // 10 == 4:
            if hours_12 + 1 == 1:
                print(clock_words["minits"][-1] + time_selector[60 - minits_60][3] + clock_words["minits"][2] + "час")
            else:
                print(clock_words["minits"][-1] + time_selector[60 - minits_60][3] + clock_words["minits"][2] + time_selector[hours_12 + 1][0])    
        elif 60 - minits_60 == 1:
            if hours_12 + 1 == 1:
                print(clock_words["minits"][-1] + time_selector[60 - minits_60][3] + clock_words["minits"][1] + "час")
            else:
                print(clock_words["minits"][-1] + time_selector[60 - minits_60][3] + clock_words["minits"][1] + time_selector[hours_12 + 1][0])    
        else:
            if hours_12 + 1 == 1:
                print(clock_words["minits"][-1] + time_selector[60 - minits_60][3] + clock_words["minits"][2] + "час")
            else:
                print(clock_words["minits"][-1] + time_selector[60 - minits_60][3] + clock_words["minits"][2] + time_selector[hours_12 + 1][0])