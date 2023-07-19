import os
import time
v = """
[1].Back To Menu
[2].Exit"""

def back():
    print(v)
    inuser = input("Enter Here: ")
    if inuser =="1" or inuser=="Exit" or inuser=="exit":
        os.system('clear')
        time.sleep(1)
        return menu()
    else:
        print("\tBye-bye")
        exit()



def design():
    project_name = "Crypt-Tools"
    author = "Crypt-tors"

    # Display the project title
    print("######################################################")
    print("#        ", project_name,'                              #')
    print("#        Author: ", author,'                        #')
    print("######################################################")



def informationGathering():
    print("\t###########################")
    print("\t   INFORMATION GATHERING    ")
    print("\t###########################")
    time.sleep(1)
    print("""
    [1].SIGIT
    [2].Infoga
    [3].Profil3r
    [4].LittleBrother
    [5].E4GL30S1NT
    [6].userrecon
    [7].FacebookOSINT
    [8].Cam-Hackers
    [9].whois
    [10].Nmap""")
    user = input("Select Number: ")
    if user == "1":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling SIGIT")
        time.sleep(1)
        os.system('pkg install wget && wget https://raw.githubusercontent.com/termuxhackers-id/SIGIT/main/install.sh && bash install.sh')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="2":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Infoga")
        time.sleep(1)
        os.system(
            'git clone https://github.com/m4ll0k/Infoga.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="3":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Profil3r")
        time.sleep(1)
        os.system('git clone https://github.com/Greyjedix/Profil3r.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="4":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling LittleBrother")
        time.sleep(1)
        os.system('git clone https://github.com/Lulz3xploit/LittleBrother')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="5":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling E4GL30S1NT")
        time.sleep(1)
        os.system('pkg install wget && wget https://raw.githubusercontent.com/C0MPL3XDEV/E4GL30S1NT/main/install.sh && bash install.sh')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="6":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling userrecon")
        time.sleep(1)
        os.system('git clone https://github.com/wishihab/userrecon.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="7":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling FacebookOSINT")
        time.sleep(1)
        os.system('git clone https://github.com/tomoneill19/FacebookOSINT')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="8":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Cam-Hackers")
        time.sleep(1)
        os.system('git clone https://github.com/AngelSecurityTeam/Cam-Hackers')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="9":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling whois")
        time.sleep(1)
        os.system('apt install whois')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="10":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Nmap")
        time.sleep(1)
        os.system('apt install nmap -y')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()
    else:
        print("\t[!] Please Select Correctly")
        time.sleep(2)
        os.system('clear')
        return informationGathering()






def vulnerability():
    print("""
    [1].Nmap
    [2].RED_HAWK
    [3].Whois
    [4].netscan""")
    user = input("Enter: ")
    if user == "1":
        os.system('clear')
        print('\tInstalling Nmap')
        time.sleep(1)
        os.system('apt install nmap -y')
        time.sleep(3)
        os.system('clear')
        print("\tDone Installing")
        time.sleep(3)
        return back()

    elif user =="2":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling RED_HAWK")
        time.sleep(1)
        os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="3":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling whoisK")
        time.sleep(1)
        os.system('apt install whois -y')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()



    elif user == "4":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tnentscan")
        time.sleep(1)
        os.system('git clone https://github.com/Yuma-Tsushima07/netscan.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    else:
        print("\t[!] Please Select Correctly")
        time.sleep(2)
        os.system('clear')
        return vulnerability()




def ipTracking():
    print("""
    [1].track-ip
    [2].trape
    [3].IPGeoLocaton
    [4].trackout
    [5].IP-Tracer""")

    user = input("Select Number: ")
    if user == "1" :
        os.system('clear')
        print('\tInstalling track-ip')
        time.sleep(1)
        os.system('git clone https://github.com/htr-tech/track-ip.git')
        time.sleep(3)
        os.system('clear')
        print("\tDone Installing")
        time.sleep(3)
        return back()

    elif user =="2":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling trape")
        time.sleep(1)
        os.system('git clone https://github.com/jofpin/trape.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="3":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling IPGeoLocation")
        time.sleep(1)
        os.system('git clone https://github.com/maldevel/IPGeoLocation')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user =="4":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling trackout")
        time.sleep(1)
        os.system('git clone https://github.com/abaykan/trackout.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user == "5":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling IP-Tracer")
        time.sleep(1)
        os.system('git clone https://github.com/rajkumardusad/IP-Tracer.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    else:
        print("\t[!] Please Select Correctly")
        time.sleep(2)
        os.system('clear')
        return ipTracking()

def editor():
    print("""
    [1].Vim
    [2].Nano""")

    user = input("Select Number: ")
    if user == "1" :
        os.system('clear')
        print('\tInstalling Vim')
        time.sleep(1)
        os.system('apt install vim -y')
        time.sleep(3)
        os.system('clear')
        print("\tDone Installing")
        time.sleep(3)
        return back()

    elif user == "5":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Nano")
        time.sleep(1)
        os.system('apt install nano -y')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    else:
        print("\t[!] Please Select Correctly")
        time.sleep(2)
        os.system('clear')
        return editor()

def pp():
    print("""
    [1].hydra
    [2].zphisher
    [3].BruteX
    [4].Facebook-phishing
    [5].Mobile_Legend-phishing
    [6].PUBG-BGMI_Phishing""")

    user = input("Select Number: ")
    if user == "1" :
        os.system('clear')
        print('\tInstalling hydra')
        time.sleep(1)
        os.system('git clone https://github.com/vanhauser-thc/thc-hydra.git')
        time.sleep(3)
        os.system('clear')
        print("\tDone Installing")
        time.sleep(3)
        return back()

    elif user == "2":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling zphisher")
        time.sleep(1)
        os.system('git clone https://github.com/htr-tech/zpisher')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user == "3":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling BruteX")
        time.sleep(1)
        os.system('git clone https://github.com/MrHacker-X/BruteX.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user == "4":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Facebook-phishing")
        time.sleep(1)
        os.system('git clone https://github.com/Crypt-tors/Facebook-phishing')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user == "5":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling Mobile_Legend-Phishing")
        time.sleep(1)
        os.system('git clone https://github.com/OnlineHacKing/Mobile_Legend-Phishing.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    elif user == "6":
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        print("\tInstalling PUBG-BGMI_Phishing")
        time.sleep(1)
        os.system('git clone https://github.com/OnlineHacKing/PUBG-BGMI_Phishing.git')
        time.sleep(3)
        os.system('clear')
        print("\t[!] Done Installing")
        time.sleep(3)
        return back()

    else:
        print("\t[!] Please Select Correctly")
        time.sleep(2)
        os.system('clear')
        return pp()





def list():
    print("""
    [1].Information Gathering
    [2].Vulnerability Scanner
    [3].IP-Tracking
    [4].Editor
    [5].PasswordAttack/Phishing
    """)

#THEMAIN
def menu():
    design()
    list()
    def main():
        while True:
            user = input("Select Number: ")
            if user == "1":
                informationGathering()
            elif user == "2":
                vulnerability()
            elif user == "3":
                ipTracking()
            elif user == "4":
                editor()
            elif user == "5":
                pp()
            else:
                print("\t[!] Please Select Correctly")
                time.sleep(2)
                os.system('clear')
                return menu() and main()
    main()


menu()
