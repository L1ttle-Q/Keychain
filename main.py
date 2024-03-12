import os, ast, subprocess

KeySet = {}

def Clear(_time):
    os.system(f"sleep {_time}")
    os.system("clear")

def Save(URL, Account, PassWord):
    KeySet.setdefault(URL)
    if (not KeySet[URL]):
        KeySet[URL] = {}
    KeySet[URL].setdefault(Account)
    KeySet[URL][Account] = PassWord
    print("Save successfully!")
    return True

def Find(URL, Account):
    global KeySet
    if (URL not in KeySet.keys()):
        return False
    elif Account not in KeySet[URL].keys():
        return False
    else:
        return True

def PrintGuide():
    '''
    try:
        os.system("color 04")
    except:
        pass
    '''

    print("Welcome to use Keys Set to manage your accounts!")

    '''
    try:
        os.system("color 0F")
    except:
        pass
    '''

    print("\
    'r' for read\n\
    'i' for insert\n\
    'q' for quit\n\
    'a' for looking all the accounts")
    print("Please press a letter and enter:")

def Y_or_N(Read):
    Read = Read.lower()
    while (Read not in ['y', 'n']):
        Read = input("Invalid input.Please try again:(y or n)")
    if (Read == 'y'):
        return True
    else:
        return False

#main

err1 = 0
if (os.access("./Lock.exe", os.X_OK)):
    pass
elif(os.access("./Lock.cpp", os.R_OK)):
    os.system("g++ ./Lock.cpp -o Lock.exe")
else:
    err1 = 1

if (err1 == 0):
    print("Succeed to link the lock&unlock program!")
    err2 = 0
    if (not os.access("key.txt", os.R_OK)):
        open("key.txt", "x")
        print("Fail to read the saved keys.")
        err2 = 1

    if(err2 == 0):
        if (not os.access("sec.txt", os.R_OK)):
            open("sec.txt", "x")
            print("Fail to read the saved keys.")

        else:
            tmp = subprocess.run(["./Lock.exe", "", "-1"], stdout = subprocess.PIPE)
            tmp = tmp.stdout.decode("utf-8")

            if (tmp == "---"):
                print("Fail to read the saved keys.")
            else:
                #change the string into dict
                KeySet = ast.literal_eval(tmp)
                print("Succeed to read the saved keys!")

            del tmp
else:
    print("Fail to link the lock&unlock program.")
    print("Your input will not be saved in the file.")

input("Click enter to continue.")
Clear(0.5)
while True:
    #print(str(KeySet))
    PrintGuide()

    opt = input()
    opt = opt.lower()

    if (opt not in ['r', 'i', 'q', 'a']):
        print("Wrong input!")
        Clear(1.5)
        continue

    if (opt == 'q'):
        break

    elif (opt == 'i'):
        URL = input("URL:")
        Account = input("Account:")
        PassWord = input("PassWord:")
        if (Find(URL, Account)):
            f = input("The account is saved.Do you want to change it?(y or n)\n")
            if (Y_or_N(f)):
                Save(URL, Account, PassWord)
            else:
                print("Fail to save.")
            Clear(1.5)
            continue
        else:
            Save(URL, Account, PassWord)
            Clear(1.5)

    elif (opt == 'r'):
        URL = input("URL:")
        if (KeySet.get(URL, False)):
            print("All accounts in this site:")
            for Acc, Pas in KeySet[URL].items():
                print(f"[Account:{Acc}\nPassWord:{Pas}]\n")
            input("Click enter to continue.")
            Clear(0.5)

        else:
            print("No account in this site,you can add an account now,", end = "")
            print("do you want to add?(y or n)")
            f = input()
            if (Y_or_N(f)):
                Account = input("Account:")
                PassWord = input("PassWord:")
                Save(URL, Account, PassWord)
            else:
                print("Fail to save.")
            Clear(1.5)

    elif (opt == 'a'):
        if (KeySet):
            for U, A in KeySet.items():
                print(f"{U}:")
                for Acc, Pas in A.items():
                    print(f"[Account:{Acc}\nPassWord:{Pas}]\n")
            input("Click enter to continue.")
            Clear(0.5)
        else:
            print("Nothing is saved.")
            Clear(1.5)

#Lock & Save the file
if (err1 == 0):
    subprocess.run(["./Lock.exe", str(KeySet), "1"])
    '''
    Write = subprocess.run(["./Lock.exe", str(KeySet), "1"], stdout=subprocess.PIPE)
    f = open("key.txt", "w")
    f.write(str(Write.stdout.decode("utf-8")))
    f.close()
    '''