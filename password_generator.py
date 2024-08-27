import argparse
import string
import random

# HELPER FUNCTIONS


# Returns 1 random character (uppercase and lowercase)
def get_random_char():
    return random.choice(string.ascii_letters)

# Returns 1 random character or digit
def get_random_digit_or_char():
    return random.choice(string.digits + string.ascii_letters)

def get_random_digit(): 
    return random.choice(string.digits)
    



# MAIN CODE
# Generates a password with random characters and given length.
def generate(num_numbers, num_letters):
    chars = ""
    for i in range(num_numbers):
        chars = chars + get_random_digit()
    for i in range(num_letters):
        chars = chars + get_random_char()
    shuffled = "".join(random.sample(chars,len(chars)))
    print(shuffled)
# Generates a password with random characters and given length.



if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-length", type=int)
#     parser.add_argument("-include-numbers", action="store_true")

#     args = parser.parse_args()
#     length = args.length
#     include_nums = args.include_numbers


    print("Number of numbers:")
    ans = input()
    ans = int(ans)

    
    while ans > 16:
        print("You can only have a maximum of 16 characters or less! Try again!")
        ans = input()
        ans = int(ans)
    print ("you will have", ans, "numbers")
    if ans == 16:
        generate(ans,0)
        exit()
    print ("how many letters would you like to have?")
    res= input()
    res = int(res)
    while res > 16-ans:
        print("You can only have", 16- ans, "letters or less! Try again!")
        res = input()
        res = int(res)
    print("you will have", res, "letters")
    generate(ans,res)
 


 
