try:
    from termcolor import colored
except ImportError():
    print("This script is about to install \"termcolor\" to your system, keep connect to the internet...")
    os.system('sudo apt install python-pip3')
    os.system('pip3 install termcolor')

import os
import sys
import subprocess as sp


print("Python3 Plymouth Theme Installer ")
print("Version: v1.5")
print('\033[1m' + "*This script is just for Ubuntu and it's deriverate"+'\033[0m')

def menu():
    print("")
    print("Menu : ")
    print("1. Move a plymouth theme to /usr/share/plymouth/themes")
    print("2. Add a plymouth theme to default.plymouth")
    print("3. Change the currently applied plymouth theme")
    print("4. List the avaible theme in /usr/share/plymouth/themes")
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
        themeName = str(input("The unlisted theme directory: "))
        os.system("locate /usr/share/plymouth/themes/%s/*.plymouth" %themeName)
        plymouthFile = sp.getoutput("locate /usr/share/plymouth/themes/%s/*.plymouth" %themeName)
        os.system("sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth %s 100" %(plymouthFile))
        print("Done.")
        print("Type 3 to apply the theme in boot")

    elif choice == '1':
        print("")
        newTheme = input("Theme directory:")
        os.system("sudo mv %s /usr/share/plymouth/themes/" %(newTheme))
        print("Done.")
        print("Type 2 to add the theme to default.plymouth")
    
    elif choice == '3':
        os.system('clear')
        print('List of available themes')
        os.system(selectTheme)
        os.system(update_initramfs)
        print('Theme applied')
        print('Type 2 to reboot')

    elif choice == '4':
        print("\nList of themes in /usr/share/plymouth/themes:\n")
        listing = sp.getoutput("ls /usr/share/plymouth/themes")
        print(colored('\033[1m' + listing + '\033[0m', 'green'))

    elif choice == '5':
        os.system("init 6")
        
    elif choice == '6':
        pass
    
    elif choice == '?':
        menu()
        
    else:
        print("Your Input isn\'t valid!")
