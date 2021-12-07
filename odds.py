# Dependencies
from random import seed
from random import randint

# Theoretical Part
n = int(input("Range? "))

if n % 2 == 0: # Even number
	p = round((2*n-2)/(n*n)*100,4)
else: # Odd number
	p = round((2*n-1)/(n*n)*100,4)

print("Range: 1 to " + str(n))
print("Calculated chance of dare being executed: " + str(p) + "%")

# Simulation Part
s = int(input("Simulations? "))
dare_cases = 0

for i in range(s):
	num1 = randint(1,n)
	num2 = randint(1,n)
	if((num1 == num2) or ((num1 + num2) == n)):
		dare_cases += 1

simulatedChance = round((dare_cases/s)*100,4)

print("Range: 1 to " + str(n))
print("Simulated chance of dare being executed: " + str(simulatedChance) + "%")
print("")
