import math
number=64
calculate_sqroot=round(math.sqrt(number))
is_prime=True

for i in range(2,calculate_sqroot + 1):
    if number % i == 0:
        is_prime=False
        break
      
if is_prime == True:
    print("Number is Prime")
else:
    print("Not a prime")        