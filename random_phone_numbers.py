from random import randrange

def gen_rand_number():
    scom_code='0355'

    random_number=randrange(1011111,9999999)

    rand_number=(f"{scom_code}{random_number}")
    return rand_number
num = 5000

for i in range(num):
    number = gen_rand_number()
    with open("rand_numbers.txt", "a", encoding="UTF-8") as file:
        file.write(f"{number}\n")

print(f"{num} Phone Numbers Generated Successfully.")
