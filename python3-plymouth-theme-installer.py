from termcolor import colored
import os
import sys
import subprocess as sp


print("Welcome to Python3 Plymouth Theme Installer ")
print("Version: v1.5")
print("This app methode inspirated form gdisk, so this app is like gidsk...")
print('\033[1m' + "(*Note! This script is just for UBUNTU adn his child OS, OK?!)"+'\033[0m')

def menu():
    print("")
    print("The Choises Menu : ")
    print("1. Move the plymouth theme to /usr/share/plymouth/themes")
    print("2. Listing your plymouth theme to default.plymouth")
    print("3. Change the applied plymouth theme")
    print("4. The avaible theme in /usr/share/plymouth/themes")
    print("5. Reboot")
    print("6. Exit")
    
    print("?. Print this menu")


selectTheme = 'sudo update-alternatives --config default.plymouth'
update_initramfs = "sudo update-initramfs -u -k all"

choice = ''

while choice != '6' :
    choice = input("\nType ? for help : ")
    if choice == '2':
        print("")
        themeName = str(input("What your theme isn\'t listed in default.plymouth? : "))
        os.system("locate /usr/share/plymouth/themes/%s/*.plymouth" %themeName)
        plymouthFile = sp.getoutput("locate /usr/share/plymouth/themes/%s/*.plymouth" %themeName)
        os.system("sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth %s 100" %(plymouthFile))
        print("OK, Insha Allah now your theme is listed in default.plymouth ...")
        print("Type \"3\" to apply your theme in boot")

    elif choice == '1':
        print("")
        newTheme = input("Where do you put the theme? Write the full path here! :")
        os.system("sudo mv %s /usr/share/plymouth/themes/" %(newTheme))
        print("OK, Your theme is moved to /usr/share/plymouth/themes ...")
        print("Type \"2\" to listing your theme in default.plymouth")
    
    elif choice == '3':
        os.system('clear')
        header = "\n--- GET READY TO APPLYING YOUR THEMES ---\n"
        print(colored('\033[1m' + header +'\033[0m', 'blue'))
        os.system(selectTheme)
        os.system(update_initramfs)
        print('OK! Your theme applied!')
        print("You can reboot your computer now to test your new boot screen...")

    elif choice == '4':
        print("\nThis is your theme in /usr/share/plymouth/themes now...\n")
        listing = sp.getoutput("ls /usr/share/plymouth/themes")
        print(colored('\033[1m' + listing + '\033[0m', 'green'))
        print("\nSorry, it\'s not written in order...")

    elif choice == '5':
        os.system("init 6")
        
    elif choice == '6':
        pass
    
    elif choice == '?':
        menu()
        
    else:
        print("Your Input isn\'t valid!")
else:
    print("Thanks for using this app!")
            
    
