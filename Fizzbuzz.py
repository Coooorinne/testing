n = int(100001)
r = range(1, n+1)
l = list(r)
#print(l)




def fizzbuzz(n):
    output = []
    if 1 <= n <= 10000:
        print("Your input number is valid")
        for num in l:
            if num % 3 == 0 and num % 5 == 0:
                output.append("FizzBuzz")
            elif num % 3 == 0:
                output.append("Fizz")
            elif num % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(num))
    else:
        print("Please choose a value between 1 and 1000")
    return output

print(fizzbuzz(n))

# ---------------------------------------------------
# Approach
#1. Converting input n to range
#2. Operation: Divider, remainder
#3. If statement --> elif not if!
#4. Convert num to string
#5. Integrate constraint

#----------------------------------------------------