import random 

machinepin = random.randint(1578,9264)
userpin = int(input("Enter 4 digits: "))
if userpin < 1000 or userpin >9999 :
    print("i said 4-digts")
    exit()
else:
    if userpin == machinepin :
            print("PIN code Matched !")
    else :
             print(f"The Computer Genrate This Code :{machinepin}")    


