import sys
_, production, rate, premium = sys.argv
salary = (float(production) * float(rate)) + float(premium)
print(salary)
