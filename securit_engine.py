import random
class security:
    def search(self, user, code):
        detect = False
        str(user)
        str(code)
        for i in range(0, len(user)):
            k = 0
            if user[i] == code[k]:
                if user[i: i + len(code)] == code:
                    detect = True
        return detect

    def skim(self, input) ->str:
        return ''.join([i for i in input if i.isdigit()])

    def generate(self, dig):
        domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        temp = ""
        for i in range(dig):
            temp = temp + str(random.choice(domain))

        return temp


lock_code = "901494"
unlock_code = "901491"

print("Option 1: Run average time test (WARNING: may take a minute) [Part 2 of the assignment. Sample output in README if you dont want to run]")
print("Option 2: Run one code breaking session [Part 1 of the assignment]")
user_in = input("1 for Option 1 an 2 for Option 2: ")

if user_in == "1":
    sum = 0
    min = 10000000000000000000000000000000000000000000
    max = 0
    dig = 0
    for j in range(0, 250):
        found = False
        i = 1
        print("breaking... " + str(j))
        while not found:
            num = random.randint(0, 999999999999999999999)
            found = security.search(security, str(num), unlock_code)
            i += 1
            dig += len(str(num))
        sum = sum + i

        if num < min:
            min = num
        if num > max:
            max = num

        if j == 249:
            temp = str(sum // j)
            print("Average time: " + temp + " attempts/seconds. Total digits (0 - 9) entered: " + str(dig))
            print("Largest value accepted: " + str(max) + ". Smallest value accepted: " + str(min))

elif user_in == "2":
    found = False
    i = 1
    print("breaking... ")
    while not found:
        num = random.randint(0, 999999999999999999999)
        found = security.search(security, str(num), unlock_code)
        i += 1
    print("generated number: " + str(num) + " Attempt number: " + str(i))

else:
    print("Incorrect Input entered. Please carefully read the instructions. Close and run again")

input(" ")