#!/usr/bin/env python2
# Puolen kilon pyytton 2
# Author: Lassi Karjalainen

import time
import os

logo = [                                            
"        :==:        \n"
"      .=:***+.      \n"
"   .::::::=*+.::.   \n"
"  .*********=.:::   \n"
"  :***:.:::::::::   \n"
"   =**.:::......    \n"
"       ::::..       \n"
"        ....        \n"
]

while True:
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in logo:
        print line
    # Sleeeep
    time.sleep(1)