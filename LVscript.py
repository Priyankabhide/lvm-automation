import os
import pyfiglet as fg

#Logical Volume Creation

def LvCreate(diskName, vgName, lvName, size, dirName):
    os.system(f'pvcreate {diskName}')
    os.system(f'vgcreate {vgName} {diskName}')
    os.system(f'vgdisplay {vgName}')
    os.system(f'lvcreate --size {size} --name {lvName} {vgName}')
    os.system(f'mkfs.ext4 /dev/{vgName}/{lvName}')
    os.system(f'mount /dev/{vgName}/{lvName} {dirName}')
    os.system(f'lvdisplay /dev/{vgName}/{lvName}')
    os.system('sleep 5')

#Extend the LV

def LvExtend( extDName, extVName, exsize, extLName):
    os.system(f'pvcreate {extDName}')
    os.system(f'vgextend {extVName} {extDName}')
    os.system('sleep 1')
    os.system(f'lvextend --size {exsize} /dev/{extVName}/{extLName}')
    os.system(f'resize2fs /dev/{extVName}/{extLName}')
    os.system('sleep 3')

#Reduce the LV Size

def LvReduce(redDirName, redVName, redLName, size):
    os.system(f'umount -v {redDirName}')
    os.system(f'e2fsck -ff /dev/mapper/{redVName}-{redLName}')
    os.system(f'resize2fs /dev/mapper/{redVName}-{redLName} {size}')
    os.system(f'lvreduce -L {size} /dev/mapper/{redVName}-{redLName} -y')
    os.system(f'mount /dev/mapper/{redVName}-{redLName} {redDirName}')
    os.system('sleep 3')

#Deleting the LV
def LvRemove(dirName, vgName, lvNName, diskName):
    os.system(f'umount -v {dirName}')
    os.system(f'lvremove /dev/{vgName}/{lvName} -y')
    os.system(f'vgremove {vgName}')
    os.system(f'pvremove {diskName}')
    os.system('sleep 5')
    os.system('df -h')
    os.system('sleep 5')
    os.system('fdisk -l')
    os.system('sleep 5')

#List the available disks
def ListDisk():
    os.system('fdisk -l')
    os.system('sleep 5')

#Display Volumes

def show():
    os.system('df -h')
    os.system('sleep 3')

#New Screen

def clear():
    os.system('clear')

while True:
    clear()
    os.system('tput setaf 6')
    print("\n                       -----------------------------------------------------')
    title = fg.figlet_format('                      LVM AUTOMATION' , font='bubble')
    print(title)
    print('                       ------------------------------------------------------')

    os.system('tput setaf 7')

    print("\n\t\t\t************  \t WELCOME TO THE MENU \t  ************\n")

    os.system("tput setaf 6")
    ch = input("\n\t\t\t\t 1 : Create Logical Volume \n\t\t\t\t 2 : Extend Logical Volume \n\t\t\t\t 3 : Reduce Logical Volume  \n\t\t\t\t 4 : Delete entire Environment \n\t\t\t\t 5 : Display Volumes \n\t\t\t\t 6 : Display the Storage attached \n\t\t\t\t q : Exit \n\n\n\t\t\t\t Type Your Input Here :  ")
    os.system("tput setaf 7")
    if ch.strip() == "1":
        diskName = input("Enter the Disk Name : ")
        vgName = input("Enter Volume Group Name : ")
        lvName = input("Enter Logical Volume Name : ")
        size = input("Enter the size for the Logical Volume : ")
        dirName = input('Enter the directory for mounting the LV :')
        LvCreate(diskName, vgName, lvName, size,  dirName)

    elif ch.strip() == "2":
        extDName = input("Enter the new disk name : ")
        extVName = input("Enter the VG to extend : ")
        extLName = input("Enter the LV to extend : ")
        exsize = input("Enter the LV size to extend : ")
        LvExtend(extDName, extVName, exsize, extLName)
        #os.system('clear')

    elif ch.strip() == "3":
        redDirName = input("Enter the mounted directory : ")
        redVName  = input("Enter the Volume Group to reduce : ")
        redLName = input("Enter the Logical Volume to reduce : ")
        size = input("Enter the size to be reduced to : ")
        LvReduce(redDirName, redVName, redLName, size)
        #os.system('clear')

    elif ch.strip() == "4":
        dirName = input("Enter the mounted directory : ")
        vgName = input("Enter the VG Name to delete : ")
        lvName = input("Enter the LV Name to delete : ")
        diskName = input("Enter the PV Name to delete : ")
        LvRemove(dirName, vgName, lvName, diskName)
        #os.system('clear')

    elif ch.strip() == "5":
        show()
        #os.system('clear')

    elif ch.strip() == "6" :
        ListDisk()
        #os.system('clear')

    elif ch.strip() == "q":
        print("Thanks for Using My tool.\n\n")
        break

    else:
        print("Invalid Input!\n\n")
        os.system('sleep 2')

os.system("tput setaf 7")


