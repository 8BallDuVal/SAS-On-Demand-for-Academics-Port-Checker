# SAS OnDemand for Academics Port Checker

Program that checks for blocked network ports associated with the hostnames used by [SAS OnDemand for Academics](https://welcome.oda.sas.com/).
The program checks different combinations of ports/hostnames depending on which SAS OnDemand for Academics software the user is using, and which region the user is in (US, EU, AP). 

This program uses a Graphical User Interface (GUI) to obtain user input, and display the resulting output. 
The resulting output can then be saved as a text file to their Desktop, which the user can send to SAS Technical Support for further assitance if necessary. 

# How to Use the Program
Windows: In the Windows Folder of this repository, download the **PortChecker.exe** file to run the executable program.
- Your Anti-Virus software may quarantine this file as it is an unsigned executable. 
    - Bypass your Anti-Virus software and allow your computer to run the PortChecker.exe file. 
- If you have Python 3 installed, you can also download the source code file (PortChecker.py) and run the program using your Python interpreter. 

# Program Details:
- Written in Python 3.6.5. Packages used:
    - tkinter 
    - base64
    - socket
    - os
    - webbrowser

- Self-Extracting Executables for Windows was created using [PyInstaller](https://pypi.org/project/PyInstaller/). 

### Notes for future reference
Command I ran to generate the executable:
```
pyinstaller.exe --onefile --noconsole PortChecker.py
```
