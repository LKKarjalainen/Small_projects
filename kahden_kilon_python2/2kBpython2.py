#!/usr/bin/env python2
# Kahden kilon pyytton 2
# Author: Lassi Karjalainen

import time
import os

logo = [                                            
"............................................................\n"
".........................::::---:::.........................\n"
"......................=**************-......................\n"
".....................******************.....................\n"
"....................:**-.:+************:....................\n"
"....................:**-..+************:....................\n"
"....................:******************:....................\n"
".....................::::::::::********:..:::::::...........\n"
"............::-----------------********:..--------..........\n"
"..........=****************************:..---------.........\n"
".........******************************:..---------:........\n"
"........-*****************************-..:----------........\n"
"........+**************************+-:..:-----------........\n"
"........*************=-...............:-------------........\n"
"........***********+...::---------------------------........\n"
"........**********+...-----------------------------:........\n"
"........-*********=..------------------------------.........\n"
".........*********=..----------------------------:..........\n"
".........:********=..--------::::::::::::::::::.............\n"
"...........-=+****-..--------...............................\n"
".....................------------------.....................\n"
".....................-------------..:--.....................\n"
".....................-------------...--.....................\n"
".....................------------------.....................\n"
"......................:--------------:......................\n"
"...........................:::::............................\n"
"............................................................\n"
]

while True:
    # Clear  
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in logo:
        print line
    time.sleep(1)