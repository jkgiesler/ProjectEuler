'''
find the number of sundays which happened on the first of the month
between 1901 and 2000
'''

#1 Jan 1901 Tuesday

def is_leap(year):
    '''is leap year?'''
    if year % 1000 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 ==0:
        return True
    
    else:
        return False


def days_of_month(month,year):
    '''how many days in month'''
    if (month == 9) or (month == 4) or (month == 6) or (month == 11):
        return 30
    elif month == 2:
        if(is_leap(year)):
            return 29
        else:
            return 28
    else:
        return 31
        
def find_first_sundays():     
    '''
    this function will return the numbers of sundays 
    which were the first day of the month
    '''
    sumr=0
    day=2 # 1 1 1901 is a Tuesday
    for i in range(100): #check 100 years
        for j in range(12): #for 12 months
            days=days_of_month(j+1,1901+i)
            change=days%7 #how many days does each month move
            day=day+change
            if day>7:
                day=day-7 #if over 7 move it back
            if day==7: #if it's a sunday
                sumr+=1 #count it
    print(sumr)
        
find_first_sundays()
    
    