import sys, os
print("Tool for unlocking bootloader on (most) MTK devices using mtkclient.")
print("OS: " + sys.platform)
print("Downloading mtkclient...")
print("Checking for git...")
if os.system("git --version") != 0:
    print("Git not found. Please install git.")
    print("Exiting...")
    exit()
print("Downloading mtkclient...")
if os.system("git clone https://github.com/bkerler/mtkclient.git") != 0:
    print("Failed to download mtkclient.")
    print("Exiting...")
    exit()
print("Downloading mtkclient done.")
print("Installing mtkclient...")
if sys.platform == "win32":
    os.system("cd mtkclient && python -m pip install -r requirements.txt")
    print("Installing usbdk...")
    os.system("curl https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi -o UsbDk.msi")
    os.system("msiexec /i UsbDk.msi /qn")
    print("Installing mtk drivers... ")
    os.system("curl https://dumpyy.gq/files/android/mtkdriver.exe -o mtkdriver.exe")
    os.system("mtkdriver.exe")
else:
    os.system("cd mtkclient && pip3 install -r requirements.txt && python3 setup.py build && python3 setup.py install")
print("Installing mtkclient done.")

print("Would you like to\n[1] Unlock bootloader\n[2] Unbrick device\n[3] Exit")
choice = input("Enter your choice: ")
if choice == "1":
    print("Unlocking bootloader...")
    print("Make sure your device is Powered Off and ready to enter BROM mode.")
    os.system("cd mtkclient && mtk da seccfg unlock")
    print("Unlocking bootloader done.")
    print("Exiting...")
    exit()
elif choice == "2":
    print("Unbricking device...")
    print("Downloading SP Flash Tool...")