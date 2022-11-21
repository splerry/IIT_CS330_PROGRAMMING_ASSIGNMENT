#Marcel Bieganski

import random
class security:
    def search(self, user, code):
        detect = False
        for i in range(0, len(user)):
            k = 0
            if user[i] == code[k]:
                if user[i: i + len(code)] == code:
                    detect = True
        return detect

    def skim(self, input) ->str:
        return ''.join([i for i in input if i.isdigit()])

lock_code = "901494"
unlock_code = "901491"

sum = 0
min = 10000000000000000000000000000000000000000000
max = 0
dig = 0
for j in range(0, 1):
    found = False
    i = 1
    k = ""
    if j == 0:
        print("breaking... ")
    elif j == 25:
        print("tests 25% complete")
    elif j == 50:
        print("tests 50% complete")
    elif j == 75:
        print("tests 75% complete")
    elif j == 99:
        print("tests complete")
    while not found:
        num = random.randint(0, 999)
        k += str(num)
        found = security.search(security, k, unlock_code)
        i += 1
        dig += len(k)
        print(k)
    sum = sum + len(k)

    if len(k) < min:
        min = num
    if len(k) > max:
        max = num

    if j == 99:
        temp = str(sum // j)
        print("Average digit amount: " + str(sum))
        print("Largest digit amount accepted: " + str(max) + ". Smallest digit amount accepted: " + str(min))