# the goal the many functions is to produce something

#-- take something in as an argument
#-- manipulate it/do something to/with it
#-- return the ouput

name = "Travis"

data = type(name) # value is returned but no printed to the screeen, so we don't get to see it
print(data)

print(type(name)) # print() is allowing us to see/view the returned data from the function

# simple function with a return statement

def addition(a, b):
    return a + b

# def addition1(a, b): # this will do exectly the same thing, but the above is easier to write
#     ans = a + b
#     return ans

total = addition(5, 5)
print(total)

# this also works
print(addition(10, 10))

addition(1, 20) # here nothing prints to the screen because data is returned, but we're not doing anything with it
print(addition(25, 25)) # here we're doing something with this data, printing it

# doubler function that takes in a list of numbers and doubles each value in the list, then returns the new list

def doubler(nums):
    doubled_nums = []
    for num in nums:
        doubled_num = num * 2
        doubled_nums.append(doubled_num)
    return doubled_nums
    # print(doubled_num) # this won't execute because it is coming after our return statement. A return statement signifies the end of a function

my_nums = [1,2,3,4,5,6,7,8,9]
dnums = doubler(my_nums)
print(dnums)

#--- a function with no return

def greet_card(name): # a function without a return statement by default returns a None value
    print(f"Have a nice day, {name}!")

card_message = greet_card("Travis")

print(card_message)