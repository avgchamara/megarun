import time
import urllib
import sys
import os
import json

os.system('clear')

hr_line = "\033[1;33;40m\n_________________________________________________\n"

name = """\033[1;32;40m
___________________________________________________________
\033[0;31;47m                 >>>> Automated <<<<                       
\033[1;36;40m      __  __               _      ____        _   _
\033[1;34;40m     |  \/  | ___  __ _   / \    |  _ \ _   _| \ | |
\033[1;36;40m     | |\/| |/ _ \/ _` | / O \   | |_) | | | |  \| |
\033[1;34;40m     | |  | |  __/ (_| |/ ___ \  |  _ <| |_| | |\  |
\033[1;36;40m     |_|  |_|\___|\__, /_/   \_\ |_| \_\\____/|_| \_|
\033[1;34;40m                  |___/
\033[1;32;40m___________________________________________________________
\033[0;31;47m            >>>> Code by BloodSeeker <<<<                  
\033[1;32;40m___________________________________________________________
"""
print(name, "")


try:
    f = open("authentication.txt", "r")
    auth = f.read()
    f.close
except:
    wr = str(input("\033[1;0;40mEnter your Authentication code : "))
    f = open("authentication.txt", "w")
    f.write(wr)
    f.close
    f = open("authentication.txt", "r")
    auth = f.read()
    f.close

    
try:
    f = open("url.txt", "r")
    url1 = f.read()
    f.close
except:
    wr = str(input("Enter Your URL Link : "))
    f = open("url.txt", "w")
    f.write(wr)
    f.close
    f = open("url.txt", "r")
    url1 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(name,"\n")
    s = int(input("\033[1;0;40mEnter Repeat Amount - "))
    header = {"Host": "megarun.dialog.lk",
              "Authorization": auth, "X-Unity-Version": "2018.3.0f2"}
    url = url1
    total_data = 0
    cmp_requst = 0
    count = 0
    while s > cmp_requst:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get(url, headers=header)
        # res = requests.get(url)
        # print(res.status_code)
        

        
        if res.status_code == 204:
            print("\n\033[1;33;40m No Data Recived this time")
            print(hr_line)  
        elif res.status_code == 200:
            count = count + 1
            current_data = int(res.json()['size'])
            # current_data = int(res.json()['critical'])
            total_data = total_data + current_data
            print(hr_line)
            print("\n\033[1;32;40m Congratulations!!! \033[1;37;40m" + str(current_data) + "MB \033[1;32;40mdata bundle recived")
            print(hr_line)
        else:
            print(hr_line)
            print("\n\033[1;31;40m Sometimes this number is Blocked. Check and Try again")
            print(hr_line)
        
        print("\n\033[1;37;40mTotal Recived Data  :  " + "\033[1;32;40m"+ str(total_data) + " MB")
        print("\n\033[1;37;40mRecived Data Pack   :  " + "\033[1;32;40m"+ str(count))
        print(hr_line)
        cmp_requst+=1
        print("\033[1;37;40m\n",str(cmp_requst),"\033[1;32;40mrequest complete.. Wait for Next Data Request",end="")
        for i in range(180):
            
            loop_presentage = i/180*100
            print("\033[1;34;40m\n===>>>> ",str(int(loop_presentage)) +"% ",end="")
            
            time.sleep(0.5)
            sys.stdout.write("\033[F")
        
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nRepeat this Again ? (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid input')
        again()


if __name__ == "__main__":
    main()
