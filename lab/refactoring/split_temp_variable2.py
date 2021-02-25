# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into database")


username = input('Please enter your username: ')
save_into_db(username)
dob = int(input('Please enter your birth year: '))
age = 2020 - dob
print("You are",age, "years old.")