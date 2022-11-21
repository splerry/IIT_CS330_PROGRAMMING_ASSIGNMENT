#Marcel Bieganski

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


lock_code = "901494"
unlock_code = "901491"

stop = False

sequence = ""
func = ""

print("Enter Access Code. Type 'stop' at any time to quit.")
while stop == False:
    user = input("")
    func = func + user
    func = security.skim(security, func)
    print(sequence + func)
    if security.search(security, func, lock_code):
        print("Locked")
        sequence = sequence + func
        func = ""
    elif security.search(security, func, unlock_code):
        print("Unlocked")
        sequence = sequence + func
        func = ""
    if user == "stop":
        stop = True
print("Total Sequence: " + sequence)