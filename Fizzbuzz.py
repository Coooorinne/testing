n = int(15)
r = range(1, n+1) #you could also range over it range(n+1)
l = list(r)
#print(l)

#class: a function in a class only affects everything in the class itself (not global)
# e. g. all API requests are in a class, e. g. login is the init function (the inital thing that you would do, everything after that within the class would include the init function)


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
        print("Please choose a value between 1 and 10000")
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