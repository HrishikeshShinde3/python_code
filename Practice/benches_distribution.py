# take a student count as a input from user
# then take how many students you want on each bench
# final output are benches which requires the given students to seat

#Student_Count = 25
#Student_On_Each_Bench = 2
#Required_Benches = 13

import math

Student_Count = int(input("Enter a total students of Institute :"))

Student_On_Each_Bench = int(input("Bench strength(Means How many students will seat on on bench) :"))

Required_Benches = Student_Count / Student_On_Each_Bench

print("Institute required",math.ceil(Required_Benches),"Benches")