#EXERCISE
# Your task is to implement a class called Weeker.
# The class constructor accepts one argument – a string. The string represents 
# the name of the day of the week and the only acceptable values must come from the following set:
# [Mon Tue Wed Thu Fri Sat Sun]
# Invoking the constructor with an argument from outside this set 
# should raise the 'WeekDayError' exception (define the exception yourself)
# objects of the class should be "printable", i.e. they should be able to implicitly convert 
# themselves into strings of the same form as the constructor arguments;
# the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), 
# with n being an integer number and updating the day of week stored inside the object in the 
# way reflecting the change of date by the indicated number of days, forward or backward.
# all object's properties should be private;

# MY CODE
class WeekDayError(Exception):
    pass
	
class Weeker:
    __week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    def __init__(self, day):
        if day in Weeker.__week_days:
            self.__day = day
        else:
            raise WeekDayError
        
    def __str__(self):
        return str(self.__day) # return the weekday name as string which is the obj

    def add_days(self, n):
        # Write code here.
        sum = Weeker.__week_days.index(self.__day) + n 
        if sum <= 6: # weekday is the weekday with index as sum if sum is <= 6
            self.__day = Weeker.__week_days[sum]
        else:
            while sum > 6: # it is 6 bcos index starts from 0
                sum -= 7 # keep substrating no of days in a week from sum if sum > 6
            self.__day = Weeker.__week_days[sum]
        return self.__day

    def subtract_days(self, n):
        # Write code here.
        div = Weeker.__week_days.index(self.__day) - n
        if div >= 0:
            self.__day = Weeker.__week_days[div]
        else:
            while div < 0:
                div += 7
            self.__day = Weeker.__week_days[div]
        return self.__day
    