#----------------------------------------------------------

# Description
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are
# case sensitive, so "a" is considered a different type of stone from "A".
#
# Example
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

#------------------------------------------------------------
jewels = input("Please enter the types of stones that are jewels: ")
# print(f"type is {type(jewels)}")
stones = input("Please also enter the stones you have: ")
# print(f"type is {type(stones)}")

def jewels_and_stones(jewels, stones):
    count = 0

    for char in jewels:
        for x in stones:
            if char == x:
                count += 1

    return count


result = jewels_and_stones(jewels, stones)

print(f"You have {result} jewels")


#------------------------------------------------------------
# Approach
# 1. Input method
# 2. Pseudo code for logic
# 3. Function with code logic

#Other Approach:
#set_jewels = set(jewels)
#for stone in stones:
#    if stone in set_jewels:
#       count += 1

#------------------------------------------------------------