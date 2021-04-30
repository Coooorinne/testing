n = int(15)
r = range(1, n+1)
l = list(r)
print(l)

def fizzbuzz(n):
    output = []
    for num in l:
        if num % 3 == 0 and num % 5 == 0:
            output.append("FizzBuzz")
        elif num % 3 == 0:
            output.append("Buzz")
        elif num % 5 == 0:
            output.append("Fizz")
        else:
            output.append(str(num))

    return output


print(fizzbuzz(4))

# ---------------------------------------------------
# Approach
#1. Converting input n to range
#2. Operation: Divider, remainder
#3. If statement --> elif not if!
#4. Convert num to string
#5. Integrate constraint

#----------------------------------------------------