#THIS SCRIPT ACCEPTS COMMAND LINE INPUT

#Example: Input 34, Output 1
#Example: Input 180, Output 11

"""
Let's calculate how many "arithmetic sequences" there are in each hour of the day and store them in a lookup table.
Since we are using a 12 hour clock, the lookup table only needs 12 slots. 
"""
import sys

lut = []

def count_sequences(hour):
    times = []

    #We can simply use special cases for hours > 10
    if hour == 10:
        return times
    elif hour == 11:
        return ['11:11']
    elif hour == 0:
        return ['0:34']  

    #The maximum possible distance between two consecutive digits is 4, since a time here has exactly 3 digits. 
    for i in range(-4, 5):
        digit2 = hour + i
        if digit2 > -1 and digit2 < 6:
            digit3 = hour + 2 * i 
            if digit3 > -1 and digit3 < 10:
                time = f'{hour}:{digit2}{digit3}'
                times.append(time)
    return times

#Populate LUT
for i in range(11):
    lut.append(count_sequences(i))

#Return Output
def getOutput(input):
    result = 0

    hours_elapsed = input // 60
    minute = input % 60

    for i in range(hours_elapsed):
        lut_index = i % 12
        result += len(lut[lut_index])

    #Include any we passed in the current hour
    current_hour = hours_elapsed % 12
    list = count_sequences(current_hour)
    #Using the +1 time instead
    current_time = f'{current_hour}:{minute + 1:02}'
    list.append(current_time)
    list.sort()
    result += list.index(current_time)

    return result

    
#Forgive the lack of error handling for now, assuming the user will cooperate 
f = open(sys.argv[1], "r")
print(f'{getOutput(int(f.readline()))}')
