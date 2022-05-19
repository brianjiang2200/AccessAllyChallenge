#THIS FILE ACCEPTS FILE NAME AS AN ARGUMENT

"""
Type O -> Type O
Type A -> Type A or Type O
Type B -> Type B or Type O
Type AB -> Any
Negative -> Negative
Postive -> Any
"""

"""
Intuition tells me that we can maximize the number of served patients by
distributing the most restrictive resources first, e.g. Give Type O Blood 
to O-blood patients before Type A or Type B patients.  
"""
import sys

f = open(sys.argv[1], "r")
supply_input = f.readline()
patient_input = f.readline()

#Blood Supply
supply = [int(elem) for elem in supply_input.split()]
#Patients
patients = [int(elem) for elem in patient_input.split()]

result = 0

#distribution helper method
def distribute(p_type, b_type):
    global result
    if patients[p_type] > supply[b_type]:
        patients[p_type] -= supply[b_type]
        result += supply[b_type]
        supply[b_type] = 0
    else:
        supply[b_type] -= patients[p_type]
        result += patients[p_type]
        patients[p_type] = 0

#Give O Negatives O Negative Blood
distribute(0, 0)
#Give A Negatives A Negative Blood and then O Negative if needed
distribute(2, 2)
distribute(2, 0)
#Give B Negatives B Negative Blood and then O Negative if needed
distribute(4, 4)
distribute(4, 0)
#Give AB Negatives any remaining Negative Type Blood
distribute(6, 0)
distribute(6, 2)
distribute(6, 4)
distribute(6, 6)

#Give O Positives Any O Negative Blood
distribute(1, 0)
distribute(1, 1)
#Give A Positives Any A Blood and then O if needed
distribute(3, 2)
distribute(3, 3)
distribute(3, 0)
distribute(3, 1)
#Give B Positives Any B Blood and then O if needed
distribute(5, 4)
distribute(5, 5)
distribute(5, 0)
distribute(5, 1)
#Give AB Positives any remaining Blood
for i in range(8):
    distribute(7, i)

print(f'{result}')

 