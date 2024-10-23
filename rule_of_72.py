import math 
#Initial values
Initial_amount = 2000
Interest_rate = 6

#calculate the years to double using the rule 72
years_to_double = math.ceil (72 / Interest_rate ) 
print(years_to_double )